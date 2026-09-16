# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 86198141-7f4a-581a-96b9-cc6083c662f6
Cutoff / prediction: 2026-09-16T22:00:13.066111+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-16T06:30:00+00:00', 'source_refs': ['raw:f0ae28b094a25b8739bc48ed2b70848db81206fe0ec1357cefcb50ea380e3a57'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 194600.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 37.5133% | 40.6718% | 21.8149% | 5.3495% | 0.0000% | 35.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 39.9889% | 37.8129% | 22.1981% | 4.2193% | 45.0000% | 30.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 39.1109% / 38.9995% / 21.8896% | 37.5133% / 40.6718% / 21.8149% | [-1.5976345152203364, 1.6723337551544648, -0.07469923993413397] |
| 1m | 39.4321% / 38.3107% / 22.2571% | 39.9889% / 37.8129% / 22.1981% | [0.5567901833274769, -0.4977770450889263, -0.05901313823855059] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503629475277778,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-16T22:00:11.983156Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f0ae28b094a25b8739bc48ed2b70848db81206fe0ec1357cefcb50ea380e3a57",
    "reason": null,
    "released_at": null,
    "rows": 265,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503629475277778,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-16T22:00:12.514308Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503629475277778,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-16T22:00:12.466134Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.5036294752777777,
    "authority": "official_original",
    "collected_at": "2026-09-16T22:00:11.934996Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-16T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e",
    "reason": null,
    "released_at": null,
    "rows": 178,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-16T22:00:12.514308Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "3cacec590c71c2bd81d60fdacd0be1daca06f2d3e60076e2dc5f620127d47db4",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503629475277776,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-16T22:00:12.498292Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "74390551fc407eb773abaa164bcb50bbb4b38a7056c453bba5028cbe5c9e693b",
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
    "collected_at": "2026-09-16T22:00:13.066111Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "8d63e3879e63d502ac6fcc6df7be3f974064c9cac410f55f514cc945a4f656be",
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
    "collected_at": "2026-09-16T22:00:12.498292Z",
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
    "collected_at": "2026-09-16T22:00:12.498292Z",
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
    "collected_at": "2026-09-16T22:00:12.498292Z",
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
    "collected_at": "2026-09-16T22:00:12.498292Z",
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
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-16T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-11T06:30:00+00:00'}, '30m': {'count': 265, 'last': '2026-09-16T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:74390551fc407eb773abaa164bcb50bbb4b38a7056c453bba5028cbe5c9e693b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_rsi_14@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_trend_alignment@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_volume_z@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "86198141-7f4a-581a-96b9-cc6083c662f6/1w/technical",
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
    "atr": 10562.432129940094,
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
      4915,
      4922
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 52.47504458486897,
    "sma": [
      192740.0,
      189213.33333333334,
      181045.83333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4917,
      4927
    ],
    "top_score": 0.30000000000000004,
    "volume_ratio": 0.9148982220371553
  },
  "primary": "30m",
  "reflexivity_effect": -0.034999999999999996,
  "regime_effect": -0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 1830.7304406345115,
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
    "bottom_neckline": 195900.0,
    "bottom_pivots": [
      240,
      256
    ],
    "bottom_score": 0.0,
    "rsi": 60.34958310705354,
    "sma": [
      191895.0,
      191777.5,
      192966.25
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 190100.0,
    "top_pivots": [
      253,
      260
    ],
    "top_score": 0.35,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '86198141-7f4a-581a-96b9-cc6083c662f6/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "eec7cf84-b7b0-5d61-bbd8-c1487660ba18",
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
    "hypothesis_id": "eec7cf84-b7b0-5d61-bbd8-c1487660ba18",
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
    "hypothesis_id": "a2c32a95-e09d-51ef-b4cf-3cd84f22137c",
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
    "hypothesis_id": "a2c32a95-e09d-51ef-b4cf-3cd84f22137c",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.0774553471564034
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.4155332524356625, 0.5191020303021543, -0.10356877786649454] | {'down': 0.3551910203030215, 'flat': 0.24896431222133505, 'up': 0.3958446674756434} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.3551910203030215, 'flat': 0.24896431222133505, 'up': 0.3958446674756434} | [3.5717789070860375, -2.668161532614388, -0.9036173744716353] | {'down': 0.32850940497687764, 'flat': 0.2399281384766187, 'up': 0.43156245654650377} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.32850940497687764, 'flat': 0.2399281384766187, 'up': 0.43156245654650377} | [3.6341395526354017, -2.635582526940139, -0.9985570256952792] | {'down': 0.30215357970747625, 'flat': 0.2299425682196659, 'up': 0.4679038520728578} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.30215357970747625, 'flat': 0.2299425682196659, 'up': 0.4679038520728578} | [-7.569660680164903, 9.055899674429247, -1.4862389942643301] | {'down': 0.3927125764517687, 'flat': 0.2150801782770226, 'up': 0.39220724527120876} |
| 4 | E10/causal | ['86198141-7f4a-581a-96b9-cc6083c662f6/1w/technical'] | {'down': 0.3927125764517687, 'flat': 0.2150801782770226, 'up': 0.39220724527120876} | [-1.4918268587904626, 1.504545388966605, -0.012718530176145104] | {'down': 0.40775803034143476, 'flat': 0.21495299297526116, 'up': 0.37728897668330413} |
| 5 | E17/scenario | ['0567d067-9dca-523b-a37c-e9d905370c81', '5e1b0e87-816e-5f31-acad-58d2dc99b445', '8b66ccaa-931e-5472-943c-553ff966f608', '36108fe7-11a0-5c4a-90e1-4899900ab1ef'] | {'down': 0.40775803034143476, 'flat': 0.21495299297526116, 'up': 0.37728897668330413} | [0.9371023029004222, 2.143364553201599, -3.080466856102029] | {'down': 0.42919167587345075, 'flat': 0.18414832441424087, 'up': 0.38665999971230836} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.42919167587345075, 'flat': 0.18414832441424087, 'up': 0.38665999971230836} | [-0.6942443122279318, -1.2479517961076103, 1.9421961083355421] | {'down': 0.41671215791237465, 'flat': 0.2035702854975963, 'up': 0.37971755659002904} |
| 7 | E13/history | [] | {'down': 0.41671215791237465, 'flat': 0.2035702854975963, 'up': 0.37971755659002904} | [0.0, 0.0, 0.0] | {'down': 0.41671215791237465, 'flat': 0.2035702854975963, 'up': 0.37971755659002904} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.41671215791237465, 'flat': 0.2035702854975963, 'up': 0.37971755659002904} | [-0.45850001184365996, -0.9993700339924139, 1.4578700458360823] | {'down': 0.4067184575724505, 'flat': 0.2181489859559571, 'up': 0.37513255647159244} |
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
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1w",
      "operator": "lt",
      "threshold": 50.0,
      "unit": "rsi"
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:74390551fc407eb773abaa164bcb50bbb4b38a7056c453bba5028cbe5c9e693b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_rsi_14@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_trend_alignment@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_volume_z@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "86198141-7f4a-581a-96b9-cc6083c662f6/1m/technical",
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
  "reflexivity_effect": 0.015000000000000003,
  "regime_effect": 0.022500000000000003,
  "sell_liquidity": null,
  "wave": {
    "atr": 10562.432129940094,
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
      4915,
      4922
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 52.47504458486897,
    "sma": [
      192740.0,
      189213.33333333334,
      181045.83333333334
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4917,
      4927
    ],
    "top_score": 0.30000000000000004,
    "volume_ratio": 0.9148982220371553
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '86198141-7f4a-581a-96b9-cc6083c662f6/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.015000000000000003, 'regime_effect': 0.022500000000000003}
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
    "hypothesis_id": "0fb14a71-ee50-54a6-a0a5-63010dedf4e3",
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
    "hypothesis_id": "0fb14a71-ee50-54a6-a0a5-63010dedf4e3",
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
    "hypothesis_id": "0fb14a71-ee50-54a6-a0a5-63010dedf4e3",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.10479465284359663
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
    "hypothesis_id": "5e326416-23f3-5a5f-88e9-89d692fb2239",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.28497998131521984, -0.214296016982235, -0.0706839643329904] | {'down': 0.34785703983017763, 'flat': 0.2492931603566701, 'up': 0.4028497998131522} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.34785703983017763, 'flat': 0.2492931603566701, 'up': 0.4028497998131522} | [2.86130135815878, -2.1228150974588855, -0.7384862606998804] | {'down': 0.3266288888555888, 'flat': 0.2419082977496713, 'up': 0.43146281339474} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3266288888555888, 'flat': 0.2419082977496713, 'up': 0.43146281339474} | [2.901221928001113, -2.101654784879059, -0.7995671431220597] | {'down': 0.3056123410067982, 'flat': 0.2339126263184507, 'up': 0.46047503267475115} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.3056123410067982, 'flat': 0.2339126263184507, 'up': 0.46047503267475115} | [-5.622813975729946, 6.718906913526496, -1.09609293779655] | {'down': 0.37280141014206314, 'flat': 0.2229516969404852, 'up': 0.4042468929174517} |
| 4 | E10/causal | ['86198141-7f4a-581a-96b9-cc6083c662f6/1m/technical'] | {'down': 0.37280141014206314, 'flat': 0.2229516969404852, 'up': 0.4042468929174517} | [0.7573118572682669, -0.7405530618604161, -0.01675879540785352] | {'down': 0.365395879523459, 'flat': 0.22278410898640666, 'up': 0.41182001149013436} |
| 5 | E17/scenario | ['505678de-450e-5a1c-a548-d423bee4b909', '30a759fe-d2c2-56a7-b2bf-689c6dc60348', '540b6b25-acb8-5dc1-b869-ca71dd833f3f', 'ddb8fb56-5d2c-5f7b-9cc9-d4031c79bc85'] | {'down': 0.365395879523459, 'flat': 0.22278410898640666, 'up': 0.41182001149013436} | [0.8385646484107834, 2.5500196488155047, -3.388584297226291] | {'down': 0.390896076011614, 'flat': 0.18889826601414375, 'up': 0.4202056579742422} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.390896076011614, 'flat': 0.18889826601414375, 'up': 0.4202056579742422} | [-1.1354859675002105, -0.7523879075665207, 1.887873875066734] | {'down': 0.3833721969359488, 'flat': 0.2077770047648111, 'up': 0.4088507982992401} |
| 7 | E13/history | [] | {'down': 0.3833721969359488, 'flat': 0.2077770047648111, 'up': 0.4088507982992401} | [0.0, 0.0, 0.0] | {'down': 0.3833721969359488, 'flat': 0.2077770047648111, 'up': 0.4088507982992401} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.3833721969359488, 'flat': 0.2077770047648111, 'up': 0.4088507982992401} | [-0.8961416111251563, -0.5242717414835452, 1.4204133526086986] | {'down': 0.37812947952111337, 'flat': 0.22198113829089808, 'up': 0.39988938218798853} |
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
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1m",
      "operator": "lt",
      "threshold": 50.0,
      "unit": "rsi"
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '6a80759bbbd580fdaee00e81bf8def03213a0676f416cfb9414ba64387b0736e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '6a80759bbbd580fdaee00e81bf8def03213a0676f416cfb9414ba64387b0736e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '6a80759bbbd580fdaee00e81bf8def03213a0676f416cfb9414ba64387b0736e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '6a80759bbbd580fdaee00e81bf8def03213a0676f416cfb9414ba64387b0736e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '6a80759bbbd580fdaee00e81bf8def03213a0676f416cfb9414ba64387b0736e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '6a80759bbbd580fdaee00e81bf8def03213a0676f416cfb9414ba64387b0736e'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '6a80759bbbd580fdaee00e81bf8def03213a0676f416cfb9414ba64387b0736e'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:74390551fc407eb773abaa164bcb50bbb4b38a7056c453bba5028cbe5c9e693b'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_rsi_14@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_trend_alignment@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#preferred_volume_z@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1e7666c4a8cb2601329a02aeadbaf91adf22c195e1e46c950f2a7b0b2f6b462a#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:7239c1ced8fee0a52a3ea950190a88518000c8d54606948bacb07f698db503ee#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:f9fa77ee65913b609b2f54011fe34785aa3ce8510280679d5f17233084d9c07e#us_10y_yield@2026-09-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "86198141-7f4a-581a-96b9-cc6083c662f6/1y/technical",
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
Feedback applied once: {'batch_id': '86198141-7f4a-581a-96b9-cc6083c662f6/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "4bbd8fad-a107-5c37-a46e-fd0e66afbfe8",
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
    "hypothesis_id": "4bbd8fad-a107-5c37-a46e-fd0e66afbfe8",
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
    "hypothesis_id": "4bbd8fad-a107-5c37-a46e-fd0e66afbfe8",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.013669652843596607
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
    "hypothesis_id": "ddb55797-f9d8-558e-a767-8ea35654be5d",
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
        "preferred_rsi_14"
      ],
      "factor_id": "preferred_rsi_14",
      "horizon": "1y",
      "operator": "lt",
      "threshold": 50.0,
      "unit": "rsi"
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
