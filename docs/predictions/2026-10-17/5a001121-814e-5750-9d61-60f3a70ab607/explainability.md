# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 5a001121-814e-5750-9d61-60f3a70ab607
Cutoff / prediction: 2026-10-16T22:00:11.486826+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-16T06:30:00+00:00', 'source_refs': ['raw:e7c427d9bb9661f265714246cc0946ca365b393ee5b159c738dcc934490913f1'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 167200.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 38.9645% | 39.6936% | 21.3419% | 7.5456% | 10.0000% | 10.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 38.6149% | 39.4989% | 21.8862% | 3.8050% | 0.0000% | 35.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 20.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 38.9645% / 39.6936% / 21.3419% | 38.9645% / 39.6936% / 21.3419% | [0.0, 0.0, 0.0] |
| 1m | 39.8413% / 38.2681% / 21.8906% | 38.6149% / 39.4989% / 21.8862% | [-1.226385964921911, 1.2307564601476084, -0.004370495225694548] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503190785,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-16T22:00:10.334407Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "e7c427d9bb9661f265714246cc0946ca365b393ee5b159c738dcc934490913f1",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503190785,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-16T22:00:10.964620Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503190785,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-16T22:00:11.005098Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-16T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.503190785,
    "authority": "official_original",
    "collected_at": "2026-10-16T22:00:10.452413Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-16T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927",
    "reason": null,
    "released_at": null,
    "rows": 199,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-16T22:00:10.847417Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "cfb31eef1029e5a9fd4ccfa8388c65e47e8ef504c9e6649a78bd696a62ccf14e",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503190785,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-16T22:00:10.924420Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-15T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b4cbddba8b828240130b5d972aeebdda49ce919951c28051975c6507ea57b211",
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
    "collected_at": "2026-10-16T22:00:11.486826Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f42eb1ef85b2e6f703fd9d48a3ee26ab42fa4d8d1ec1f8dcad0ae472f2008c24",
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
    "collected_at": "2026-10-16T22:00:10.924420Z",
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
    "collected_at": "2026-10-16T22:00:10.924420Z",
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
    "collected_at": "2026-10-16T22:00:10.924420Z",
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
    "collected_at": "2026-10-16T22:00:10.924420Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-16T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-10-16T06:30:00+00:00'}, '30m': {'count': 217, 'last': '2026-10-16T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b4cbddba8b828240130b5d972aeebdda49ce919951c28051975c6507ea57b211'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "5a001121-814e-5750-9d61-60f3a70ab607/1w/technical",
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
    "atr": 10635.428026631338,
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
    "rsi": 37.3559943028347,
    "sma": [
      193675.0,
      187461.66666666666,
      190230.83333333334
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
    "volume_ratio": 1.050487717885096
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 2717.7238324213176,
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
    "bottom_neckline": 168000.0,
    "bottom_pivots": [
      203,
      211
    ],
    "bottom_score": 0.1,
    "rsi": 50.518477044209696,
    "sma": [
      163565.0,
      172988.33333333334,
      186084.16666666666
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
    "top_neckline": 164900.0,
    "top_pivots": [
      206,
      213
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '5a001121-814e-5750-9d61-60f3a70ab607/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "6c5911b8-0c75-5135-a04a-a1d4d0611ba6",
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
    "hypothesis_id": "6c5911b8-0c75-5135-a04a-a1d4d0611ba6",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "6c5911b8-0c75-5135-a04a-a1d4d0611ba6",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.04609417143725929
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
    "hypothesis_id": "e2373b02-7453-5ed6-bfdc-bd1dfc9fc7ea",
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
    "hypothesis_id": "e2373b02-7453-5ed6-bfdc-bd1dfc9fc7ea",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.341388153823463
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-1.835159576984008, 2.311451958930655, -0.4762923819466386] | {'down': 0.3731145195893065, 'flat': 0.24523707618053361, 'up': 0.38164840423015994} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3731145195893065, 'flat': 0.24523707618053361, 'up': 0.38164840423015994} | [0.31884577735785125, -0.24753014254474404, -0.07131563481312109] | {'down': 0.3706392181638591, 'flat': 0.2445239198324024, 'up': 0.38483686200373846} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3706392181638591, 'flat': 0.2445239198324024, 'up': 0.38483686200373846} | [4.76001319113451, -3.617203781573303, -1.1428094095612074] | {'down': 0.33446718034812606, 'flat': 0.23309582573679033, 'up': 0.43243699391508356} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.33446718034812606, 'flat': 0.23309582573679033, 'up': 0.43243699391508356} | [4.8699535106173535, -3.5616008575548754, -1.3083526530624778] | {'down': 0.2988511717725773, 'flat': 0.22001229920616555, 'up': 0.4811365290212571} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2988511717725773, 'flat': 0.22001229920616555, 'up': 0.4811365290212571} | [-7.68311765330264, 9.053829306576139, -1.370711653273493] | {'down': 0.3893894648383387, 'flat': 0.20630518267343062, 'up': 0.4043053524882307} |
| 5 | E10/causal | ['5a001121-814e-5750-9d61-60f3a70ab607/1w/technical'] | {'down': 0.3893894648383387, 'flat': 0.20630518267343062, 'up': 0.4043053524882307} | [-0.48343947481762073, 0.4809086498853976, 0.002530824932223119] | {'down': 0.39419855133719267, 'flat': 0.20633049092275285, 'up': 0.3994709577400545} |
| 6 | E17/scenario | ['59935326-89ec-5faa-8a69-c954911ca4ca', 'a32e57a5-8fc0-5b70-ae2c-97e224a08395', '0e4a215e-55a4-52d8-baa8-69529aede3bd', '879bed06-ee10-5ed6-9602-a17ff350a619'] | {'down': 0.39419855133719267, 'flat': 0.20633049092275285, 'up': 0.3994709577400545} | [0.5825716949219018, 2.0829967819140984, -2.6655684768360026] | {'down': 0.41502851915633365, 'flat': 0.17967480615439282, 'up': 0.4052966746892735} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.41502851915633365, 'flat': 0.17967480615439282, 'up': 0.4052966746892735} | [-0.878335818404935, -0.9971161225640457, 1.8754519409689778] | {'down': 0.4050573579306932, 'flat': 0.1984293255640826, 'up': 0.39651331650522414} |
| 8 | E13/history | [] | {'down': 0.4050573579306932, 'flat': 0.1984293255640826, 'up': 0.39651331650522414} | [0.0, 0.0, 0.0] | {'down': 0.4050573579306932, 'flat': 0.1984293255640826, 'up': 0.39651331650522414} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4050573579306932, 'flat': 0.1984293255640826, 'up': 0.39651331650522414} | [-0.6868129622786545, -0.8121437832619927, 1.498956745540661] | {'down': 0.39693592009807327, 'flat': 0.21341889301948921, 'up': 0.3896451868824376} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b4cbddba8b828240130b5d972aeebdda49ce919951c28051975c6507ea57b211'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "5a001121-814e-5750-9d61-60f3a70ab607/1m/technical",
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
      1024,
      1031
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
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  },
  "primary": "1d",
  "reflexivity_effect": -0.034999999999999996,
  "regime_effect": -0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 10635.428026631338,
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
    "rsi": 37.3559943028347,
    "sma": [
      193675.0,
      187461.66666666666,
      190230.83333333334
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
    "volume_ratio": 1.050487717885096
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '5a001121-814e-5750-9d61-60f3a70ab607/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.034999999999999996, 'regime_effect': -0.0525}
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
    "hypothesis_id": "7f7f27fb-f46a-5b35-9575-939157a46b62",
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
    "hypothesis_id": "7f7f27fb-f46a-5b35-9575-939157a46b62",
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
    "hypothesis_id": "7f640b1e-6cca-5927-a00c-d5c2e751498d",
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
    "hypothesis_id": "7f640b1e-6cca-5927-a00c-d5c2e751498d",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.405175653823463
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "7f640b1e-6cca-5927-a00c-d5c2e751498d",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": -1,
    "strength": 0.017693328562740713
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.8459098614872818, 1.059395061286883, -0.21348519979959846] | {'down': 0.3605939506128688, 'flat': 0.24786514800200402, 'up': 0.3915409013851272} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.3605939506128688, 'flat': 0.24786514800200402, 'up': 0.3915409013851272} | [-0.03698896932630702, 0.0465611860066939, -0.009572216680378554] | {'down': 0.36105956247293575, 'flat': 0.24776942583520023, 'up': 0.39117101169186413} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.36105956247293575, 'flat': 0.24776942583520023, 'up': 0.39117101169186413} | [3.8050208718909295, -2.8631143840290916, -0.9419064878618544] | {'down': 0.33242841863264483, 'flat': 0.23835036095658169, 'up': 0.42922122041077343} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.33242841863264483, 'flat': 0.23835036095658169, 'up': 0.42922122041077343} | [3.8789089385012243, -2.8285892209993504, -1.0503197175018602] | {'down': 0.3041425264226513, 'flat': 0.22784716378156308, 'up': 0.4680103097957857} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3041425264226513, 'flat': 0.22784716378156308, 'up': 0.4680103097957857} | [-5.675385228137719, 6.722208400057511, -1.0468231719198058] | {'down': 0.37136461042322644, 'flat': 0.21737893206236503, 'up': 0.4112564575144085} |
| 5 | E10/causal | ['5a001121-814e-5750-9d61-60f3a70ab607/1m/technical'] | {'down': 0.37136461042322644, 'flat': 0.21737893206236503, 'up': 0.4112564575144085} | [-2.059861174882643, 2.0377400172240434, 0.022121157658611112] | {'down': 0.39174201059546687, 'flat': 0.21760014363895114, 'up': 0.39065784576558205} |
| 6 | E17/scenario | ['fd0b5954-6cc0-5abf-bc7a-5b2fe98a574d', '513b09fc-9c90-5d26-ba44-e6c7521fe2e9', 'f05d94df-5baa-5280-a679-38c4408e1ca7', '83d6f788-ebbb-551a-bf51-4c32532dd8d7'] | {'down': 0.39174201059546687, 'flat': 0.21760014363895114, 'up': 0.39065784576558205} | [1.0261015970559895, 2.0976092352052, -3.1237108322611977] | {'down': 0.4127181029475189, 'flat': 0.18636303531633916, 'up': 0.40091886173614194} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.4127181029475189, 'flat': 0.18636303531633916, 'up': 0.40091886173614194} | [-0.8281178508907028, -0.9726926216296505, 1.8008104725203506] | {'down': 0.40299117673122237, 'flat': 0.20437114004154266, 'up': 0.3926376832272349} |
| 8 | E13/history | [] | {'down': 0.40299117673122237, 'flat': 0.20437114004154266, 'up': 0.3926376832272349} | [0.0, 0.0, 0.0] | {'down': 0.40299117673122237, 'flat': 0.20437114004154266, 'up': 0.3926376832272349} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.40299117673122237, 'flat': 0.20437114004154266, 'up': 0.3926376832272349} | [-0.6488335435354431, -0.8002643925467401, 1.4490979360821887] | {'down': 0.39498853280575497, 'flat': 0.21886211940236455, 'up': 0.3861493477918805} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '98e2c87198c88bf6b4c41d4cc4225a493845c0fcdc6041f9def4150aaf944fad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '98e2c87198c88bf6b4c41d4cc4225a493845c0fcdc6041f9def4150aaf944fad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '98e2c87198c88bf6b4c41d4cc4225a493845c0fcdc6041f9def4150aaf944fad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '98e2c87198c88bf6b4c41d4cc4225a493845c0fcdc6041f9def4150aaf944fad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '98e2c87198c88bf6b4c41d4cc4225a493845c0fcdc6041f9def4150aaf944fad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '98e2c87198c88bf6b4c41d4cc4225a493845c0fcdc6041f9def4150aaf944fad'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '98e2c87198c88bf6b4c41d4cc4225a493845c0fcdc6041f9def4150aaf944fad'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:b4cbddba8b828240130b5d972aeebdda49ce919951c28051975c6507ea57b211'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:f8fbb4916fdecaf7e1e2e295f4fed29f6dfad23291a882af383abccdbf412aa1#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:15f8f109a2358163453a0dec5a0775a723a22606a17db8c099d989e6f494ba01#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:22ccc2c285a78a4cfb116caf1548ea2e7ff5e3ea412cc873d20559b079fc8927#us_10y_yield@2026-10-09T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "5a001121-814e-5750-9d61-60f3a70ab607/1y/technical",
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
      1024,
      1031
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
      1034,
      1039
    ],
    "top_score": 0.2,
    "volume_ratio": 1.217229696011059
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '5a001121-814e-5750-9d61-60f3a70ab607/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.020000000000000004, 'regime_effect': -0.03}
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
    "hypothesis_id": "07e45836-7845-5205-9420-9850267d6d5c",
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
    "hypothesis_id": "07e45836-7845-5205-9420-9850267d6d5c",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.81
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "07e45836-7845-5205-9420-9850267d6d5c",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.009644171437259286
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
    "hypothesis_id": "03b2365b-a961-5139-af70-aa94261081aa",
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
    "hypothesis_id": "03b2365b-a961-5139-af70-aa94261081aa",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.377838153823463
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
