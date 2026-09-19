# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: ef09898d-e70e-56e6-ad29-52ada01db174
Cutoff / prediction: 2026-09-19T22:00:09.667796+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-18T06:30:00+00:00', 'source_refs': ['raw:e5a486bbe29677c0e06ebe45786ad79bbca4eebd13f471f91bfa35228024fb97'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 196100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 42.4667% | 36.2077% | 21.3256% | 6.1033% | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 41.7908% | 36.2620% | 21.9471% | 4.8454% | 45.0000% | 30.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 42.9688% / 35.7851% / 21.2462% | 42.4667% / 36.2077% / 21.3256% | [-0.5020833474284336, 0.42266023337274583, 0.0794231140556989] |
| 1m | 41.2685% / 36.7769% / 21.9546% | 41.7908% / 36.2620% / 21.9471% | [0.5222839815060387, -0.514834961981897, -0.007449019524158329] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 39.50268549888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-19T22:00:08.890212Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e5a486bbe29677c0e06ebe45786ad79bbca4eebd13f471f91bfa35228024fb97",
    "reason": null,
    "released_at": null,
    "rows": 277,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.50268549888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-19T22:00:09.220182Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 39.50268549888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-19T22:00:09.172117Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544",
    "reason": null,
    "released_at": null,
    "rows": 4936,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 26.502685498888887,
    "authority": "official_original",
    "collected_at": "2026-09-19T22:00:09.112125Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-18T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27",
    "reason": null,
    "released_at": null,
    "rows": 180,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-19T22:00:09.439851Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "6346f3acc540a1c13033bb8c3fd3dccd739712598a2890096fcf372330d71e03",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50268549888889,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-19T22:00:09.617709Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "a85857a7ecf1ae7efcc4bab6fb72275afba84492b87e5b490989389d7ed2c225",
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
    "collected_at": "2026-09-19T22:00:09.666798Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "6489c660a9286195f74b7149d2e5294a7b7e2fbf52c410b4fe208296cb65400d",
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
    "collected_at": "2026-09-19T22:00:09.220182Z",
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
    "collected_at": "2026-09-19T22:00:09.220182Z",
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
    "collected_at": "2026-09-19T22:00:09.220182Z",
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
    "collected_at": "2026-09-19T22:00:09.220182Z",
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
Bar boundaries: {'1d': {'count': 4934, 'last': '2026-09-18T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-09-18T06:30:00+00:00'}, '30m': {'count': 277, 'last': '2026-09-18T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a85857a7ecf1ae7efcc4bab6fb72275afba84492b87e5b490989389d7ed2c225'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_rsi_14@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_trend_alignment@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_volume_z@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "ef09898d-e70e-56e6-ad29-52ada01db174/1w/technical",
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
    "atr": 9930.872601836101,
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
      4922,
      4930
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 53.29297186877112,
    "sma": [
      192300.0,
      188770.0,
      182125.0
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
    "volume_ratio": 0.9550670307608872
  },
  "primary": "30m",
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1508.2996873843815,
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
    "bottom_neckline": 200000.0,
    "bottom_pivots": [
      256,
      267
    ],
    "bottom_score": 0.0,
    "rsi": 53.42764645960255,
    "sma": [
      195767.5,
      191830.83333333334,
      194546.66666666666
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
    "top_neckline": 195500.0,
    "top_pivots": [
      264,
      274
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'ef09898d-e70e-56e6-ad29-52ada01db174/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "b78567a6-a62d-5517-b32a-144fb2c1897c",
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
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "b78567a6-a62d-5517-b32a-144fb2c1897c",
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
    "hypothesis_id": "b78567a6-a62d-5517-b32a-144fb2c1897c",
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
    "hypothesis_id": "b78567a6-a62d-5517-b32a-144fb2c1897c",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.04845768034261516
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
    "hypothesis_id": "e80baab1-4c3a-5935-8d2c-a6dc32818ebd",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.3389209934707593, -0.25479797018587713, -0.08412302328489052] | {'down': 0.3474520202981412, 'flat': 0.2491587697671511, 'up': 0.4033892099347076} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3474520202981412, 'flat': 0.2491587697671511, 'up': 0.4033892099347076} | [4.178807942344632, -3.0819498121063713, -1.0968581302382485] | {'down': 0.3166325221770775, 'flat': 0.2381901884647686, 'up': 0.4451772893581539} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3166325221770775, 'flat': 0.2381901884647686, 'up': 0.4451772893581539} | [3.6441959462890585, -2.6034049254529568, -1.0407910208361182] | {'down': 0.2905984729225479, 'flat': 0.22778227825640743, 'up': 0.4816192488210445} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.2905984729225479, 'flat': 0.22778227825640743, 'up': 0.4816192488210445} | [3.653457581446201, -2.5373036860836584, -1.1161538953625287] | {'down': 0.26522543606171134, 'flat': 0.21662073930278214, 'up': 0.5181538246355065} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.26522543606171134, 'flat': 0.21662073930278214, 'up': 0.5181538246355065} | [-7.571332526184777, 8.593001300042607, -1.0216687738578367] | {'down': 0.3511554490621374, 'flat': 0.20640405156420377, 'up': 0.44244049937365876} |
| 5 | E10/causal | ['ef09898d-e70e-56e6-ad29-52ada01db174/1w/technical'] | {'down': 0.3511554490621374, 'flat': 0.20640405156420377, 'up': 0.44244049937365876} | [0.6532959329133947, -0.6205787779878291, -0.032717154925565595] | {'down': 0.3449496612822591, 'flat': 0.20607688001494812, 'up': 0.4489734587027927} |
| 6 | E17/scenario | ['8d4008d0-b8dc-5181-8892-52977ff0ff56', '32d0a113-bc82-529f-bf16-885bf07e9b9d', '9f740663-c8ba-5119-a18e-b3c7fc0c3876', '440ad764-1504-5697-af17-5ed90e36f16b'] | {'down': 0.3449496612822591, 'flat': 0.20607688001494812, 'up': 0.4489734587027927} | [0.3815922248732728, 2.3828440936914994, -2.764436318564756] | {'down': 0.3687781022191741, 'flat': 0.17843251682930056, 'up': 0.45278938095152543} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3687781022191741, 'flat': 0.17843251682930056, 'up': 0.45278938095152543} | [-1.5218141936016838, -0.4515497829947368, 1.973363976596415] | {'down': 0.36426260438922675, 'flat': 0.1981661565952647, 'up': 0.4375712390155086} |
| 8 | E13/history | [] | {'down': 0.36426260438922675, 'flat': 0.1981661565952647, 'up': 0.4375712390155086} | [0.0, 0.0, 0.0] | {'down': 0.36426260438922675, 'flat': 0.1981661565952647, 'up': 0.4375712390155086} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.36426260438922675, 'flat': 0.1981661565952647, 'up': 0.4375712390155086} | [-1.2904413900572231, -0.2185367814081962, 1.5089781714654138] | {'down': 0.3620772365751448, 'flat': 0.21325593830991885, 'up': 0.42466682511493636} |
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.32805
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a85857a7ecf1ae7efcc4bab6fb72275afba84492b87e5b490989389d7ed2c225'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_rsi_14@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_trend_alignment@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_volume_z@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "ef09898d-e70e-56e6-ad29-52ada01db174/1m/technical",
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
      1028,
      1035
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.8119782592470246
  },
  "primary": "1d",
  "reflexivity_effect": 0.015000000000000003,
  "regime_effect": 0.022500000000000003,
  "sell_liquidity": null,
  "wave": {
    "atr": 9930.872601836101,
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
      4922,
      4930
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 53.29297186877112,
    "sma": [
      192300.0,
      188770.0,
      182125.0
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
    "volume_ratio": 0.9550670307608872
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'ef09898d-e70e-56e6-ad29-52ada01db174/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.015000000000000003, 'regime_effect': 0.022500000000000003}
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
    "hypothesis_id": "c1fd4ce9-696f-577e-9c38-ccc57a9cc955",
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
    "hypothesis_id": "c1fd4ce9-696f-577e-9c38-ccc57a9cc955",
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
    "hypothesis_id": "c1fd4ce9-696f-577e-9c38-ccc57a9cc955",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.6348374999999999
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "c1fd4ce9-696f-577e-9c38-ccc57a9cc955",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.09402018034261515
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
    "hypothesis_id": "952a1905-d17d-5944-bdf5-1ea1d875c5cf",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.255652066355494, -0.19226696987287295, -0.06338509648262103] | {'down': 0.34807733030127125, 'flat': 0.2493661490351738, 'up': 0.40255652066355496} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34807733030127125, 'flat': 0.2493661490351738, 'up': 0.40255652066355496} | [1.738066236117236, -1.2959374965994586, -0.4421287395177803] | {'down': 0.33511795533527666, 'flat': 0.244944861639996, 'up': 0.4199371830247273} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.33511795533527666, 'flat': 0.244944861639996, 'up': 0.4199371830247273} | [2.8875243690043795, -2.111638654355569, -0.7758857146488191] | {'down': 0.314001568791721, 'flat': 0.2371860044935078, 'up': 0.4488124267147711} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.314001568791721, 'flat': 0.2371860044935078, 'up': 0.4488124267147711} | [2.9158276504951175, -2.0830034277145804, -0.8328242227805399] | {'down': 0.29317153451457517, 'flat': 0.2288577622657024, 'up': 0.4779707032197223} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.29317153451457517, 'flat': 0.2288577622657024, 'up': 0.4779707032197223} | [-5.641074323682566, 6.611912972949041, -0.97083864926647] | {'down': 0.3592906642440656, 'flat': 0.2191493757730377, 'up': 0.42155995998289664} |
| 5 | E10/causal | ['ef09898d-e70e-56e6-ad29-52ada01db174/1m/technical'] | {'down': 0.3592906642440656, 'flat': 0.2191493757730377, 'up': 0.42155995998289664} | [1.7822115845467335, -1.7037479392279564, -0.0784636453187687] | {'down': 0.342253184851786, 'flat': 0.21836473931985, 'up': 0.43938207582836397} |
| 6 | E17/scenario | ['352cf712-906b-5fbd-934a-841b098aa1cc', '6abb0dd7-d66e-537c-b33e-dd93d2b966b0', 'c487d685-8182-5777-acf2-4af717244071', '09719f84-2c80-5f7d-bc20-9cf060716fdf'] | {'down': 0.342253184851786, 'flat': 0.21836473931985, 'up': 0.43938207582836397} | [0.46491673009532164, 2.7562856017469217, -3.2212023318422545] | {'down': 0.36981604086925524, 'flat': 0.18615271600142747, 'up': 0.4440312431293172} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.36981604086925524, 'flat': 0.18615271600142747, 'up': 0.4440312431293172} | [-1.4152145003201222, -0.4664122096878831, 1.8816267100080053] | {'down': 0.3651519187723764, 'flat': 0.20496898310150752, 'up': 0.42987909812611597} |
| 8 | E13/history | [] | {'down': 0.3651519187723764, 'flat': 0.20496898310150752, 'up': 0.42987909812611597} | [0.0, 0.0, 0.0] | {'down': 0.3651519187723764, 'flat': 0.20496898310150752, 'up': 0.42987909812611597} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3651519187723764, 'flat': 0.20496898310150752, 'up': 0.42987909812611597} | [-1.197100441347576, -0.2531453332629663, 1.4502457746105506] | {'down': 0.36262046543974674, 'flat': 0.21947144084761303, 'up': 0.4179080937126402} |
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
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.26666666666666666, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.1417176
Confidence-lowering Strong Evidence: ['bit_supply', 'cxmt_memory_capacity', 'dram_contract_asp', 'equity_discount_rate', 'fab_capacity', 'gpu_demand_growth', 'hbm_demand', 'hbm_price', 'hyperscaler_capex', 'memory_bit_shipment', 'memory_inventory', 'new_capacity', 'samsung_eps', 'samsung_eps_revision', 'samsung_forward_per', 'samsung_free_cash_flow', 'usdkrw', 'yield_rate']
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '2238010cca391885acebc03b6d55eda9670d6531950a9fc8d96e995a1b9a0238'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '2238010cca391885acebc03b6d55eda9670d6531950a9fc8d96e995a1b9a0238'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '2238010cca391885acebc03b6d55eda9670d6531950a9fc8d96e995a1b9a0238'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '2238010cca391885acebc03b6d55eda9670d6531950a9fc8d96e995a1b9a0238'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '2238010cca391885acebc03b6d55eda9670d6531950a9fc8d96e995a1b9a0238'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '2238010cca391885acebc03b6d55eda9670d6531950a9fc8d96e995a1b9a0238'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '2238010cca391885acebc03b6d55eda9670d6531950a9fc8d96e995a1b9a0238'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a85857a7ecf1ae7efcc4bab6fb72275afba84492b87e5b490989389d7ed2c225'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_rsi_14@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_trend_alignment@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#preferred_volume_z@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:d5f685b8bda92c4fbff65f5be811757ee50c3902ed61cba5800abfdecb530544#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:4c1d2a42e8bfe73402e2aac191c370cecfb0199e16cab04ea853b43ac4942fed#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:d992faa760d752258ea0c35747cdbc1889fe2496935dee05aa6b273516461d27#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "ef09898d-e70e-56e6-ad29-52ada01db174/1y/technical",
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
      1028,
      1035
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
      1030,
      1038
    ],
    "top_score": 0.1,
    "volume_ratio": 0.8119782592470246
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'ef09898d-e70e-56e6-ad29-52ada01db174/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "b7c49043-1ce2-5cf2-afbb-09c98c91e5e4",
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
    "hypothesis_id": "b7c49043-1ce2-5cf2-afbb-09c98c91e5e4",
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
    "hypothesis_id": "b7c49043-1ce2-5cf2-afbb-09c98c91e5e4",
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
    "hypothesis_id": "b7c49043-1ce2-5cf2-afbb-09c98c91e5e4",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.04845768034261516
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
    "hypothesis_id": "afa6c0cf-1d01-5e01-b668-eb9e3740364d",
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
