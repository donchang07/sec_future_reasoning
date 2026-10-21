# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: e2a1f30f-e478-55a2-93bf-30a930848b16
Cutoff / prediction: 2026-10-21T22:00:15.420812+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-21T06:30:00+00:00', 'source_refs': ['raw:179b990db4139bc2fa57c34b464493d73f6e100ae00ee080cb24eb46142dc9fa'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 172200.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 37.9762% | 40.2539% | 21.7699% | 5.3957% | 0.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 37.7138% | 40.1544% | 22.1318% | 2.7378% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 37.9762% / 40.2539% / 21.7699% | 37.9762% / 40.2539% / 21.7699% | [0.0, 0.0, 0.0] |
| 1m | 38.8980% / 38.9007% / 22.2013% | 37.7138% / 40.1544% / 22.1318% | [-1.184215408041972, 1.2537030687474748, -0.06948766070550838] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.504283558888888,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-21T22:00:14.536811Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-21T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "179b990db4139bc2fa57c34b464493d73f6e100ae00ee080cb24eb46142dc9fa",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504283558888888,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-21T22:00:14.909536Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-21T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.504283558888888,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-21T22:00:14.964556Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-21T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.504283558888889,
    "authority": "official_original",
    "collected_at": "2026-10-21T22:00:14.596358Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-21T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1",
    "reason": null,
    "released_at": null,
    "rows": 202,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-21T22:00:15.037615Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "0bdf007921519667bd3b1af869c1e2c86a74bc34eee61d9282f54f810c64f141",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.504283558888886,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-21T22:00:15.073770Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-20T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "3ae704f1799f6222a8410d221a464ec4c14464043844487dd4537c3b39da2a36",
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
    "collected_at": "2026-10-21T22:00:15.419811Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "804e478ca6d57593a84caab3a7401c03b5e290a3ceef87f9a5189d91d895b1d0",
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
    "collected_at": "2026-10-21T22:00:14.964556Z",
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
    "collected_at": "2026-10-21T22:00:14.964556Z",
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
    "collected_at": "2026-10-21T22:00:14.965556Z",
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
    "collected_at": "2026-10-21T22:00:14.965556Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-10-21T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-16T06:30:00+00:00'}, '30m': {'count': 217, 'last': '2026-10-21T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3ae704f1799f6222a8410d221a464ec4c14464043844487dd4537c3b39da2a36'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_rsi_14@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_trend_alignment@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_volume_z@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-14T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "e2a1f30f-e478-55a2-93bf-30a930848b16/1w/technical",
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
    "atr": 10830.95312482108,
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
    "rsi": 42.06198490110937,
    "sma": [
      190375.0,
      187023.33333333334,
      190738.33333333334
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
    "volume_ratio": 0.7505988811330697
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 2383.64796277537,
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
      202,
      212
    ],
    "bottom_score": 0.0,
    "rsi": 55.304369206344354,
    "sma": [
      170135.0,
      167050.0,
      177057.08333333334
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
    "top_neckline": 163900.0,
    "top_pivots": [
      196,
      205
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'e2a1f30f-e478-55a2-93bf-30a930848b16/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "c810c272-bf6f-572c-b61f-1346aa802bf3",
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
    "hypothesis_id": "c810c272-bf6f-572c-b61f-1346aa802bf3",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075
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
    "hypothesis_id": "aa8cec28-b730-5120-a5ea-871b613cdac3",
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
    "hypothesis_id": "aa8cec28-b730-5120-a5ea-871b613cdac3",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.1607448057525353
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.8629853766732365, 1.080887012965187, -0.2179016362919478] | {'down': 0.36080887012965185, 'flat': 0.24782098363708052, 'up': 0.39137014623326766} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.36080887012965185, 'flat': 0.24782098363708052, 'up': 0.39137014623326766} | [3.564893653383161, -2.684170761613347, -0.8807228917698084] | {'down': 0.3339671625135184, 'flat': 0.23901375471938244, 'up': 0.42701908276709927} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3339671625135184, 'flat': 0.23901375471938244, 'up': 0.42701908276709927} | [3.6321322710218205, -2.6553171000852913, -0.976815170936543] | {'down': 0.30741399151266546, 'flat': 0.229245603010017, 'up': 0.4633404054773175} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.30741399151266546, 'flat': 0.229245603010017, 'up': 0.4633404054773175} | [-7.587273441269426, 9.119491840825095, -1.5322183995556542] | {'down': 0.3986089099209164, 'flat': 0.21392341901446046, 'up': 0.3874676710646232} |
| 4 | E10/causal | ['e2a1f30f-e478-55a2-93bf-30a930848b16/1w/technical'] | {'down': 0.3986089099209164, 'flat': 0.21392341901446046, 'up': 0.3874676710646232} | [-0.2589629636619961, 0.26090732424882135, -0.0019443605868307845] | {'down': 0.4012179831634046, 'flat': 0.21390397540859216, 'up': 0.38487804142800325} |
| 5 | E17/scenario | ['ab6bdead-1a1b-577c-a6b5-04509a1b7e83', '6fcd921a-6ddd-58ff-b328-8dbba29f4c29', '150a0c11-4705-59dc-9fd2-ad8bf02891bf', '0a7c535e-4fee-56f4-9faa-b3111db7b228'] | {'down': 0.4012179831634046, 'flat': 0.21390397540859216, 'up': 0.38487804142800325} | [0.797604331712809, 2.230270248748789, -3.027874580461609] | {'down': 0.4235206856508925, 'flat': 0.18362522960397606, 'up': 0.39285408474513134} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4235206856508925, 'flat': 0.18362522960397606, 'up': 0.39285408474513134} | [-0.7738641855053907, -1.1725786433919527, 1.946442828897346] | {'down': 0.411794899216973, 'flat': 0.20308965789294953, 'up': 0.38511544289007743} |
| 7 | E13/history | [] | {'down': 0.411794899216973, 'flat': 0.20308965789294953, 'up': 0.38511544289007743} | [0.0, 0.0, 0.0] | {'down': 0.411794899216973, 'flat': 0.20308965789294953, 'up': 0.38511544289007743} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.411794899216973, 'flat': 0.20308965789294953, 'up': 0.38511544289007743} | [-0.5353202498202092, -0.9256367500510121, 1.460956999871235] | {'down': 0.40253853171646287, 'flat': 0.21769922789166188, 'up': 0.37976224039187534} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3ae704f1799f6222a8410d221a464ec4c14464043844487dd4537c3b39da2a36'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_rsi_14@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_trend_alignment@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_volume_z@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-14T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "e2a1f30f-e478-55a2-93bf-30a930848b16/1m/technical",
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
    "atr": 10830.95312482108,
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
    "rsi": 42.06198490110937,
    "sma": [
      190375.0,
      187023.33333333334,
      190738.33333333334
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
    "volume_ratio": 0.7505988811330697
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'e2a1f30f-e478-55a2-93bf-30a930848b16/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "246535d1-9a8f-54ea-822e-34d502f22657",
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
    "hypothesis_id": "246535d1-9a8f-54ea-822e-34d502f22657",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075
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
    "hypothesis_id": "8b60ac2a-f64e-5fcb-826e-0c36e744099e",
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
    "hypothesis_id": "8b60ac2a-f64e-5fcb-826e-0c36e744099e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2883198057525353
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.6017116869356853, 0.7524996280552754, -0.1507879411195956] | {'down': 0.35752499628055273, 'flat': 0.24849212058880404, 'up': 0.39398288313064317} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.35752499628055273, 'flat': 0.24849212058880404, 'up': 0.39398288313064317} | [2.848852383028361, -2.141614034018735, -0.7072383490096201] | {'down': 0.3361088559403654, 'flat': 0.24141973709870784, 'up': 0.4224714069609268} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3361088559403654, 'flat': 0.24141973709870784, 'up': 0.4224714069609268} | [2.8948616401202387, -2.1249189376308264, -0.7699427024893984] | {'down': 0.3148596665640571, 'flat': 0.23372031007381386, 'up': 0.45142002336212916} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.3148596665640571, 'flat': 0.23372031007381386, 'up': 0.45142002336212916} | [-5.636596928184106, 6.801690360603247, -1.1650934324191453] | {'down': 0.3828765701700896, 'flat': 0.2220693757496224, 'up': 0.3950540540802881} |
| 4 | E10/causal | ['e2a1f30f-e478-55a2-93bf-30a930848b16/1m/technical'] | {'down': 0.3828765701700896, 'flat': 0.2220693757496224, 'up': 0.3950540540802881} | [-1.8193934325776095, 1.8256883239520683, -0.006294891374469813] | {'down': 0.40113345340961026, 'flat': 0.2220064268358777, 'up': 0.376860119754512} |
| 5 | E17/scenario | ['bf31da15-5826-504c-924c-cb8feb304409', '7ae550cf-0581-547b-85a0-a0017cfc9857', 'cbe3a9dc-5be5-56f4-8fe5-a851ae28e99a', '99b08d5c-acb9-5bf6-8776-17c6ab7435ec'] | {'down': 0.40113345340961026, 'flat': 0.2220064268358777, 'up': 0.376860119754512} | [1.2642032733533315, 2.1225792493788695, -3.386782522732179] | {'down': 0.42235924590339896, 'flat': 0.18813860160855592, 'up': 0.3895021524880453} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.42235924590339896, 'flat': 0.18813860160855592, 'up': 0.3895021524880453} | [-0.7315066071775622, -1.1594162781959072, 1.8909228853734639] | {'down': 0.4107650831214399, 'flat': 0.20704783046229056, 'up': 0.3821870864162697} |
| 7 | E13/history | [] | {'down': 0.4107650831214399, 'flat': 0.20704783046229056, 'up': 0.3821870864162697} | [0.0, 0.0, 0.0] | {'down': 0.4107650831214399, 'flat': 0.20704783046229056, 'up': 0.3821870864162697} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.4107650831214399, 'flat': 0.20704783046229056, 'up': 0.3821870864162697} | [-0.5049134430326951, -0.9221346188308444, 1.4270480618635144] | {'down': 0.40154373693313145, 'flat': 0.2213183110809257, 'up': 0.37713795198594274} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '251f1bb0ef044193975c9776eb4a271197ee9f9b0a334f1a46bcf55b00c7af4e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '251f1bb0ef044193975c9776eb4a271197ee9f9b0a334f1a46bcf55b00c7af4e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '251f1bb0ef044193975c9776eb4a271197ee9f9b0a334f1a46bcf55b00c7af4e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '251f1bb0ef044193975c9776eb4a271197ee9f9b0a334f1a46bcf55b00c7af4e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '251f1bb0ef044193975c9776eb4a271197ee9f9b0a334f1a46bcf55b00c7af4e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '251f1bb0ef044193975c9776eb4a271197ee9f9b0a334f1a46bcf55b00c7af4e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '251f1bb0ef044193975c9776eb4a271197ee9f9b0a334f1a46bcf55b00c7af4e'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:3ae704f1799f6222a8410d221a464ec4c14464043844487dd4537c3b39da2a36'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_rsi_14@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_trend_alignment@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#preferred_volume_z@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:bb216cf0799174c502fbeb6b200e2ec3e1e302f57960f0daf8dd6a05259cc33b#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:49ea1bf0e8ef858db464ecc52f1426fddf14ce5a164585f4b716d8272f8be9ac#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:ee0fe546e86151570445fe4bbfdbd479c8051a35ab26affea000812b24183bb1#us_10y_yield@2026-10-14T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "e2a1f30f-e478-55a2-93bf-30a930848b16/1y/technical",
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
Feedback applied once: {'batch_id': 'e2a1f30f-e478-55a2-93bf-30a930848b16/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "99aa05b5-792f-5382-a923-4ce4d219dcc4",
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
    "hypothesis_id": "99aa05b5-792f-5382-a923-4ce4d219dcc4",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.6075
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
    "hypothesis_id": "fdee8e89-7088-5e96-8ca6-e113e969976a",
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
    "hypothesis_id": "fdee8e89-7088-5e96-8ca6-e113e969976a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2336448057525353
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
