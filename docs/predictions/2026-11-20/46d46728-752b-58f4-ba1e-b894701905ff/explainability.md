# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 46d46728-752b-58f4-ba1e-b894701905ff
Cutoff / prediction: 2026-11-19T22:00:12.922796+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-11-19T06:30:00+00:00', 'source_refs': ['raw:a79e852c3296598ab1046963630cf4b0aa48fd8c11505d595637f23a1287a7be'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 157500.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 39.0513% | 39.5521% | 21.3966% | 7.5723% | 10.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | — | — | — | — | 0.0000% | 0.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 0.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 38.6081% / 40.0544% / 21.3375% | 39.0513% / 39.5521% / 21.3966% | [0.44316398745447017, -0.5022433978489449, 0.059079410394477505] |
| 1m | insufficient_evidence | insufficient_evidence | None |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503589665555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-19T22:00:12.064674Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-19T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "a79e852c3296598ab1046963630cf4b0aa48fd8c11505d595637f23a1287a7be",
    "reason": null,
    "released_at": null,
    "rows": 275,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503589665555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-19T22:00:12.421333Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-11-19T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503589665555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-19T22:00:12.461335Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-11-19T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 1.5035896655555554,
    "authority": "official_original",
    "collected_at": "2026-11-19T22:00:12.128191Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-11-19T20:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f",
    "reason": null,
    "released_at": null,
    "rows": 222,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-19T22:00:12.596306Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "a9cc6019ed6c9ef1d00381afed2a485055f46c8173caa93ad216a5f02724ea9c",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.50358966555555,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-19T22:00:12.616074Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-11-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "a8144225fb079748947793b2c8cbaf3c5281db7d10674d01e855193c2e1923bb",
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
    "collected_at": "2026-11-19T22:00:12.921796Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "869cb060ebb116ff17d500dc78b42e04402da1ac4637d89a17246accc2985fdd",
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
    "collected_at": "2026-11-19T22:00:12.462332Z",
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
    "collected_at": "2026-11-19T22:00:12.462332Z",
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
    "collected_at": "2026-11-19T22:00:12.462332Z",
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
    "collected_at": "2026-11-19T22:00:12.462332Z",
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
Document statuses: {'dram_spot': 'unavailable: URLError: source unavailable', 'exports_10': 'stale', 'exports_20': 'stale', 'exports_month': 'stale', 'krx_access': 'documentation_only; foreign/institution/program unavailable; no approved data API response', 'samsung_bs': 'available_unmapped', 'samsung_cf': 'available_unmapped', 'samsung_soi': 'available_unmapped'}
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-11-19T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-10-31T14:59:59+00:00'}, '1w': {'count': 1042, 'last': '2026-11-13T06:30:00+00:00'}, '30m': {'count': 275, 'last': '2026-11-19T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.0, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a8144225fb079748947793b2c8cbaf3c5281db7d10674d01e855193c2e1923bb'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-12T20:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "46d46728-752b-58f4-ba1e-b894701905ff/1w/technical",
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
    "atr": 10588.53813063966,
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
    "bottom_neckline": 179000.0,
    "bottom_pivots": [
      4917,
      4922
    ],
    "bottom_score": 0.0,
    "rsi": 42.92057835803883,
    "sma": [
      166240.0,
      182488.33333333334,
      188761.66666666666
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
    "top_neckline": 141900.0,
    "top_pivots": [
      4916,
      4927
    ],
    "top_score": 0.0,
    "volume_ratio": 0.8605697127531453
  },
  "primary": "30m",
  "reflexivity_effect": 0.010000000000000002,
  "regime_effect": 0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 2411.159385843743,
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
    "bottom_neckline": 155700.0,
    "bottom_pivots": [
      265,
      272
    ],
    "bottom_score": 0.1,
    "rsi": 57.482144265196716,
    "sma": [
      153817.5,
      159852.5,
      159556.25
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
    "top_neckline": 150200.0,
    "top_pivots": [
      264,
      270
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '46d46728-752b-58f4-ba1e-b894701905ff/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.010000000000000002, 'regime_effect': 0.015}
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
    "hypothesis_id": "1c724341-3d86-5e88-890c-b1b873235f17",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "1c724341-3d86-5e88-890c-b1b873235f17",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
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
    "hypothesis_id": "5ba848af-7cbe-5050-bce9-6ff7e456f7f3",
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
    "hypothesis_id": "5ba848af-7cbe-5050-bce9-6ff7e456f7f3",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.17291938433295156
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "5ba848af-7cbe-5050-bce9-6ff7e456f7f3",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.14916050607383227
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.9284380467386, 1.1633075768952006, -0.23486953015660894] | {'down': 0.361633075768952, 'flat': 0.2476513046984339, 'up': 0.390715619532614} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.361633075768952, 'flat': 0.2476513046984339, 'up': 0.390715619532614} | [-0.8027212378429016, 1.0158517258703537, -0.2131304880274576] | {'down': 0.3717915930276555, 'flat': 0.24551999981815933, 'up': 0.382688407154185} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3717915930276555, 'flat': 0.24551999981815933, 'up': 0.382688407154185} | [4.751712460679963, -3.61419324654505, -1.137519214134905] | {'down': 0.335649660562205, 'flat': 0.23414480767681028, 'up': 0.43020553176098464} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.335649660562205, 'flat': 0.23414480767681028, 'up': 0.43020553176098464} | [4.865706550532167, -3.5611080461662836, -1.304598504365867] | {'down': 0.3000385801005422, 'flat': 0.22109882263315161, 'up': 0.4788625972663063} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3000385801005422, 'flat': 0.22109882263315161, 'up': 0.4788625972663063} | [-7.673151792262556, 9.064206713129453, -1.391054920866905] | {'down': 0.3906806472318367, 'flat': 0.20718827342448257, 'up': 0.40213107934368075} |
| 5 | E10/causal | ['46d46728-752b-58f4-ba1e-b894701905ff/1w/technical'] | {'down': 0.3906806472318367, 'flat': 0.20718827342448257, 'up': 0.40213107934368075} | [-0.12932809136376178, 0.12864299600968132, 0.0006850953540804561] | {'down': 0.3919670771919335, 'flat': 0.20719512437802337, 'up': 0.40083779843004314} |
| 6 | E17/scenario | ['3af60b4d-14ab-5e6a-9a8d-5f2f8d2c3a62', 'f3f392f4-5338-5752-8d66-0e5094876dc3', 'ab5052d2-c410-5faf-8d97-6a5810d892f8', 'bea3f190-f076-5af0-8e06-73b18a088c19'] | {'down': 0.3919670771919335, 'flat': 0.20719512437802337, 'up': 0.40083779843004314} | [0.5633932269917707, 2.1189095735592134, -2.6823028005509815] | {'down': 0.41315617292752566, 'flat': 0.18037209637251356, 'up': 0.40647173069996084} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.41315617292752566, 'flat': 0.18037209637251356, 'up': 0.40647173069996084} | [-0.8919558590100352, -0.9734756574163839, 1.8654315164264106] | {'down': 0.4034214163533618, 'flat': 0.19902641153677766, 'up': 0.3975521721098605} |
| 8 | E13/history | [] | {'down': 0.4034214163533618, 'flat': 0.19902641153677766, 'up': 0.3975521721098605} | [0.0, 0.0, 0.0] | {'down': 0.4034214163533618, 'flat': 0.19902641153677766, 'up': 0.3975521721098605} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4034214163533618, 'flat': 0.19902641153677766, 'up': 0.3975521721098605} | [-0.7039530117293025, -0.7900256062780553, 1.4939786180073606] | {'down': 0.39552116029058126, 'flat': 0.21396619771685127, 'up': 0.39051264199256747} |
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
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
Eligibility: False; reasons: ['coverage:memory']
Coverage: {'ai_demand': 0.0, 'earnings': 1.0, 'flow': 0.0, 'macro': 0.5, 'memory': 0.0, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.0
Confidence-lowering Strong Evidence: ['dram_contract_asp', 'foreign_net_buy', 'hbm_demand', 'hbm_price', 'institution_net_buy', 'samsung_eps', 'samsung_eps_revision', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a8144225fb079748947793b2c8cbaf3c5281db7d10674d01e855193c2e1923bb'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-12T20:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "46d46728-752b-58f4-ba1e-b894701905ff/1m/technical",
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
    "atr": 25710.46356221683,
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
      1026,
      1037
    ],
    "bottom_score": 0.0,
    "rsi": 48.050660675144414,
    "sma": [
      186395.0,
      145438.33333333334,
      97925.41666666667
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
    "top_neckline": 154400.0,
    "top_pivots": [
      1034,
      1039
    ],
    "top_score": 0.0,
    "volume_ratio": 1.018493887929581
  },
  "primary": "1d",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 10588.53813063966,
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
    "bottom_neckline": 179000.0,
    "bottom_pivots": [
      4917,
      4922
    ],
    "bottom_score": 0.0,
    "rsi": 42.92057835803883,
    "sma": [
      166240.0,
      182488.33333333334,
      188761.66666666666
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
    "top_neckline": 141900.0,
    "top_pivots": [
      4916,
      4927
    ],
    "top_score": 0.0,
    "volume_ratio": 0.8605697127531453
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '46d46728-752b-58f4-ba1e-b894701905ff/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "52210557-cf19-504a-adb7-276280cfee39",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "52210557-cf19-504a-adb7-276280cfee39",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
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
    "hypothesis_id": "99c09bfb-a74d-5c3e-abf1-cca2292e745a",
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
    "hypothesis_id": "99c09bfb-a74d-5c3e-abf1-cca2292e745a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.19114438433295158
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "99c09bfb-a74d-5c3e-abf1-cca2292e745a",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.1673855060738323
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
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
  "missing_coverage": [
    "coverage:memory"
  ],
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:a8144225fb079748947793b2c8cbaf3c5281db7d10674d01e855193c2e1923bb'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:0837e3e7358135a50498b692c9e67694e96609138ff6b0b6f5e3886a42b09a61#samsung_common_price@2026-11-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-10-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:02af86863eb04fb05cb785659712d6d265befeb04329ac9a28b41168addc89ea#samsung_preferred_price@2026-11-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-10-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:92dd0f21c709175f0d35722667976a62b8aa9e429c187df5ad2a93ee1b2e214f#us_10y_yield@2026-11-12T20:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "46d46728-752b-58f4-ba1e-b894701905ff/1y/technical",
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
    "atr": 30149.60386604615,
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
      218,
      235
    ],
    "bottom_score": 0.0,
    "rsi": 64.65633306538288,
    "sma": [
      115682.5,
      76521.66666666667,
      61062.666666666664
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
      219,
      234
    ],
    "top_score": 0.1,
    "volume_ratio": 1.1963416147691088
  },
  "primary": "1w",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 25710.46356221683,
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
      1026,
      1037
    ],
    "bottom_score": 0.0,
    "rsi": 48.050660675144414,
    "sma": [
      186395.0,
      145438.33333333334,
      97925.41666666667
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
    "top_neckline": 154400.0,
    "top_pivots": [
      1034,
      1039
    ],
    "top_score": 0.0,
    "volume_ratio": 1.018493887929581
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '46d46728-752b-58f4-ba1e-b894701905ff/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "4de60a4a-0d10-54d0-9510-bc76748585da",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "4de60a4a-0d10-54d0-9510-bc76748585da",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
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
    "hypothesis_id": "b0ae5d82-9fee-5939-a744-8cf3eead899a",
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
    "hypothesis_id": "b0ae5d82-9fee-5939-a744-8cf3eead899a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.19114438433295158
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "b0ae5d82-9fee-5939-a744-8cf3eead899a",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.1673855060738323
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
        "preferred_volume_z"
      ],
      "factor_id": "preferred_volume_z",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 0.0,
      "unit": "z_score"
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
