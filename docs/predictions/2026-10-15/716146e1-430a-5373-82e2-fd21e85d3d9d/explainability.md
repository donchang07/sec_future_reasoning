# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 716146e1-430a-5373-82e2-fd21e85d3d9d
Cutoff / prediction: 2026-10-14T22:00:16.783136+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-14T06:30:00+00:00', 'source_refs': ['raw:12c443021919259f61b7c497d202ad99e1171f4a3af4a8cb9ac25fa1fa112940'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 173600.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 36.5303% | 41.9043% | 21.5654% | 6.3206% | 10.0000% | 50.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 37.8901% | 40.0157% | 22.0942% | 3.1783% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 38.4125% / 40.0197% / 21.5678% | 36.5303% / 41.9043% / 21.5654% | [-1.8822336204451229, 1.8846044993954814, -0.0023708789503501526] |
| 1m | 39.1023% / 38.7855% / 22.1121% | 37.8901% / 40.0157% / 22.0942% | [-1.2122233125957171, 1.2301061198853214, -0.017882807289593128] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.504661982222222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-14T22:00:15.837891Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "12c443021919259f61b7c497d202ad99e1171f4a3af4a8cb9ac25fa1fa112940",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504661982222222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-14T22:00:16.606355Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504661982222222,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-14T22:00:16.242940Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-14T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5046619822222222,
    "authority": "official_original",
    "collected_at": "2026-10-14T22:00:15.960430Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-14T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68",
    "reason": null,
    "released_at": null,
    "rows": 197,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-14T22:00:16.345796Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "40a64e004f5f0d18e167bb5554867d759ba0e1f3a97443b4f1ec4a67bd89b99a",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.504661982222224,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-14T22:00:16.447246Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-13T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "3882c2d264d91439f34319e687165304481336d3d4967dad47094d6b187216d5",
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
    "collected_at": "2026-10-14T22:00:16.783136Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "8870dfe396f7166a8fde34a0810651f97a417e16e499acbd318bcc1f54d7d6ea",
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
    "collected_at": "2026-10-14T22:00:16.345796Z",
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
    "collected_at": "2026-10-14T22:00:16.345796Z",
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
    "collected_at": "2026-10-14T22:00:16.345796Z",
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
    "collected_at": "2026-10-14T22:00:16.345796Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-10-14T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-09T06:30:00+00:00'}, '30m': {'count': 217, 'last': '2026-10-14T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3882c2d264d91439f34319e687165304481336d3d4967dad47094d6b187216d5'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_rsi_14@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_trend_alignment@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_volume_z@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-07T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "716146e1-430a-5373-82e2-fd21e85d3d9d/1w/technical",
  "bearish_alignment": 0.4,
  "bullish_alignment": 0.0,
  "buy_liquidity": null,
  "evidence_refs": [
    "bars:30m",
    "bars:1d"
  ],
  "flow_effect": 0.0,
  "higher": "1d",
  "higher_wave": {
    "atr": 9714.460906625693,
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
      4913,
      4923
    ],
    "bottom_score": 0.0,
    "rsi": 37.294719707057574,
    "sma": [
      196195.0,
      188090.0,
      189975.0
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
      4910,
      4919
    ],
    "top_score": 0.35,
    "volume_ratio": 1.1749673888379304
  },
  "primary": "30m",
  "reflexivity_effect": -0.04000000000000001,
  "regime_effect": -0.06,
  "sell_liquidity": null,
  "wave": {
    "atr": 2256.7491474385756,
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
    "bottom_neckline": 179700.0,
    "bottom_pivots": [
      198,
      206
    ],
    "bottom_score": 0.1,
    "rsi": 36.427126396362624,
    "sma": [
      175270.0,
      187259.16666666666,
      193630.41666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 174300.0,
    "top_pivots": [
      205,
      210
    ],
    "top_score": 0.5,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '716146e1-430a-5373-82e2-fd21e85d3d9d/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.04000000000000001, 'regime_effect': -0.06}
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
    "hypothesis_id": "342ffd35-765f-5a19-8712-3b1d0fb93769",
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
    "hypothesis_id": "342ffd35-765f-5a19-8712-3b1d0fb93769",
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
    "hypothesis_id": "342ffd35-765f-5a19-8712-3b1d0fb93769",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.08339120914151366
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
    "hypothesis_id": "3edee915-d2b3-55f4-adb8-1026503fa5e7",
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
    "hypothesis_id": "3edee915-d2b3-55f4-adb8-1026503fa5e7",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.3301819259320841
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-1.7747972622069674, 2.2346496780218716, -0.45985241581490144] | {'down': 0.3723464967802187, 'flat': 0.24540147584185099, 'up': 0.38225202737793035} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3723464967802187, 'flat': 0.24540147584185099, 'up': 0.38225202737793035} | [0.5777434588040697, -0.447555281899914, -0.1301881769041613] | {'down': 0.36787094396121955, 'flat': 0.24409959407280937, 'up': 0.38802946196597105} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.36787094396121955, 'flat': 0.24409959407280937, 'up': 0.38802946196597105} | [3.5640113836145684, -2.7129440542194736, -0.8510673293950916] | {'down': 0.3407415034190248, 'flat': 0.23558892077885846, 'up': 0.4236695758021167} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3407415034190248, 'flat': 0.23558892077885846, 'up': 0.4236695758021167} | [3.635086797207615, -2.6877245523603763, -0.9473622448472552] | {'down': 0.31386425789542105, 'flat': 0.2261152983303859, 'up': 0.4600204437741929} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.31386425789542105, 'flat': 0.2261152983303859, 'up': 0.4600204437741929} | [-7.635208094149082, 9.20261542089803, -1.5674073267489375] | {'down': 0.40589041210440135, 'flat': 0.21044122506289653, 'up': 0.38366836283270206} |
| 5 | E10/causal | ['716146e1-430a-5373-82e2-fd21e85d3d9d/1w/technical'] | {'down': 0.40589041210440135, 'flat': 0.21044122506289653, 'up': 0.38366836283270206} | [-1.9536376117665843, 1.9979128728188023, -0.044275261052201254] | {'down': 0.4258695408325894, 'flat': 0.20999847245237452, 'up': 0.3641319867150362} |
| 6 | E17/scenario | ['c21d23c4-79ff-5409-8b32-de5febc2999d', 'f72a62ea-75d7-5fbf-b903-ac858caaf973', '4b7cfbb9-7a76-5659-ae91-ea66ceca2df7', 'bf781781-e5ba-5244-a918-c654adc383ba'] | {'down': 0.4258695408325894, 'flat': 0.20999847245237452, 'up': 0.3641319867150362} | [0.9039984289917313, 1.9363884222613703, -2.8403868512531183] | {'down': 0.4452334250552031, 'flat': 0.18159460393984334, 'up': 0.37317197100495353} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4452334250552031, 'flat': 0.18159460393984334, 'up': 0.37317197100495353} | [-0.5043184897795705, -1.416546562875326, 1.920865052654905] | {'down': 0.4310679594264498, 'flat': 0.20080325446639238, 'up': 0.3681287861071578} |
| 8 | E13/history | [] | {'down': 0.4310679594264498, 'flat': 0.20080325446639238, 'up': 0.3681287861071578} | [0.0, 0.0, 0.0] | {'down': 0.4310679594264498, 'flat': 0.20080325446639238, 'up': 0.3681287861071578} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4310679594264498, 'flat': 0.20080325446639238, 'up': 0.3681287861071578} | [-0.2825893313141148, -1.202524122436588, 1.4851134537506971] | {'down': 0.41904271820208394, 'flat': 0.21565438900389935, 'up': 0.3653028927940167} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3882c2d264d91439f34319e687165304481336d3d4967dad47094d6b187216d5'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_rsi_14@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_trend_alignment@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_volume_z@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-07T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "716146e1-430a-5373-82e2-fd21e85d3d9d/1m/technical",
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
    "atr": 23181.788385145166,
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
      1024,
      1031
    ],
    "bottom_score": 0.0,
    "rsi": 54.03649354201776,
    "sma": [
      198045.0,
      136554.16666666666,
      93745.41666666667
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
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 0.3527739039220778
  },
  "primary": "1d",
  "reflexivity_effect": -0.034999999999999996,
  "regime_effect": -0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 9714.460906625693,
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
      4913,
      4923
    ],
    "bottom_score": 0.0,
    "rsi": 37.294719707057574,
    "sma": [
      196195.0,
      188090.0,
      189975.0
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
      4910,
      4919
    ],
    "top_score": 0.35,
    "volume_ratio": 1.1749673888379304
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '716146e1-430a-5373-82e2-fd21e85d3d9d/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "d4523522-d409-55be-86d5-0ca7990c4d79",
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
    "hypothesis_id": "d4523522-d409-55be-86d5-0ca7990c4d79",
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
    "hypothesis_id": "d4523522-d409-55be-86d5-0ca7990c4d79",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.09250370914151367
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
    "hypothesis_id": "8e207759-dfd9-51d3-8700-eb21a3fc534a",
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
    "hypothesis_id": "8e207759-dfd9-51d3-8700-eb21a3fc534a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.3210694259320842
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.6701325092852983, 0.8384000846258122, -0.16826757534052217] | {'down': 0.3583840008462581, 'flat': 0.24831732424659478, 'up': 0.39329867490714704} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3583840008462581, 'flat': 0.24831732424659478, 'up': 0.39329867490714704} | [0.25060616494234633, -0.19072987931156304, -0.05987628563078051] | {'down': 0.35647670205314247, 'flat': 0.24771856139028697, 'up': 0.3958047365565705} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.35647670205314247, 'flat': 0.24771856139028697, 'up': 0.3958047365565705} | [2.852837229511157, -2.1425900565682108, -0.7102471729429571] | {'down': 0.33505080148746036, 'flat': 0.2406160896608574, 'up': 0.4243331088516821} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.33505080148746036, 'flat': 0.2406160896608574, 'up': 0.4243331088516821} | [2.897641552118052, -2.1251361836461147, -0.7725053684719152] | {'down': 0.3137994396509992, 'flat': 0.23289103597613825, 'up': 0.4533095243728626} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3137994396509992, 'flat': 0.23289103597613825, 'up': 0.4533095243728626} | [-5.643377319722265, 6.7949588401152115, -1.1515815203929498] | {'down': 0.38174902805215133, 'flat': 0.22137522077220875, 'up': 0.39687575117563995} |
| 5 | E10/causal | ['716146e1-430a-5373-82e2-fd21e85d3d9d/1m/technical'] | {'down': 0.38174902805215133, 'flat': 0.22137522077220875, 'up': 0.39687575117563995} | [-1.7274485852807164, 1.7295707139279415, -0.002122128647227828] | {'down': 0.39904473519143074, 'flat': 0.22135399948573647, 'up': 0.3796012653228328} |
| 6 | E17/scenario | ['004e598c-42e5-58f4-a28d-49d20c56183e', 'e25e4d18-ccb8-529a-addb-389d5179321f', '25b4e731-7084-5607-92be-ccac6779c03e', '60675bca-8a63-5099-96c6-77ab3bafcfe3'] | {'down': 0.39904473519143074, 'flat': 0.22135399948573647, 'up': 0.3796012653228328} | [1.2042310564629677, 2.1112116519306445, -3.315442708393601] | {'down': 0.4201568517107372, 'flat': 0.18819957240180046, 'up': 0.39164357588746246} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4201568517107372, 'flat': 0.18819957240180046, 'up': 0.39164357588746246} | [-0.7408533571431952, -1.1031251500827233, 1.8439785072259212] | {'down': 0.40912560020990996, 'flat': 0.20663935747405968, 'up': 0.3842350423160305} |
| 8 | E13/history | [] | {'down': 0.40912560020990996, 'flat': 0.20663935747405968, 'up': 0.3842350423160305} | [0.0, 0.0, 0.0] | {'down': 0.40912560020990996, 'flat': 0.20663935747405968, 'up': 0.3842350423160305} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.40912560020990996, 'flat': 0.20663935747405968, 'up': 0.3842350423160305} | [-0.5333946628980291, -0.8969045321466751, 1.4302991950446986] | {'down': 0.4001565548884432, 'flat': 0.22094234942450666, 'up': 0.3789010956870502} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'e1f9b7234f9f601bffa0efe9592b7379631c63cb0eb48cf49cc957cb9421aed2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'e1f9b7234f9f601bffa0efe9592b7379631c63cb0eb48cf49cc957cb9421aed2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'e1f9b7234f9f601bffa0efe9592b7379631c63cb0eb48cf49cc957cb9421aed2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'e1f9b7234f9f601bffa0efe9592b7379631c63cb0eb48cf49cc957cb9421aed2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'e1f9b7234f9f601bffa0efe9592b7379631c63cb0eb48cf49cc957cb9421aed2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'e1f9b7234f9f601bffa0efe9592b7379631c63cb0eb48cf49cc957cb9421aed2'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'e1f9b7234f9f601bffa0efe9592b7379631c63cb0eb48cf49cc957cb9421aed2'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3882c2d264d91439f34319e687165304481336d3d4967dad47094d6b187216d5'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_rsi_14@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_trend_alignment@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#preferred_volume_z@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:9ca9842d91133f8e7a63d0b5f8f6895a0e7f3e9a527760f0aa955b86171f4de1#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7a8be05b4f7987243a9d9450fe9921711b11670a186496a673d6d6b617f587d5#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:dc2a57514c7224dfdf7189d5d3ef28d51506901d2080cc2aabdf6be0269cfc68#us_10y_yield@2026-10-07T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "716146e1-430a-5373-82e2-fd21e85d3d9d/1y/technical",
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
    "atr": 23181.788385145166,
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
      1024,
      1031
    ],
    "bottom_score": 0.0,
    "rsi": 54.03649354201776,
    "sma": [
      198045.0,
      136554.16666666666,
      93745.41666666667
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
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 0.3527739039220778
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '716146e1-430a-5373-82e2-fd21e85d3d9d/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "102c4244-c3a2-5dba-b774-773d6dcfa4e0",
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
    "hypothesis_id": "102c4244-c3a2-5dba-b774-773d6dcfa4e0",
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
    "hypothesis_id": "102c4244-c3a2-5dba-b774-773d6dcfa4e0",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.11984120914151365
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
    "hypothesis_id": "d922498f-f910-5017-9eb1-126dc34186f7",
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
    "hypothesis_id": "d922498f-f910-5017-9eb1-126dc34186f7",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2937319259320842
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
