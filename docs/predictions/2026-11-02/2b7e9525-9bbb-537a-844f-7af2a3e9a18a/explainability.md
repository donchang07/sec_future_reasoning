# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: 2b7e9525-9bbb-537a-844f-7af2a3e9a18a
Cutoff / prediction: 2026-11-01T22:00:16.528927+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-30T06:30:00+00:00', 'source_refs': ['raw:5fc1ef4decfd2459f46db36c30acaf80a0611579e5627d983b12bcd417018c5f'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 174100.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 38.1828% | 39.7569% | 22.0603% | 4.8389% | 0.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 39.7995% | 37.7347% | 22.4658% | 2.4643% | 45.0000% | 10.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 10.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 38.1828% / 39.7569% / 22.0603% | 38.1828% / 39.7569% / 22.0603% | [0.0, 0.0, 0.0] |
| 1m | 38.5885% / 38.9378% / 22.4737% | 39.7995% / 37.7347% / 22.4658% | [1.2109779870950022, -1.2030607521497927, -0.007917234945209461] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 63.504591368611116,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-01T22:00:15.647737Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "5fc1ef4decfd2459f46db36c30acaf80a0611579e5627d983b12bcd417018c5f",
    "reason": null,
    "released_at": null,
    "rows": 241,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 63.504591368611116,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-01T22:00:16.072825Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 63.504591368611116,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-01T22:00:16.014310Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 50.504591368611116,
    "authority": "official_original",
    "collected_at": "2026-11-01T22:00:15.794162Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-30T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98",
    "reason": null,
    "released_at": null,
    "rows": 209,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-01T22:00:16.125332Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "97809fc4054dd1b5fb666e2c9a314afff459ced34c373228381dfe13032ab0a9",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 63.504591368611116,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-01T22:00:16.317391Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-30T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "8e5b07c2508d7fd708965d755da6ec4572698d59ed41550db2a6307ab0482cf4",
    "reason": null,
    "released_at": null,
    "rows": 245,
    "source_id": "kospi",
    "status": "fresh",
    "used_by_model": false
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-11-01T22:00:16.527928Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "8c63915085521474d0f0b260133d1c03a04f84e50c46a4cc46a970ae3ad25980",
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
    "collected_at": "2026-11-01T22:00:16.072825Z",
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
    "collected_at": "2026-11-01T22:00:16.072825Z",
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
    "collected_at": "2026-11-01T22:00:16.072825Z",
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
    "collected_at": "2026-11-01T22:00:16.072825Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-30T06:30:00+00:00'}, '1mo': {'count': 240, 'last': '2026-10-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-10-30T06:30:00+00:00'}, '30m': {'count': 241, 'last': '2026-10-30T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:8e5b07c2508d7fd708965d755da6ec4572698d59ed41550db2a6307ab0482cf4'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_rsi_14@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_rsi_14@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_trend_alignment@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_trend_alignment@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_volume_z@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_volume_z@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1w/technical",
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
    "atr": 11529.88776541418,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4921,
      4927
    ],
    "bottom_score": 0.44999999999999996,
    "rsi": 46.10801995017749,
    "sma": [
      179205.0,
      187303.33333333334,
      191546.66666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 154400.0,
    "top_pivots": [
      4909,
      4925
    ],
    "top_score": 0.1,
    "volume_ratio": 1.354423747083146
  },
  "primary": "30m",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 3040.485586005412,
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
    "bottom_neckline": 187700.0,
    "bottom_pivots": [
      223,
      232
    ],
    "bottom_score": 0.0,
    "rsi": 43.55056764861911,
    "sma": [
      176947.5,
      176667.5,
      172580.41666666666
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
    "top_neckline": 168100.0,
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
Feedback applied once: {'batch_id': '2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "1ab4739a-9f71-50b3-be13-d131c732535a",
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
    "hypothesis_id": "1ab4739a-9f71-50b3-be13-d131c732535a",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "1ab4739a-9f71-50b3-be13-d131c732535a",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.1594857702414395
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
    "hypothesis_id": "8ddd97e2-d3f4-5e24-9469-d36e6b880658",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8ddd97e2-d3f4-5e24-9469-d36e6b880658",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.05254173067260384
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.28181154668596164, 0.3517765073725365, -0.06996496068656655] | {'down': 0.35351776507372534, 'flat': 0.24930035039313433, 'up': 0.3971818845331404} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.35351776507372534, 'flat': 0.24930035039313433, 'up': 0.3971818845331404} | [1.1170201120158207, -0.8411547654451179, -0.2758653465707195] | {'down': 0.34510621741927416, 'flat': 0.24654169692742714, 'up': 0.4083520856532986} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.34510621741927416, 'flat': 0.24654169692742714, 'up': 0.4083520856532986} | [2.390628433188635, -1.7735825442885933, -0.6170458889000391] | {'down': 0.32737039197638823, 'flat': 0.24037123803842675, 'up': 0.43225836998518496} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.32737039197638823, 'flat': 0.24037123803842675, 'up': 0.43225836998518496} | [2.4180499393703814, -1.7588099496395726, -0.6592399897307977] | {'down': 0.3097822924799925, 'flat': 0.23377883814111877, 'up': 0.4564388693788888} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3097822924799925, 'flat': 0.23377883814111877, 'up': 0.4564388693788888} | [-7.075698206430197, 8.55497368833552, -1.4792754819053315] | {'down': 0.3953320293633477, 'flat': 0.21898608332206546, 'up': 0.3856818873145868} |
| 5 | E10/causal | ['2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1w/technical'] | {'down': 0.3953320293633477, 'flat': 0.21898608332206546, 'up': 0.3856818873145868} | [0.1714645145170446, -0.17222894895593255, 0.0007644344388990643] | {'down': 0.3936097398737884, 'flat': 0.21899372766645445, 'up': 0.38739653245975725} |
| 6 | E17/scenario | ['56b67524-bfb2-52b3-aabd-5a96fcf941d6', '4d212bea-59c5-5b9e-8008-cdf3c19c4c76', 'b5187531-c25f-5839-9b6a-5b1aaeafd5fe', '25243a93-35fa-5384-b3c6-40b6362279a0'] | {'down': 0.3936097398737884, 'flat': 0.21899372766645445, 'up': 0.38739653245975725} | [0.8515682359789389, 2.3541329181645643, -3.2057011541435143] | {'down': 0.41715106905543403, 'flat': 0.1869367161250193, 'up': 0.39591221481954664} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.41715106905543403, 'flat': 0.1869367161250193, 'up': 0.39591221481954664} | [-0.826531286119786, -1.1070504818993743, 1.9335817680191714] | {'down': 0.4060805642364403, 'flat': 0.20627253380521102, 'up': 0.3876469019583488} |
| 8 | E13/history | [] | {'down': 0.4060805642364403, 'flat': 0.20627253380521102, 'up': 0.3876469019583488} | [0.0, 0.0, 0.0] | {'down': 0.4060805642364403, 'flat': 0.20627253380521102, 'up': 0.3876469019583488} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.4060805642364403, 'flat': 0.20627253380521102, 'up': 0.3876469019583488} | [-0.5818712914703095, -0.85118175401806, 1.4330530454883612] | {'down': 0.3975687466962597, 'flat': 0.22060306426009463, 'up': 0.3818281890436457} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:8e5b07c2508d7fd708965d755da6ec4572698d59ed41550db2a6307ab0482cf4'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_rsi_14@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_rsi_14@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_trend_alignment@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_trend_alignment@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_volume_z@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_volume_z@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1m/technical",
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
    "atr": 24694.383776298808,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      1029,
      1040
    ],
    "bottom_score": 0.1,
    "rsi": 48.1424750550949,
    "sma": [
      192480.0,
      142174.16666666666,
      96333.75
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      1032,
      1037
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  },
  "primary": "1d",
  "reflexivity_effect": 0.034999999999999996,
  "regime_effect": 0.0525,
  "sell_liquidity": null,
  "wave": {
    "atr": 11529.88776541418,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": true,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 176000.0,
    "bottom_pivots": [
      4921,
      4927
    ],
    "bottom_score": 0.44999999999999996,
    "rsi": 46.10801995017749,
    "sma": [
      179205.0,
      187303.33333333334,
      191546.66666666666
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 154400.0,
    "top_pivots": [
      4909,
      4925
    ],
    "top_score": 0.1,
    "volume_ratio": 1.354423747083146
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': '2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.034999999999999996, 'regime_effect': 0.0525}
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
    "hypothesis_id": "8ba72d39-ea4a-5456-8708-9d8c26984213",
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
    "hypothesis_id": "8ba72d39-ea4a-5456-8708-9d8c26984213",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8ba72d39-ea4a-5456-8708-9d8c26984213",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.22327327024143948
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "8ba72d39-ea4a-5456-8708-9d8c26984213",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.011245769327396153
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
    "hypothesis_id": "c695292b-26bb-5b32-aacc-653c04e395e2",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.030552930361033015, -0.02300043336037061, -0.007552497000656855] | {'down': 0.34976999566639627, 'flat': 0.24992447502999343, 'up': 0.40030552930361035} |
| 1 | E12/causal | ['preferred_volume_z'] | {'down': 0.34976999566639627, 'flat': 0.24992447502999343, 'up': 0.40030552930361035} | [0.6080209641889156, -0.45644820921654783, -0.15157275497236777] | {'down': 0.3452055135742308, 'flat': 0.24840874748026975, 'up': 0.4063857389454995} |
| 2 | E12/causal | ['samsung_common_price'] | {'down': 0.3452055135742308, 'flat': 0.24840874748026975, 'up': 0.4063857389454995} | [1.9064228846249809, -1.4158141456345197, -0.490608738990464] | {'down': 0.3310473721178856, 'flat': 0.24350266009036511, 'up': 0.4254499677917493} |
| 3 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3310473721178856, 'flat': 0.24350266009036511, 'up': 0.4254499677917493} | [1.925952134139658, -1.4075714322384192, -0.5183807019012332] | {'down': 0.3169716577955014, 'flat': 0.23831885307135278, 'up': 0.4447094891331459} |
| 4 | E12/causal | ['us_10y_yield'] | {'down': 0.3169716577955014, 'flat': 0.23831885307135278, 'up': 0.4447094891331459} | [-5.255440100243513, 6.382750191067643, -1.1273100908241322] | {'down': 0.38079915970617784, 'flat': 0.22704575216311146, 'up': 0.39215508813071076} |
| 5 | E10/causal | ['2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1m/technical'] | {'down': 0.38079915970617784, 'flat': 0.22704575216311146, 'up': 0.39215508813071076} | [1.7383579794699566, -1.70938143057624, -0.028976548893727694] | {'down': 0.36370534540041544, 'flat': 0.22675598667417418, 'up': 0.4095386679254103} |
| 6 | E17/scenario | ['0aeb4682-4755-517b-a656-431ca3e18684', '9aafc702-6fd2-56bf-9456-b11397ad447f', '02c4f3d9-6003-5653-8099-04c10d9a0d25', '098fb6dd-21ea-5c11-9e9a-7f2779653b9d'] | {'down': 0.36370534540041544, 'flat': 0.22675598667417418, 'up': 0.4095386679254103} | [0.8370734551192249, 2.6351708205631597, -3.47224427568239] | {'down': 0.39005705360604703, 'flat': 0.19203354391735028, 'up': 0.4179094024766026} |
| 7 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.39005705360604703, 'flat': 0.19203354391735028, 'up': 0.4179094024766026} | [-1.1181661022016787, -0.7499348437709497, 1.8681009459726257] | {'down': 0.38255770516833754, 'flat': 0.21071455337707654, 'up': 0.4067277414545858} |
| 8 | E13/history | [] | {'down': 0.38255770516833754, 'flat': 0.21071455337707654, 'up': 0.4067277414545858} | [0.0, 0.0, 0.0] | {'down': 0.38255770516833754, 'flat': 0.21071455337707654, 'up': 0.4067277414545858} |
| 9 | E18/calibration | ['temperature:1.15'] | {'down': 0.38255770516833754, 'flat': 0.21071455337707654, 'up': 0.4067277414545858} | [-0.8732824227385527, -0.5210496424285616, 1.394332065167128] | {'down': 0.3773472087440519, 'flat': 0.22465787402874782, 'up': 0.39799491722720026} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '219cb9fc73e5c3db76ece4b3db4661a1f12786e85e6fcae8063470bf692d789a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '219cb9fc73e5c3db76ece4b3db4661a1f12786e85e6fcae8063470bf692d789a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '219cb9fc73e5c3db76ece4b3db4661a1f12786e85e6fcae8063470bf692d789a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '219cb9fc73e5c3db76ece4b3db4661a1f12786e85e6fcae8063470bf692d789a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '219cb9fc73e5c3db76ece4b3db4661a1f12786e85e6fcae8063470bf692d789a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '219cb9fc73e5c3db76ece4b3db4661a1f12786e85e6fcae8063470bf692d789a'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '219cb9fc73e5c3db76ece4b3db4661a1f12786e85e6fcae8063470bf692d789a'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:8e5b07c2508d7fd708965d755da6ec4572698d59ed41550db2a6307ab0482cf4'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_rsi_14@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_rsi_14@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_trend_alignment@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_trend_alignment@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_volume_z@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#preferred_volume_z@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:07d56edbe1813dd0b3eb69a93d1fecb30d4ba385052c2e21d6946c0b1a86131c#samsung_common_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:2eb3b41d9e8b658dafd138033db413a87885396239d830af1445516504642f70#samsung_preferred_price@2026-10-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:795e49bf8efd80e31649b90f88b1ae382fe3ebdb645f928436248261c7c8dd98#us_10y_yield@2026-10-23T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1y/technical",
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
    "atr": 30149.603866601974,
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
    "rsi": 64.65633306086202,
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
      220,
      235
    ],
    "top_score": 0.1,
    "volume_ratio": 1.1963416147691088
  },
  "primary": "1w",
  "reflexivity_effect": -0.030000000000000006,
  "regime_effect": -0.045000000000000005,
  "sell_liquidity": null,
  "wave": {
    "atr": 24694.383776298808,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": false,
      "divergence": false,
      "double": false,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "bottom_neckline": 220000.0,
    "bottom_pivots": [
      1029,
      1040
    ],
    "bottom_score": 0.1,
    "rsi": 48.1424750550949,
    "sma": [
      192480.0,
      142174.16666666666,
      96333.75
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": false,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": true,
      "volume": false
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      1032,
      1037
    ],
    "top_score": 0.4,
    "volume_ratio": 1.2256089562225412
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': '2b7e9525-9bbb-537a-844f-7af2a3e9a18a/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.030000000000000006, 'regime_effect': -0.045000000000000005}
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
    "hypothesis_id": "e3b86df6-0ccb-5a2b-9a98-00cb7e977ad5",
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
    "hypothesis_id": "e3b86df6-0ccb-5a2b-9a98-00cb7e977ad5",
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
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "e3b86df6-0ccb-5a2b-9a98-00cb7e977ad5",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.10481077024143949
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
    "hypothesis_id": "40a7b1cb-ee3e-52c9-99a4-21d8b9571d9a",
    "node_ids": [
      "us_10y_yield",
      "module:macro",
      "preferred_price"
    ],
    "path_id": "us_10y_yield_to_macro/macro_to_price",
    "root_evidence_group": "us_10y_yield",
    "sign": -1,
    "strength": 0.7614000000000004
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "40a7b1cb-ee3e-52c9-99a4-21d8b9571d9a",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.10721673067260386
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
