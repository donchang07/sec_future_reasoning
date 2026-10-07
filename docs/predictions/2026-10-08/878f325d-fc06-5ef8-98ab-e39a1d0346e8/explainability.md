# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 878f325d-fc06-5ef8-98ab-e39a1d0346e8
Cutoff / prediction: 2026-10-07T22:00:19.769106+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-07T06:30:00+00:00', 'source_refs': ['raw:152f126d5267132b0970a56a58b3405e8d9dc0ed99895eac51e9336cda3f5d65'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 198000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 39.1803% | 38.8087% | 22.0111% | 4.7962% | 35.0000% | 10.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1m | 38.4316% | 39.1308% | 22.4376% | 2.5090% | 0.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 37.9902% / 39.9460% / 22.0638% | 39.1803% / 38.8087% / 22.0111% | [1.1900253421669393, -1.137334127402867, -0.052691214764061245] |
| 1m | 38.4316% / 39.1308% / 22.4376% | 38.4316% / 39.1308% / 22.4376% | [0.0, 0.0, 0.0] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.505491418333333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-07T22:00:18.866475Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-07T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "152f126d5267132b0970a56a58b3405e8d9dc0ed99895eac51e9336cda3f5d65",
    "reason": null,
    "released_at": null,
    "rows": 229,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.505491418333333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-07T22:00:19.232933Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-07T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.505491418333333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-07T22:00:19.288957Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-07T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5054914183333334,
    "authority": "official_original",
    "collected_at": "2026-10-07T22:00:18.935789Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-07T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340",
    "reason": null,
    "released_at": null,
    "rows": 193,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-07T22:00:19.474354Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "4f1fc1e238be4df1539af88247c44fab1a4f1fe4bbeaec532e217f7041a3fbac",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50549141833333,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-07T22:00:19.513866Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-06T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "0322250462bfbf4eb6d8dcc39606cc55d60cfd7ea2de81369064d9e78cdab5a6",
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
    "collected_at": "2026-10-07T22:00:19.769106Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "7a221787b9435e8310fabfa289dc7c52e180e693b99f9f0e51c24720a9964d43",
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
    "collected_at": "2026-10-07T22:00:19.289957Z",
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
    "collected_at": "2026-10-07T22:00:19.289957Z",
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
    "collected_at": "2026-10-07T22:00:19.289957Z",
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
    "collected_at": "2026-10-07T22:00:19.289957Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-10-07T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-10-02T06:30:00+00:00'}, '30m': {'count': 229, 'last': '2026-10-07T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:0322250462bfbf4eb6d8dcc39606cc55d60cfd7ea2de81369064d9e78cdab5a6'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_rsi_14@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_trend_alignment@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_volume_z@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-30T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "878f325d-fc06-5ef8-98ab-e39a1d0346e8/1w/technical",
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
    "atr": 9324.923153563692,
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
    "rsi": 50.27332499490547,
    "sma": [
      199685.0,
      188261.66666666666,
      188610.0
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
    "volume_ratio": 0.7094033586165305
  },
  "primary": "30m",
  "reflexivity_effect": 0.024999999999999998,
  "regime_effect": 0.03749999999999999,
  "sell_liquidity": null,
  "wave": {
    "atr": 1269.707051273895,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "bottom_neckline": 203000.0,
    "bottom_pivots": [
      213,
      220
    ],
    "bottom_score": 0.35,
    "rsi": 42.23339454808591,
    "sma": [
      198747.5,
      199323.33333333334,
      204657.5
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 197600.0,
    "top_pivots": [
      217,
      225
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '878f325d-fc06-5ef8-98ab-e39a1d0346e8/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.024999999999999998, 'regime_effect': 0.03749999999999999}
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
    "hypothesis_id": "a64b9ab9-01b8-511c-a49a-8d8d6ed0ee35",
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
    "hypothesis_id": "a64b9ab9-01b8-511c-a49a-8d8d6ed0ee35",
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
    "hypothesis_id": "a64b9ab9-01b8-511c-a49a-8d8d6ed0ee35",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.1805625
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "a64b9ab9-01b8-511c-a49a-8d8d6ed0ee35",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.04925238743122387
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
    "hypothesis_id": "6fe26cda-6430-5445-9680-bcab90d0d046",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.3444863391784292, -0.25897566224187263, -0.08551067693656766] | {'down': 0.34741024337758125, 'flat': 0.24914489323063432, 'up': 0.4034448633917843} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34741024337758125, 'flat': 0.24914489323063432, 'up': 0.4034448633917843} | [1.270025058093388, -0.9481254427183394, -0.3218996153750403] | {'down': 0.33792898895039786, 'flat': 0.24592589707688392, 'up': 0.4161451139727182} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.33792898895039786, 'flat': 0.24592589707688392, 'up': 0.4161451139727182} | [2.399257974013241, -1.7636175746064853, -0.6356403994067589] | {'down': 0.320292813204333, 'flat': 0.23956949308281633, 'up': 0.4401376937128506} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.320292813204333, 'flat': 0.23956949308281633, 'up': 0.4401376937128506} | [2.4229804968877056, -1.7463140182218395, -0.6766664786658633] | {'down': 0.3028296730221146, 'flat': 0.2328028282961577, 'up': 0.46436749868172766} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3028296730221146, 'flat': 0.2328028282961577, 'up': 0.46436749868172766} | [-7.5353967347151, 9.052960133974885, -1.517563399259786] | {'down': 0.39335927436186346, 'flat': 0.21762719430355984, 'up': 0.38901353133457667} |
| 5 | E10/causal | ['878f325d-fc06-5ef8-98ab-e39a1d0346e8/1w/technical'] | {'down': 0.39335927436186346, 'flat': 0.21762719430355984, 'up': 0.38901353133457667} | [1.3511323613503323, -1.3442850519003013, -0.0068473094500254295] | {'down': 0.37991642384286045, 'flat': 0.21755872120905959, 'up': 0.40252485494808} |
| 6 | E17/scenario | ['2b57ef95-896c-5522-9dfc-f6e9b23f2ac0', '8d462f11-02e4-532a-853e-e9b603ef03cb', 'e1515ebf-2d37-571d-92df-e60282c1a5a2', 'cfb9b391-5138-56ab-83a8-61be2a3a598c'] | {'down': 0.37991642384286045, 'flat': 0.21755872120905959, 'up': 0.40252485494808} | [0.6835191390885009, 2.4428347285158694, -3.1263538676043616] | {'down': 0.40434477112801914, 'flat': 0.18629518253301597, 'up': 0.409360046338965} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.40434477112801914, 'flat': 0.18629518253301597, 'up': 0.409360046338965} | [-1.0053503248188822, -0.9390301017940195, 1.9443804266129043] | {'down': 0.39495447011007895, 'flat': 0.205738986799145, 'up': 0.3993065430907762} |
| 8 | E13/history | [] | {'down': 0.39495447011007895, 'flat': 0.205738986799145, 'up': 0.3993065430907762} | [0.0, 0.0, 0.0] | {'down': 0.39495447011007895, 'flat': 0.205738986799145, 'up': 0.3993065430907762} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.39495447011007895, 'flat': 0.205738986799145, 'up': 0.3993065430907762} | [-0.7503969730218274, -0.6867839820243249, 1.4371809550461467] | {'down': 0.3880866302898357, 'flat': 0.22011079634960648, 'up': 0.3918025733605579} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:0322250462bfbf4eb6d8dcc39606cc55d60cfd7ea2de81369064d9e78cdab5a6'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_rsi_14@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_trend_alignment@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_volume_z@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-30T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "878f325d-fc06-5ef8-98ab-e39a1d0346e8/1m/technical",
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
    "atr": 9324.923153563692,
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
    "rsi": 50.27332499490547,
    "sma": [
      199685.0,
      188261.66666666666,
      188610.0
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
    "volume_ratio": 0.7094033586165305
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '878f325d-fc06-5ef8-98ab-e39a1d0346e8/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "8a76072e-5137-5cf0-bb81-d758457815ae",
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
    "hypothesis_id": "8a76072e-5137-5cf0-bb81-d758457815ae",
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
    "hypothesis_id": "8a76072e-5137-5cf0-bb81-d758457815ae",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.13499999999999998
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8a76072e-5137-5cf0-bb81-d758457815ae",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.0036898874312238767
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
    "hypothesis_id": "9ab2fb39-2246-5f70-b388-f33196627799",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.010024050341278512, -0.007546845719746953, -0.0024772046215287835] | {'down': 0.3499245315428025, 'flat': 0.2499752279537847, 'up': 0.4001002405034128} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3499245315428025, 'flat': 0.2499752279537847, 'up': 0.4001002405034128} | [0.36725893519432007, -0.2760438920894226, -0.09121504310491135] | {'down': 0.3471640926219083, 'flat': 0.2490630775227356, 'up': 0.403772829855356} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3471640926219083, 'flat': 0.2490630775227356, 'up': 0.403772829855356} | [1.9032906031871244, -1.4166599951409287, -0.48663060804618463] | {'down': 0.332997492670499, 'flat': 0.24419677144227375, 'up': 0.42280573588722725} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.332997492670499, 'flat': 0.24419677144227375, 'up': 0.42280573588722725} | [1.9235917843498707, -1.4089302279015836, -0.514661556448287] | {'down': 0.31890819039148316, 'flat': 0.23905015587779088, 'up': 0.44204165373072596} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.31890819039148316, 'flat': 0.23905015587779088, 'up': 0.44204165373072596} | [-5.588227632553422, 6.8202459493151455, -1.2320183167617182] | {'down': 0.3871106498846346, 'flat': 0.2267299727101737, 'up': 0.38615937740519174} |
| 5 | E10/causal | ['878f325d-fc06-5ef8-98ab-e39a1d0346e8/1m/technical'] | {'down': 0.3871106498846346, 'flat': 0.2267299727101737, 'up': 0.38615937740519174} | [0.22074858492691085, -0.22058613109383618, -0.00016245383308577388] | {'down': 0.38490478857369625, 'flat': 0.22672834817184284, 'up': 0.38836686325446085} |
| 6 | E17/scenario | ['4997e1b3-6f44-53e4-91f4-1afadc3efa84', '0fbb51e4-31c7-5883-9499-659e6f89e4c1', 'ae6b785a-a702-5667-87a5-a0ceb3399e92', '5b646731-ef39-5e01-a29a-95b29c102cb9'] | {'down': 0.38490478857369625, 'flat': 0.22672834817184284, 'up': 0.38836686325446085} | [1.104843052999549, 2.394040983630724, -3.4988840366302703] | {'down': 0.4088451984100035, 'flat': 0.19173950780554014, 'up': 0.39941529378445634} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4088451984100035, 'flat': 0.19173950780554014, 'up': 0.39941529378445634} | [-0.8715272499085713, -0.995894305442313, 1.8674215553508788] | {'down': 0.39888625535558037, 'flat': 0.21041372335904893, 'up': 0.3907000212853706} |
| 8 | E13/history | [] | {'down': 0.39888625535558037, 'flat': 0.21041372335904893, 'up': 0.3907000212853706} | [0.0, 0.0, 0.0] | {'down': 0.39888625535558037, 'flat': 0.21041372335904893, 'up': 0.3907000212853706} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.39888625535558037, 'flat': 0.21041372335904893, 'up': 0.3907000212853706} | [-0.6384186884507925, -0.7577768560226406, 1.3961955444734357] | {'down': 0.39130848679535396, 'flat': 0.22437567880378328, 'up': 0.3843158344008627} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'ac472253a83f41b16cba0336b7b78fd1e4cc904c039dda43f5d3ed3fa8280bc3'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'ac472253a83f41b16cba0336b7b78fd1e4cc904c039dda43f5d3ed3fa8280bc3'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'ac472253a83f41b16cba0336b7b78fd1e4cc904c039dda43f5d3ed3fa8280bc3'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'ac472253a83f41b16cba0336b7b78fd1e4cc904c039dda43f5d3ed3fa8280bc3'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'ac472253a83f41b16cba0336b7b78fd1e4cc904c039dda43f5d3ed3fa8280bc3'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'ac472253a83f41b16cba0336b7b78fd1e4cc904c039dda43f5d3ed3fa8280bc3'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'ac472253a83f41b16cba0336b7b78fd1e4cc904c039dda43f5d3ed3fa8280bc3'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:0322250462bfbf4eb6d8dcc39606cc55d60cfd7ea2de81369064d9e78cdab5a6'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_rsi_14@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_rsi_14@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_trend_alignment@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_trend_alignment@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_volume_z@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#preferred_volume_z@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:c5e76630fee841c95eb68a0ccd139a52c3e1ef6cef28c62e042b69839386fd7a#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:21d07665cc18b974a8f8e537f16ca30320fb23f62088f84cd5498c7ccd506dc7#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:174005978cf0270009932e625f594aad9f235bc8461c0519fc96ba620910d340#us_10y_yield@2026-09-30T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "878f325d-fc06-5ef8-98ab-e39a1d0346e8/1y/technical",
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
Feedback applied once: {'batch_id': '878f325d-fc06-5ef8-98ab-e39a1d0346e8/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "69b33c3f-1541-5d22-beb5-2b99613cfce3",
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
    "hypothesis_id": "69b33c3f-1541-5d22-beb5-2b99613cfce3",
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
    "hypothesis_id": "69b33c3f-1541-5d22-beb5-2b99613cfce3",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.11677499999999999
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
    "hypothesis_id": "1a739dd1-973a-5ad3-9da1-2c3643335411",
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
    "hypothesis_id": "1a739dd1-973a-5ad3-9da1-2c3643335411",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.014535112568776123
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
