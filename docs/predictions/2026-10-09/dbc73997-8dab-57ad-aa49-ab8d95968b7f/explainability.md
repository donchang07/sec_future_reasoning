# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: dbc73997-8dab-57ad-aa49-ab8d95968b7f
Cutoff / prediction: 2026-10-08T22:57:18.083937+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-08T06:30:00+00:00', 'source_refs': ['raw:9903a00eea495837c973c8c1c94072f2d8bfea9aadcf8b98b9b8e20bcdc00e55'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 194000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 40.5017% | 37.7604% | 21.7379% | 6.0002% | 15.0000% | 0.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1m | 39.7624% | 38.0597% | 22.1779% | 3.1041% | 0.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 39.7856% / 38.4529% / 21.7615% | 40.5017% / 37.7604% / 21.7379% | [0.7160857207616556, -0.692441631481816, -0.023644089279828417] |
| 1m | 39.7624% / 38.0597% / 22.1779% | 39.7624% / 38.0597% / 22.1779% | [0.0, 0.0, 0.0] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 16.455023315833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-08T22:57:17.479190Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-08T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "9903a00eea495837c973c8c1c94072f2d8bfea9aadcf8b98b9b8e20bcdc00e55",
    "reason": null,
    "released_at": null,
    "rows": 229,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 16.455023315833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-08T22:57:17.857752Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-08T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 16.455023315833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-08T22:57:17.700336Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-08T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 3.455023315833333,
    "authority": "official_original",
    "collected_at": "2026-10-08T22:57:17.544486Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-08T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549",
    "reason": null,
    "released_at": null,
    "rows": 194,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-08T22:57:17.915931Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f5b90fa08e2a06bf67d65b1573bc26247ae72d0d1e248e924e612acef636cc6b",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 40.45502331583333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-08T22:57:17.939851Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-07T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "854fd6a23b65649f4d5b9933408668a648c7b3f5821d71804fedc211f454cc7d",
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
    "collected_at": "2026-10-08T22:57:18.083937Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "9bf45f3306cd3e763c30597fef2b87fc90c4bbd7c8458b96aebb8cc159aaabf4",
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
    "collected_at": "2026-10-08T22:57:17.857752Z",
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
    "collected_at": "2026-10-08T22:57:17.857752Z",
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
    "collected_at": "2026-10-08T22:57:17.857752Z",
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
    "collected_at": "2026-10-08T22:57:17.857752Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-08T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-02T06:30:00+00:00'}, '30m': {'count': 229, 'last': '2026-10-08T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:854fd6a23b65649f4d5b9933408668a648c7b3f5821d71804fedc211f454cc7d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-10-01T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "dbc73997-8dab-57ad-aa49-ab8d95968b7f/1w/technical",
  "bearish_alignment": 0.13333333333333336,
  "bullish_alignment": 0.26666666666666666,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 9087.428642594856,
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
      4918,
      4928
    ],
    "bottom_score": 0.0,
    "rsi": 47.81934073307465,
    "sma": [
      199405.0,
      188401.66666666666,
      189056.66666666666
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
      4915,
      4924
    ],
    "top_score": 0.0,
    "volume_ratio": 0.5813296625740929
  },
  "primary": "30m",
  "reflexivity_effect": 0.015,
  "regime_effect": 0.0225,
  "sell_liquidity": null,
  "wave": {
    "atr": 1513.442348559977,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 199300.0,
    "bottom_pivots": [
      217,
      224
    ],
    "bottom_score": 0.15,
    "rsi": 34.352908660934375,
    "sma": [
      197550.0,
      199160.0,
      203564.58333333334
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
    "top_neckline": 195200.0,
    "top_pivots": [
      219,
      226
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'dbc73997-8dab-57ad-aa49-ab8d95968b7f/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.015, 'regime_effect': 0.0225}
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
    "hypothesis_id": "fafee269-a080-53ab-a982-3201e0c00e05",
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
    "hypothesis_id": "fafee269-a080-53ab-a982-3201e0c00e05",
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
    "hypothesis_id": "fafee269-a080-53ab-a982-3201e0c00e05",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.22983749999999997
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
    "hypothesis_id": "b356e1c8-c965-5fb9-84c4-d286a5200551",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "b356e1c8-c965-5fb9-84c4-d286a5200551",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.016820850155238404
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.09018903341045936, 0.11245406296456761, -0.022265029554116578] | {'down': 0.35112454062964565, 'flat': 0.24977734970445883, 'up': 0.39909810966589543} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.35112454062964565, 'flat': 0.24977734970445883, 'up': 0.39909810966589543} | [1.614002127760178, -1.2086721162359038, -0.4053300115242603] | {'down': 0.3390378194672866, 'flat': 0.24572404958921623, 'up': 0.4152381309434972} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3390378194672866, 'flat': 0.24572404958921623, 'up': 0.4152381309434972} | [3.6077227346801966, -2.6431319717661217, -0.964590762914086] | {'down': 0.3126064997496254, 'flat': 0.23607814196007537, 'up': 0.4513153582902992} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3126064997496254, 'flat': 0.23607814196007537, 'up': 0.4513153582902992} | [3.6492818845798802, -2.5968384750506948, -1.0524434095291775] | {'down': 0.28663811499911845, 'flat': 0.2255537078647836, 'up': 0.487808177136098} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.28663811499911845, 'flat': 0.2255537078647836, 'up': 0.487808177136098} | [-7.579089010814755, 8.875679121913505, -1.296590111098761] | {'down': 0.3753949062182535, 'flat': 0.212587806753796, 'up': 0.41201728702795043} |
| 5 | E10/causal | ['dbc73997-8dab-57ad-aa49-ab8d95968b7f/1w/technical'] | {'down': 0.3753949062182535, 'flat': 0.212587806753796, 'up': 0.41201728702795043} | [0.9448742818036981, -0.921667185698194, -0.023207096105493097] | {'down': 0.36617823436127156, 'flat': 0.21235573579274106, 'up': 0.4214660298459874} |
| 6 | E17/scenario | ['c75b78e5-5a56-5ba0-9173-c607198f94be', '034a187d-4d07-5906-ab2c-230d7d33f0de', 'c45564d1-3b9d-5131-b071-c17a4706c922', 'dd88f9f0-19a5-5ed8-9041-a0ef17516a03'] | {'down': 0.36617823436127156, 'flat': 0.21235573579274106, 'up': 0.4214660298459874} | [0.5140237688808169, 2.3613695985487793, -2.8753933674295906] | {'down': 0.38979193034675935, 'flat': 0.18360180211844515, 'up': 0.4266062675347956} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.38979193034675935, 'flat': 0.18360180211844515, 'up': 0.4266062675347956} | [-1.19181462953446, -0.7214116555854744, 1.9132262851199315] | {'down': 0.3825778137909046, 'flat': 0.20273406496964447, 'up': 0.414688121239451} |
| 8 | E13/history | [] | {'down': 0.3825778137909046, 'flat': 0.20273406496964447, 'up': 0.414688121239451} | [0.0, 0.0, 0.0] | {'down': 0.3825778137909046, 'flat': 0.20273406496964447, 'up': 0.414688121239451} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3825778137909046, 'flat': 0.20273406496964447, 'up': 0.414688121239451} | [-0.9671079074463407, -0.4973508212553768, 1.4644587287017146] | {'down': 0.37760430557835084, 'flat': 0.21737865225666161, 'up': 0.4050170421649876} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:854fd6a23b65649f4d5b9933408668a648c7b3f5821d71804fedc211f454cc7d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-10-01T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "dbc73997-8dab-57ad-aa49-ab8d95968b7f/1m/technical",
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
    "atr": 24272.69518400249,
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
      1025,
      1032
    ],
    "bottom_score": 0.0,
    "rsi": 56.50121698277543,
    "sma": [
      197720.0,
      134290.83333333334,
      92659.58333333333
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
      1027,
      1035
    ],
    "top_score": 0.1,
    "volume_ratio": 0.97794445414138
  },
  "primary": "1d",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 9087.428642594856,
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
      4918,
      4928
    ],
    "bottom_score": 0.0,
    "rsi": 47.81934073307465,
    "sma": [
      199405.0,
      188401.66666666666,
      189056.66666666666
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
      4915,
      4924
    ],
    "top_score": 0.0,
    "volume_ratio": 0.5813296625740929
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'dbc73997-8dab-57ad-aa49-ab8d95968b7f/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "037db45b-19d0-55d0-ba33-361eb9272967",
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
    "hypothesis_id": "037db45b-19d0-55d0-ba33-361eb9272967",
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
    "hypothesis_id": "037db45b-19d0-55d0-ba33-361eb9272967",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.20249999999999996
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
    "hypothesis_id": "b517b633-a91d-5610-a431-6208c1f4d506",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "b517b633-a91d-5610-a431-6208c1f4d506",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.044158350155238404
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.09207583339332359, 0.11480792676916707, -0.022732093375843476] | {'down': 0.35114807926769165, 'flat': 0.24977267906624157, 'up': 0.3990792416660668} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.35114807926769165, 'flat': 0.24977267906624157, 'up': 0.3990792416660668} | [0.5509594670282447, -0.41450629671812567, -0.13645317031011628] | {'down': 0.3470030163005104, 'flat': 0.2484081473631404, 'up': 0.40458883633634923} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3470030163005104, 'flat': 0.2484081473631404, 'up': 0.40458883633634923} | [2.86490814045135, -2.1241789257066266, -0.7407292147447203] | {'down': 0.3257612270434441, 'flat': 0.2410008552156932, 'up': 0.43323791774086273} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3257612270434441, 'flat': 0.2410008552156932, 'up': 0.43323791774086273} | [2.9036729280837283, -2.102324612168738, -0.8013483159150098] | {'down': 0.30473798092175675, 'flat': 0.2329873720565431, 'up': 0.4622746470217} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.30473798092175675, 'flat': 0.2329873720565431, 'up': 0.4622746470217} | [-5.629823735069811, 6.7133920358187655, -1.083568300748941] | {'down': 0.3718719012799444, 'flat': 0.2221516890490537, 'up': 0.4059764096710019} |
| 5 | E10/causal | ['dbc73997-8dab-57ad-aa49-ab8d95968b7f/1m/technical'] | {'down': 0.3718719012799444, 'flat': 0.2221516890490537, 'up': 0.4059764096710019} | [0.2556492605148619, -0.25034678276278366, -0.0053024777520727095] | {'down': 0.36936843345231657, 'flat': 0.22209866427153296, 'up': 0.4085329022761505} |
| 6 | E17/scenario | ['faf63d03-036e-5761-a63c-c67a21855d5c', '4fe8535e-56b3-5726-be61-bb54e26e1c35', 'a7168dd1-c79b-5295-83bc-673d76adf3fd', '511dad64-078a-588e-8ed2-d54f32d7de5a'] | {'down': 0.36936843345231657, 'flat': 0.22209866427153296, 'up': 0.4085329022761505} | [0.8311365608196952, 2.4622219051629757, -3.293358465982674] | {'down': 0.3939906525039463, 'flat': 0.18916507961170623, 'up': 0.4168442678843475} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3939906525039463, 'flat': 0.18916507961170623, 'up': 0.4168442678843475} | [-1.0655107677767228, -0.7739229248030555, 1.8394336925797754] | {'down': 0.38625142325591577, 'flat': 0.20755941653750398, 'up': 0.40618916020658025} |
| 8 | E13/history | [] | {'down': 0.38625142325591577, 'flat': 0.20755941653750398, 'up': 0.40618916020658025} | [0.0, 0.0, 0.0] | {'down': 0.38625142325591577, 'flat': 0.20755941653750398, 'up': 0.40618916020658025} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.38625142325591577, 'flat': 0.20755941653750398, 'up': 0.40618916020658025} | [-0.8565025677612081, -0.5654235890428461, 1.4219261568040487] | {'down': 0.3805971873654873, 'flat': 0.22177867810554447, 'up': 0.39762413452896817} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '6fb3db5ec912060eb8f240847e2216d2d5e5ecb2e8ad57401a417b80b471b67a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '6fb3db5ec912060eb8f240847e2216d2d5e5ecb2e8ad57401a417b80b471b67a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '6fb3db5ec912060eb8f240847e2216d2d5e5ecb2e8ad57401a417b80b471b67a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '6fb3db5ec912060eb8f240847e2216d2d5e5ecb2e8ad57401a417b80b471b67a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '6fb3db5ec912060eb8f240847e2216d2d5e5ecb2e8ad57401a417b80b471b67a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '6fb3db5ec912060eb8f240847e2216d2d5e5ecb2e8ad57401a417b80b471b67a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '6fb3db5ec912060eb8f240847e2216d2d5e5ecb2e8ad57401a417b80b471b67a'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:854fd6a23b65649f4d5b9933408668a648c7b3f5821d71804fedc211f454cc7d'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1bba2bd45fb6476b5fbe531e07a7ea39589c615f16c2983e00d5f5631663b8f8#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:191ac7443f88e51d36d3f887153ed3d9eac6188a35ef10b0464d4e33f150166c#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:2eac7e46954d86c93138115f89545aa9c7eebe342aed8a6150bacdf70781b549#us_10y_yield@2026-10-01T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "dbc73997-8dab-57ad-aa49-ab8d95968b7f/1y/technical",
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
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 24272.69518400249,
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
      1025,
      1032
    ],
    "bottom_score": 0.0,
    "rsi": 56.50121698277543,
    "sma": [
      197720.0,
      134290.83333333334,
      92659.58333333333
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
      1027,
      1035
    ],
    "top_score": 0.1,
    "volume_ratio": 0.97794445414138
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'dbc73997-8dab-57ad-aa49-ab8d95968b7f/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "63d33253-b2e2-5297-aedb-c149b09b5188",
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
    "hypothesis_id": "63d33253-b2e2-5297-aedb-c149b09b5188",
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
    "hypothesis_id": "63d33253-b2e2-5297-aedb-c149b09b5188",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.18427499999999994
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
    "hypothesis_id": "9d1c72c6-1a9d-5260-8812-6ee08d995838",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "9d1c72c6-1a9d-5260-8812-6ee08d995838",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.0623833501552384
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
