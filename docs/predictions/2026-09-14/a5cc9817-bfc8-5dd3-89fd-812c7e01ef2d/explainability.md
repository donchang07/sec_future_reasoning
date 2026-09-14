# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d
Cutoff / prediction: 2026-09-14T00:15:08.538723+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-11T06:30:00+00:00', 'source_refs': ['raw:469cea24aec103f379053b6f9676f5ded126b6853e0f1a861dbba62738478afb'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 193300.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 40.3917% | 37.7183% | 21.8900% | 4.5981% | 10.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 40.2970% | 37.3833% | 22.3197% | 3.8089% | 45.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 39.9169% / 38.1564% / 21.9267% | 40.3917% / 37.7183% / 21.8900% | [0.4747881289902889, -0.4381005179523001, -0.036687611037977685] |
| 1m | 39.3971% / 38.2177% / 22.3852% | 40.2970% / 37.3833% / 22.3197% | [0.8999145285459309, -0.8344126300495858, -0.06550189849635069] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 65.7523718675,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T00:15:07.493184Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "469cea24aec103f379053b6f9676f5ded126b6853e0f1a861dbba62738478afb",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 65.7523718675,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T00:15:07.944695Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0",
    "reason": null,
    "released_at": null,
    "rows": 4931,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 65.7523718675,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T00:15:08.008696Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 52.7523718675,
    "authority": "official_original",
    "collected_at": "2026-09-14T00:15:07.430184Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-11T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82",
    "reason": null,
    "released_at": null,
    "rows": 175,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T00:15:08.010696Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "181f65be4584c36801e18a3ce06a074d39ff5fb2341de879622271c61fb256b6",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 65.7523718675,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-14T00:15:08.088696Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-11T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b63904aef988a4875e95c487681cfb48c32c5b56a6be72e321b1b5745c2d53de",
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
    "collected_at": "2026-09-14T00:15:08.537723Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "d29ad30b78616a78119a87a7c51966c43b111efe9c913d12e0b19fd03187cf24",
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
    "collected_at": "2026-09-14T00:15:08.008696Z",
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
    "collected_at": "2026-09-14T00:15:08.008696Z",
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
    "collected_at": "2026-09-14T00:15:08.008696Z",
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
    "collected_at": "2026-09-14T00:15:08.008696Z",
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
Bar boundaries: {'1d': {'count': 4931, 'last': '2026-09-11T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-09-11T06:30:00+00:00'}, '30m': {'count': 241, 'last': '2026-09-11T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b63904aef988a4875e95c487681cfb48c32c5b56a6be72e321b1b5745c2d53de'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_rsi_14@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_rsi_14@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_trend_alignment@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_trend_alignment@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_volume_z@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_volume_z@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1w/technical",
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
    "atr": 10868.827384868286,
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
      4917,
      4924
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 51.51471624545329,
    "sma": [
      192365.0,
      191036.66666666666,
      179705.0
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
      4912,
      4919
    ],
    "top_score": 0.2,
    "volume_ratio": 0.719964281862356
  },
  "primary": "30m",
  "reflexivity_effect": 0.010000000000000002,
  "regime_effect": 0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1413.391930190856,
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
    "bottom_neckline": 193300.0,
    "bottom_pivots": [
      230,
      235
    ],
    "bottom_score": 0.1,
    "rsi": 41.95290389913051,
    "sma": [
      195142.5,
      197382.5,
      192065.83333333334
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
    "top_neckline": 191000.0,
    "top_pivots": [
      227,
      237
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.010000000000000002, 'regime_effect': 0.015}
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
    "hypothesis_id": "35e6a890-7336-5a89-81a6-b6ce4ffd11a1",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.423225
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "35e6a890-7336-5a89-81a6-b6ce4ffd11a1",
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
    "hypothesis_id": "35e6a890-7336-5a89-81a6-b6ce4ffd11a1",
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
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "35e6a890-7336-5a89-81a6-b6ce4ffd11a1",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.038673669313619465
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
    "hypothesis_id": "8659f13d-5cc3-5140-9391-af0f2df9759c",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.2704218360235988, -0.2033616764274493, -0.06706015959614398] | {'down': 0.3479663832357255, 'flat': 0.24932939840403856, 'up': 0.402704218360236} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3479663832357255, 'flat': 0.24932939840403856, 'up': 0.402704218360236} | [2.9908787983713383, -2.2180192909611818, -0.7728595074101619] | {'down': 0.32578619032611367, 'flat': 0.24160080332993694, 'up': 0.4326130063439494} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.32578619032611367, 'flat': 0.24160080332993694, 'up': 0.4326130063439494} | [2.416780203866231, -1.7524944557632705, -0.6642857481029607] | {'down': 0.30826124576848096, 'flat': 0.23495794584890733, 'up': 0.4567808083826117} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.30826124576848096, 'flat': 0.23495794584890733, 'up': 0.4567808083826117} | [2.4326952240758204, -1.7302494388480194, -0.7024457852277982] | {'down': 0.29095875138000077, 'flat': 0.22793348799662935, 'up': 0.4811077606233699} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.29095875138000077, 'flat': 0.22793348799662935, 'up': 0.4811077606233699} | [-7.2574313134709465, 8.547211910841785, -1.2897805973708487] | {'down': 0.3764308704884186, 'flat': 0.21503568202292087, 'up': 0.40853344748866044} |
| 5 | E10/causal | ['a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1w/technical'] | {'down': 0.3764308704884186, 'flat': 0.21503568202292087, 'up': 0.40853344748866044} | [1.1494439246025001, -1.1223480346447656, -0.027095889957717834] | {'down': 0.36520739014197096, 'flat': 0.2147647231233437, 'up': 0.42002788673468544} |
| 6 | E17/scenario | ['13849654-8712-5479-af87-9a009d91fc7c', '2abbf554-6ad1-5e87-bd71-cf7d5915acb4', 'f0e7a949-27ed-52c6-b563-e86f7be193ce', '3b1e29db-23f4-5819-980e-2d85e45804ea'] | {'down': 0.36520739014197096, 'flat': 0.2147647231233437, 'up': 0.42002788673468544} | [0.571623035349883, 2.442472090719716, -3.0140951260696047] | {'down': 0.3896321110491681, 'flat': 0.18462377186264764, 'up': 0.42574411708818427} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3896321110491681, 'flat': 0.18462377186264764, 'up': 0.42574411708818427} | [-1.2287864077222377, -0.7486049789612592, 1.9773913866834913] | {'down': 0.3821460612595555, 'flat': 0.20439768572948255, 'up': 0.4134562530109619} |
| 8 | E13/history | [] | {'down': 0.3821460612595555, 'flat': 0.20439768572948255, 'up': 0.4134562530109619} | [0.0, 0.0, 0.0] | {'down': 0.3821460612595555, 'flat': 0.20439768572948255, 'up': 0.4134562530109619} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3821460612595555, 'flat': 0.20439768572948255, 'up': 0.4134562530109619} | [-0.9539464961681288, -0.4962618667212704, 1.4502083628894102] | {'down': 0.3771834425923428, 'flat': 0.21889976935837666, 'up': 0.4039167880492806} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b63904aef988a4875e95c487681cfb48c32c5b56a6be72e321b1b5745c2d53de'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_rsi_14@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_rsi_14@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_trend_alignment@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_trend_alignment@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_volume_z@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_volume_z@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1m/technical",
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
  "reflexivity_effect": 0.02500000000000001,
  "regime_effect": 0.037500000000000006,
  "sell_liquidity": null,
  "wave": {
    "atr": 10868.827384868286,
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
      4917,
      4924
    ],
    "bottom_score": 0.45000000000000007,
    "rsi": 51.51471624545329,
    "sma": [
      192365.0,
      191036.66666666666,
      179705.0
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
      4912,
      4919
    ],
    "top_score": 0.2,
    "volume_ratio": 0.719964281862356
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.02500000000000001, 'regime_effect': 0.037500000000000006}
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
    "hypothesis_id": "10e63c1b-80a4-51cc-8e06-494ef612cc4c",
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
    "hypothesis_id": "10e63c1b-80a4-51cc-8e06-494ef612cc4c",
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
    "hypothesis_id": "10e63c1b-80a4-51cc-8e06-494ef612cc4c",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.45056250000000003
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "10e63c1b-80a4-51cc-8e06-494ef612cc4c",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.06601116931361947
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
    "hypothesis_id": "8eecb14d-4dc7-55cf-abd3-c5fd412f6f5b",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.1794415386080883, -0.1349966613072795, -0.044444877300797714] | {'down': 0.3486500333869272, 'flat': 0.24955555122699202, 'up': 0.4017944153860809} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3486500333869272, 'flat': 0.24955555122699202, 'up': 0.4017944153860809} | [1.230906914534946, -0.9203845818011314, -0.31052233273382024] | {'down': 0.33944618756891587, 'flat': 0.24645032789965382, 'up': 0.41410348453143037} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.33944618756891587, 'flat': 0.24645032789965382, 'up': 0.41410348453143037} | [1.915032346309753, -1.412913857028597, -0.5021184892811642] | {'down': 0.3253170489986299, 'flat': 0.24142914300684218, 'up': 0.4332538079945279} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3253170489986299, 'flat': 0.24142914300684218, 'up': 0.4332538079945279} | [1.9322662887288566, -1.4031619958206343, -0.5291042929082168] | {'down': 0.31128542904042356, 'flat': 0.23613810007776, 'up': 0.45257647088181646} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.31128542904042356, 'flat': 0.23613810007776, 'up': 0.45257647088181646} | [-5.382993248470425, 6.4824812944037635, -1.0994880459333334] | {'down': 0.3761102419844612, 'flat': 0.22514321961842668, 'up': 0.3987465383971122} |
| 5 | E10/causal | ['a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1m/technical'] | {'down': 0.3761102419844612, 'flat': 0.22514321961842668, 'up': 0.3987465383971122} | [1.8096292192108898, -1.767456598202083, -0.042172621008809696] | {'down': 0.35843567600244036, 'flat': 0.22472149340833858, 'up': 0.4168428305892211} |
| 6 | E17/scenario | ['f57118bd-be1d-5a9b-bac8-bb3ad5cf80bd', 'e21a9abf-f033-5105-b646-c237bc15d1aa', '6c5da427-90b3-5d3f-8567-b288d3a40572', '7f2eadc3-92e3-5652-91cb-62381e8ee1c0'] | {'down': 0.35843567600244036, 'flat': 0.22472149340833858, 'up': 0.4168428305892211} | [0.7762599444789797, 2.6846442437072957, -3.4609041881862868] | {'down': 0.3852821184395133, 'flat': 0.1901124515264757, 'up': 0.4246054300340109} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3852821184395133, 'flat': 0.1901124515264757, 'up': 0.4246054300340109} | [-1.2101197268695019, -0.6887564975093463, 1.8988762243788537] | {'down': 0.37839455346441986, 'flat': 0.20910121377026425, 'up': 0.4125042327653159} |
| 8 | E13/history | [] | {'down': 0.37839455346441986, 'flat': 0.20910121377026425, 'up': 0.4125042327653159} | [0.0, 0.0, 0.0] | {'down': 0.37839455346441986, 'flat': 0.20910121377026425, 'up': 0.4125042327653159} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.37839455346441986, 'flat': 0.20910121377026425, 'up': 0.4125042327653159} | [-0.9534505709755559, -0.45612014057522243, 1.4095707115507756] | {'down': 0.37383335205866763, 'flat': 0.223196920885772, 'up': 0.40296972705556033} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '694a9cd7b337c18850a04cb919f563119c4abe787d5be2fc6e4af6d1c2b69c1d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '694a9cd7b337c18850a04cb919f563119c4abe787d5be2fc6e4af6d1c2b69c1d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '694a9cd7b337c18850a04cb919f563119c4abe787d5be2fc6e4af6d1c2b69c1d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '694a9cd7b337c18850a04cb919f563119c4abe787d5be2fc6e4af6d1c2b69c1d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '694a9cd7b337c18850a04cb919f563119c4abe787d5be2fc6e4af6d1c2b69c1d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '694a9cd7b337c18850a04cb919f563119c4abe787d5be2fc6e4af6d1c2b69c1d'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '694a9cd7b337c18850a04cb919f563119c4abe787d5be2fc6e4af6d1c2b69c1d'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b63904aef988a4875e95c487681cfb48c32c5b56a6be72e321b1b5745c2d53de'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_rsi_14@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_rsi_14@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_trend_alignment@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_trend_alignment@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_volume_z@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#preferred_volume_z@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:1c55fbef9589c56b66e28780830cc644fe4fdfc5d743ad2da99c1768d97b90d5#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:add1aebf281f6f7dcd9750a8b968d767c745f2208991731246ff9f8789316dc0#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:8aa5980ea89e0c8954a079f94acf3e07a885484912486b6d1ce6f6af66c87f82#us_10y_yield@2026-09-04T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1y/technical",
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
Feedback applied once: {'batch_id': 'a5cc9817-bfc8-5dd3-89fd-812c7e01ef2d/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "ed02633a-d6f7-581e-be08-5689dbf8344e",
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
    "hypothesis_id": "ed02633a-d6f7-581e-be08-5689dbf8344e",
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
    "hypothesis_id": "ed02633a-d6f7-581e-be08-5689dbf8344e",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.386775
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "ed02633a-d6f7-581e-be08-5689dbf8344e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.002223669313619461
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
    "hypothesis_id": "3979cc62-029e-50e4-a940-d1552e950a3f",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7776000000000001
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
