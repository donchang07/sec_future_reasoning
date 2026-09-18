# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 2385b632-a398-586d-b081-1e9b2bec0f78
Cutoff / prediction: 2026-09-18T22:00:11.916539+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-18T06:30:00+00:00', 'source_refs': ['raw:e5a486bbe29677c0e06ebe45786ad79bbca4eebd13f471f91bfa35228024fb97'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 196100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 45.6459% | 33.6600% | 20.6941% | 7.9026% | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 43.7966% | 34.6877% | 21.5158% | 6.2745% | 45.0000% | 30.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 46.1508% / 33.2205% / 20.6287% | 45.6459% / 33.6600% / 20.6941% | [-0.5048858300278736, 0.4394704765806723, 0.06541535344720961] |
| 1m | 43.2512% / 35.1778% / 21.5710% | 43.7966% / 34.6877% / 21.5158% | [0.5453970593497726, -0.49014498712722787, -0.05525207222255302] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.503310149722221,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-18T22:00:11.069758Z",
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
    "age_hours": 15.503310149722221,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-18T22:00:11.383353Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.503310149722221,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-18T22:00:11.425702Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-18T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd",
    "reason": null,
    "released_at": null,
    "rows": 4936,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.503310149722222,
    "authority": "official_original",
    "collected_at": "2026-09-18T22:00:11.209681Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-18T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085",
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
    "collected_at": "2026-09-18T22:00:11.633401Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "c27f70e1ae70cb9797de02bd6ab5ecf9b66f581b40e855a6a0a4620d4dd8a093",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.503310149722225,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-18T22:00:11.683939Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-17T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c47e1bad1e4de9a6efa8efd243a14f8eaa23b4a5863363b7feea40f711d3ccb1",
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
    "collected_at": "2026-09-18T22:00:11.915542Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "caa76409e4a7909fa799bfe25c621812c2a9add52498fd8105126d42fb632d85",
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
    "collected_at": "2026-09-18T22:00:11.425702Z",
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
    "collected_at": "2026-09-18T22:00:11.425702Z",
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
    "collected_at": "2026-09-18T22:00:11.425702Z",
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
    "collected_at": "2026-09-18T22:00:11.425702Z",
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c47e1bad1e4de9a6efa8efd243a14f8eaa23b4a5863363b7feea40f711d3ccb1'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "2385b632-a398-586d-b081-1e9b2bec0f78/1w/technical",
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
Feedback applied once: {'batch_id': '2385b632-a398-586d-b081-1e9b2bec0f78/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "6914fa31-b2ec-5528-8654-a8386014529c",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.791775
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "6914fa31-b2ec-5528-8654-a8386014529c",
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
    "hypothesis_id": "6914fa31-b2ec-5528-8654-a8386014529c",
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
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "6914fa31-b2ec-5528-8654-a8386014529c",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.0706852404568202
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
    "hypothesis_id": "8fec0fe3-7528-5505-9f32-15d8a167719a",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.49466502360889786, -0.37163269812791055, -0.12303232548098175] | {'down': 0.3462836730187209, 'flat': 0.24876967674519018, 'up': 0.404946650236089} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3462836730187209, 'flat': 0.24876967674519018, 'up': 0.404946650236089} | [5.637098658951628, -4.127442486604377, -1.5096561723472512] | {'down': 0.3050092481526771, 'flat': 0.23367311502171767, 'up': 0.4613176368256053} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3050092481526771, 'flat': 0.23367311502171767, 'up': 0.4613176368256053} | [4.870978576744983, -3.420065599921135, -1.4509129768238538] | {'down': 0.27080859215346575, 'flat': 0.21916398525347913, 'up': 0.5100274225930551} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.27080859215346575, 'flat': 0.21916398525347913, 'up': 0.5100274225930551} | [4.833689332871027, -3.271783810817419, -1.5619055220536056] | {'down': 0.23809075404529156, 'flat': 0.20354493003294308, 'up': 0.5583643159217654} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.23809075404529156, 'flat': 0.20354493003294308, 'up': 0.5583643159217654} | [-7.479467051153371, 8.163084816994997, -0.6836177658416237] | {'down': 0.31972160221524154, 'flat': 0.19670875237452684, 'up': 0.4835696454102317} |
| 5 | E10/causal | ['2385b632-a398-586d-b081-1e9b2bec0f78/1w/technical'] | {'down': 0.31972160221524154, 'flat': 0.19670875237452684, 'up': 0.4835696454102317} | [1.0293792649593625, -0.9424593597488373, -0.08691990521051962] | {'down': 0.31029700861775317, 'flat': 0.19583955332242164, 'up': 0.4938634380598253} |
| 6 | E17/scenario | ['56ffc792-debe-5931-881e-9afbdff89348', 'ed5a647f-3e04-5053-bfdb-7dfb59afd327', 'f93c3cdb-c295-5832-be55-7b691b515793', '2ee5900e-2e27-5fc3-b6a5-99fc606be520'] | {'down': 0.31029700861775317, 'flat': 0.19583955332242164, 'up': 0.4938634380598253} | [0.011373023396454851, 2.4173985467459245, -2.4287715701423935] | {'down': 0.3344709940852124, 'flat': 0.1715518376209977, 'up': 0.49397716829378985} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3344709940852124, 'flat': 0.1715518376209977, 'up': 0.49397716829378985} | [-1.9394702166365574, -0.013735100045692006, 1.953205316682252] | {'down': 0.3343336430847555, 'flat': 0.19108389078782023, 'up': 0.4745824661274243} |
| 8 | E13/history | [] | {'down': 0.3343336430847555, 'flat': 0.19108389078782023, 'up': 0.4745824661274243} | [0.0, 0.0, 0.0] | {'down': 0.3343336430847555, 'flat': 0.19108389078782023, 'up': 0.4745824661274243} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.3343336430847555, 'flat': 0.19108389078782023, 'up': 0.4745824661274243} | [-1.8123392014403272, 0.22658751990836112, 1.5857516815319688] | {'down': 0.3365995182838391, 'flat': 0.20694140760313992, 'up': 0.456459074113021} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c47e1bad1e4de9a6efa8efd243a14f8eaa23b4a5863363b7feea40f711d3ccb1'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "2385b632-a398-586d-b081-1e9b2bec0f78/1m/technical",
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
Feedback applied once: {'batch_id': '2385b632-a398-586d-b081-1e9b2bec0f78/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.015000000000000003, 'regime_effect': 0.022500000000000003}
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
    "hypothesis_id": "03406e03-6842-509a-87e5-f88c38c3f2da",
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
    "hypothesis_id": "03406e03-6842-509a-87e5-f88c38c3f2da",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "03406e03-6842-509a-87e5-f88c38c3f2da",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.8373375
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "03406e03-6842-509a-87e5-f88c38c3f2da",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.11624774045682022
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
    "hypothesis_id": "eaf1271a-272c-58e3-9c94-bbd9a2c8f69f",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.31616194955326193, -0.23771151881900598, -0.07845043073425595] | {'down': 0.3476228848118099, 'flat': 0.24921549569265744, 'up': 0.40316161949553264} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.3476228848118099, 'flat': 0.24921549569265744, 'up': 0.40316161949553264} | [2.2972732872719726, -1.7079543291886545, -0.5893189580833125] | {'down': 0.3305433415199234, 'flat': 0.24332230611182432, 'up': 0.42613435236825237} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3305433415199234, 'flat': 0.24332230611182432, 'up': 0.42613435236825237} | [3.8667070852700105, -2.8023344909310524, -1.0643725943389608] | {'down': 0.30251999661061285, 'flat': 0.2326785801684347, 'up': 0.46480142322095247} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.30251999661061285, 'flat': 0.2326785801684347, 'up': 0.46480142322095247} | [3.8976687950235176, -2.7394587247742965, -1.158210070249216] | {'down': 0.2751254093628699, 'flat': 0.22109647946594255, 'up': 0.5037781111711876} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.2751254093628699, 'flat': 0.22109647946594255, 'up': 0.5037781111711876} | [-5.6420560367155534, 6.435306024990134, -0.7932499882745803] | {'down': 0.3394784696127712, 'flat': 0.21316397958319674, 'up': 0.4473575508040321} |
| 5 | E10/causal | ['2385b632-a398-586d-b081-1e9b2bec0f78/1m/technical'] | {'down': 0.3394784696127712, 'flat': 0.21316397958319674, 'up': 0.4473575508040321} | [2.164703935566581, -2.0162684272127085, -0.1484355083538752] | {'down': 0.31931578534064414, 'flat': 0.211679624499658, 'up': 0.4690045901596979} |
| 6 | E17/scenario | ['dcea96ad-b16a-5565-8b52-2fad0f51bbb5', 'fd517ce8-89a9-59cf-b8da-e20222bc73b2', '7aef5a90-de77-53c7-9050-334d78d06c58', '610e010e-b7d0-548e-b43d-f2755e6d1a52'] | {'down': 0.31931578534064414, 'flat': 0.211679624499658, 'up': 0.4690045901596979} | [0.07793599491691117, 2.9148800225268614, -2.992816017443778] | {'down': 0.34846458556591275, 'flat': 0.1817514643252202, 'up': 0.46978395010886703} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.34846458556591275, 'flat': 0.1817514643252202, 'up': 0.46978395010886703} | [-1.6552854220205582, -0.1835575523906008, 1.8388429744111616] | {'down': 0.34662901004200675, 'flat': 0.20013989406933183, 'up': 0.45323109588866145} |
| 8 | E13/history | [] | {'down': 0.34662901004200675, 'flat': 0.20013989406933183, 'up': 0.45323109588866145} | [0.0, 0.0, 0.0] | {'down': 0.34662901004200675, 'flat': 0.20013989406933183, 'up': 0.45323109588866145} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.34662901004200675, 'flat': 0.20013989406933183, 'up': 0.45323109588866145} | [-1.5265351262671034, 0.024767250691049014, 1.5017678755760488] | {'down': 0.34687668254891724, 'flat': 0.21515757282509232, 'up': 0.4379657446259904} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '60d9fcb9b444b386839ad2a3f2a4f132f335658771b1da6021c359d471a1e6b4'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '60d9fcb9b444b386839ad2a3f2a4f132f335658771b1da6021c359d471a1e6b4'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '60d9fcb9b444b386839ad2a3f2a4f132f335658771b1da6021c359d471a1e6b4'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '60d9fcb9b444b386839ad2a3f2a4f132f335658771b1da6021c359d471a1e6b4'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '60d9fcb9b444b386839ad2a3f2a4f132f335658771b1da6021c359d471a1e6b4'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '60d9fcb9b444b386839ad2a3f2a4f132f335658771b1da6021c359d471a1e6b4'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '60d9fcb9b444b386839ad2a3f2a4f132f335658771b1da6021c359d471a1e6b4'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c47e1bad1e4de9a6efa8efd243a14f8eaa23b4a5863363b7feea40f711d3ccb1'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:43c55da498a3109084134eea905d19a02096eb52e08d7821cb4d41bd797b47bd#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:054cf71bff948706277e6d378221e795bbb4665f414f055afc39aaef002f7c4e#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:519fc08eee21242ffe0cc859e34fce65b452901f88ea63c9edc34680724ad085#us_10y_yield@2026-09-11T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "2385b632-a398-586d-b081-1e9b2bec0f78/1y/technical",
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
Feedback applied once: {'batch_id': '2385b632-a398-586d-b081-1e9b2bec0f78/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "b69bf7b4-e052-5076-b384-9d2cfd7258d2",
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
    "hypothesis_id": "b69bf7b4-e052-5076-b384-9d2cfd7258d2",
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
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "b69bf7b4-e052-5076-b384-9d2cfd7258d2",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.791775
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "b69bf7b4-e052-5076-b384-9d2cfd7258d2",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.0706852404568202
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
    "hypothesis_id": "c5bbfab4-7a4a-5fb2-adb8-768ad21c6625",
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
