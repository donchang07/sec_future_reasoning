# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: a4c806cb-22e4-5335-b2e3-2295b28333a6
Cutoff / prediction: 2026-09-26T22:00:13.721310+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-09-23T06:30:00+00:00', 'source_refs': ['raw:04a952a4af859f3b825f3396b1a16eb3fe7708f9562a87712f77783aeeb78985'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 220000.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 38.0472% | 39.8768% | 22.0760% | 3.6594% | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |
| 1m | 39.0894% | 38.3836% | 22.5271% | 3.0413% | 65.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 10.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 38.5051% / 39.4127% / 22.0822% | 38.0472% / 39.8768% / 22.0760% | [-0.45786171670380016, 0.4640674195279082, -0.00620570282408861] |
| 1m | 38.2203% / 39.2384% / 22.5412% | 39.0894% / 38.3836% / 22.5271% | [0.8690428390499716, -0.8548905032723597, -0.01415233577761743] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 87.50381147499999,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-26T22:00:12.760815Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "04a952a4af859f3b825f3396b1a16eb3fe7708f9562a87712f77783aeeb78985",
    "reason": null,
    "released_at": null,
    "rows": 277,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 87.50381147499999,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-26T22:00:13.475625Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518",
    "reason": null,
    "released_at": null,
    "rows": 4932,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 87.50381147499999,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-26T22:00:13.201917Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97",
    "reason": null,
    "released_at": null,
    "rows": 4934,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 26.503811475,
    "authority": "official_original",
    "collected_at": "2026-09-26T22:00:13.144397Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-09-25T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903",
    "reason": null,
    "released_at": null,
    "rows": 185,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-26T22:00:13.269920Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "26837378b900deada157cc03439f9a021e5dcde9cc7c770cf64a65606254ad66",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 87.50381147499999,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-09-26T22:00:13.720310Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-09-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "f0c0dbc45e99da4f6dc69e51b3308397836a6d55048aa8c797553b5465cf41fe",
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
    "collected_at": "2026-09-26T22:00:13.701808Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "f73b1b5ddec021b8aa83123ce6635dea0f40892ae82e0d93dfbffb74759dfa0d",
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
    "collected_at": "2026-09-26T22:00:13.269920Z",
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
    "collected_at": "2026-09-26T22:00:13.269920Z",
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
    "collected_at": "2026-09-26T22:00:13.269920Z",
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
    "collected_at": "2026-09-26T22:00:13.269920Z",
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
Document statuses: {'dram_spot': 'available_unmapped', 'exports_10': 'stale', 'exports_20': 'available_unmapped', 'exports_month': 'available_unmapped', 'krx_access': 'documentation_only; foreign/institution/program unavailable; no approved data API response', 'samsung_bs': 'available_unmapped', 'samsung_cf': 'available_unmapped', 'samsung_soi': 'available_unmapped'}
Bar boundaries: {'1d': {'count': 4932, 'last': '2026-09-23T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-08-31T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-09-25T06:30:00+00:00'}, '30m': {'count': 277, 'last': '2026-09-23T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.5833333333333334, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:f0c0dbc45e99da4f6dc69e51b3308397836a6d55048aa8c797553b5465cf41fe'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-18T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "a4c806cb-22e4-5335-b2e3-2295b28333a6/1w/technical",
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
    "atr": 9883.464688860755,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4917,
      4925
    ],
    "bottom_score": 0.65,
    "rsi": 64.68247187439766,
    "sma": [
      195245.0,
      188328.33333333334,
      184442.5
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4912,
      4922
    ],
    "top_score": 0.4,
    "volume_ratio": 1.688807602541006
  },
  "primary": "30m",
  "reflexivity_effect": -0.010000000000000002,
  "regime_effect": -0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1762.1091635620198,
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
      263,
      269
    ],
    "bottom_score": 0.0,
    "rsi": 71.33035351706422,
    "sma": [
      216850.0,
      206302.5,
      199028.33333333334
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
    "top_neckline": 210000.0,
    "top_pivots": [
      260,
      267
    ],
    "top_score": 0.1,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a4c806cb-22e4-5335-b2e3-2295b28333a6/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
Memory module state (coverage/semantic diagnostic, no invented graph route): {'conflict': 0.0, 'family_scores': {'dram_contract_asp': None, 'dram_spot_price': None, 'hbm_demand': None, 'hbm_price': None, 'memory_bit_shipment': None, 'memory_inventory': None, 'semiconductor_export_momentum': 1.0}, 'negative_families': [], 'positive_families': ['semiconductor_export_momentum'], 'root_contributions': {'semiconductor_export_momentum|kcs_exports:2026-07': 1.0, 'semiconductor_export_momentum|kcs_exports:2026-08': 1.0}, 'score': 1.0, 'unknown_families': ['dram_contract_asp', 'dram_spot_price', 'hbm_demand', 'hbm_price', 'memory_inventory', 'memory_bit_shipment']}

positive_paths (up to five; never padded)
```json
[
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "159f91a3-29d3-551c-aca8-858969df6786",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.19035
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "159f91a3-29d3-551c-aca8-858969df6786",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.19035
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_common_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "159f91a3-29d3-551c-aca8-858969df6786",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "159f91a3-29d3-551c-aca8-858969df6786",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "159f91a3-29d3-551c-aca8-858969df6786",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.08695668515218423
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
    "hypothesis_id": "e57ee435-e6d9-5be5-967c-0b988497faba",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.6087852625389412, -0.4571421586643032, -0.1516431038746463] | {'down': 0.34542857841335695, 'flat': 0.24848356896125354, 'up': 0.40608785262538943} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34542857841335695, 'flat': 0.24848356896125354, 'up': 0.40608785262538943} | [1.3414894036719416, -0.9989036000454254, -0.3425858036265217] | {'down': 0.3354395424129027, 'flat': 0.24505771092498832, 'up': 0.41950274666210885} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.3354395424129027, 'flat': 0.24505771092498832, 'up': 0.41950274666210885} | [1.3520615560685068, -0.9953808897701477, -0.35668066629834516] | {'down': 0.3254857335152012, 'flat': 0.24149090426200487, 'up': 0.4330233622227939} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.3254857335152012, 'flat': 0.24149090426200487, 'up': 0.4330233622227939} | [1.2058940248548644, -0.878436021742901, -0.32745800311196893] | {'down': 0.3167013732977722, 'flat': 0.23821632423088518, 'up': 0.44508230247134256} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3167013732977722, 'flat': 0.23821632423088518, 'up': 0.44508230247134256} | [1.211253440823984, -0.8737389839504783, -0.3375144568735] | {'down': 0.3079639834582674, 'flat': 0.23484117966215018, 'up': 0.4571948368795824} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.3079639834582674, 'flat': 0.23484117966215018, 'up': 0.4571948368795824} | [-7.51702916372613, 9.104066275742461, -1.5870371120163262] | {'down': 0.39900464621569204, 'flat': 0.21897080854198692, 'up': 0.3820245452423211} |
| 6 | E10/causal | ['a4c806cb-22e4-5335-b2e3-2295b28333a6/1w/technical'] | {'down': 0.39900464621569204, 'flat': 0.21897080854198692, 'up': 0.3820245452423211} | [0.3595909105982342, -0.36229787808815805, 0.002706967489918277] | {'down': 0.39538166743481046, 'flat': 0.2189978782168861, 'up': 0.38562045434830344} |
| 7 | E17/scenario | ['9ed1a1e8-666c-57b2-9a54-5c82b10bb59f', '785702c3-b9dc-5d74-81be-a110835554b4', 'dcf2a31e-d9bf-5149-9ce6-2d6962bb94fc', 'a2b5737f-040f-5a4e-b47b-cb0e4616acb3'] | {'down': 0.39538166743481046, 'flat': 0.2189978782168861, 'up': 0.38562045434830344} | [0.8777455965083558, 2.382724128359631, -3.260469724867987] | {'down': 0.41920890871840677, 'flat': 0.18639318096820623, 'up': 0.394397910313387} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.41920890871840677, 'flat': 0.18639318096820623, 'up': 0.394397910313387} | [-0.8332055654003689, -1.1717432737833267, 2.0049488391836903] | {'down': 0.4074914759805735, 'flat': 0.20644266936004313, 'up': 0.3860658546593833} |
| 9 | E13/history | [] | {'down': 0.4074914759805735, 'flat': 0.20644266936004313, 'up': 0.3860658546593833} | [0.0, 0.0, 0.0] | {'down': 0.4074914759805735, 'flat': 0.20644266936004313, 'up': 0.3860658546593833} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.4074914759805735, 'flat': 0.20644266936004313, 'up': 0.3860658546593833} | [-0.5593947423197909, -0.8723655106322448, 1.4317602529520497] | {'down': 0.39876782087425106, 'flat': 0.22076027188956363, 'up': 0.3804719072361854} |
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
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1w",
      "operator": "gt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:f0c0dbc45e99da4f6dc69e51b3308397836a6d55048aa8c797553b5465cf41fe'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-18T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "a4c806cb-22e4-5335-b2e3-2295b28333a6/1m/technical",
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
    "atr": 24085.97942892576,
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
      1027,
      1034
    ],
    "bottom_score": 0.0,
    "rsi": 63.840396085983556,
    "sma": [
      196640.0,
      131914.16666666666,
      91521.25
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
      1029,
      1037
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
  },
  "primary": "1d",
  "reflexivity_effect": 0.025,
  "regime_effect": 0.0375,
  "sell_liquidity": null,
  "wave": {
    "atr": 9883.464688860755,
    "available": true,
    "bottom_confirmed": false,
    "bottom_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": true,
      "neckline": true,
      "volume": false
    },
    "bottom_neckline": 204000.0,
    "bottom_pivots": [
      4917,
      4925
    ],
    "bottom_score": 0.65,
    "rsi": 64.68247187439766,
    "sma": [
      195245.0,
      188328.33333333334,
      184442.5
    ],
    "top_confirmed": false,
    "top_features": {
      "atr": true,
      "divergence": false,
      "double": true,
      "extreme": false,
      "ma": false,
      "neckline": false,
      "volume": true
    },
    "top_neckline": 179200.0,
    "top_pivots": [
      4912,
      4922
    ],
    "top_score": 0.4,
    "volume_ratio": 1.688807602541006
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'a4c806cb-22e4-5335-b2e3-2295b28333a6/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.025, 'regime_effect': 0.0375}
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
    "hypothesis_id": "73eae710-8d33-5a14-bdb3-ba94ebbabb8e",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "73eae710-8d33-5a14-bdb3-ba94ebbabb8e",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "73eae710-8d33-5a14-bdb3-ba94ebbabb8e",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.232875
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "73eae710-8d33-5a14-bdb3-ba94ebbabb8e",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.232875
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "73eae710-8d33-5a14-bdb3-ba94ebbabb8e",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.12948168515218422
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
    "hypothesis_id": "a14b7eb0-faee-543b-abc6-a30dcfb911f2",
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
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [0.3522012398949059, -0.26476660806352137, -0.08743463183138733] | {'down': 0.34735233391936476, 'flat': 0.24912565368168613, 'up': 0.4035220123989491} |
| 1 | E12/causal | ['preferred_trend_alignment'] | {'down': 0.34735233391936476, 'flat': 0.24912565368168613, 'up': 0.4035220123989491} | [0.6356792097669373, -0.4758236342970845, -0.1598555754698472] | {'down': 0.3425940975763939, 'flat': 0.24752709792698765, 'up': 0.40987880449661845} |
| 2 | E12/causal | ['preferred_volume_z'] | {'down': 0.3425940975763939, 'flat': 0.24752709792698765, 'up': 0.40987880449661845} | [0.6383845481792161, -0.4752373066965465, -0.16314724148267234] | {'down': 0.33784172450942845, 'flat': 0.24589562551216093, 'up': 0.4162626499784106} |
| 3 | E12/causal | ['samsung_common_price'] | {'down': 0.33784172450942845, 'flat': 0.24589562551216093, 'up': 0.4162626499784106} | [0.9562055959151161, -0.7070372539531022, -0.24916834196200555] | {'down': 0.33077135196989743, 'flat': 0.24340394209254088, 'up': 0.4258247059375618} |
| 4 | E12/causal | ['samsung_preferred_price'] | {'down': 0.33077135196989743, 'flat': 0.24340394209254088, 'up': 0.4258247059375618} | [0.9610638612284395, -0.7049583797433423, -0.25610548148509715] | {'down': 0.323721768172464, 'flat': 0.2408428872776899, 'up': 0.43543534454984617} |
| 5 | E12/causal | ['us_10y_yield'] | {'down': 0.323721768172464, 'flat': 0.2408428872776899, 'up': 0.43543534454984617} | [-5.57200511430806, 6.853673840051683, -1.281668725743626] | {'down': 0.39225850657298084, 'flat': 0.22802620002025364, 'up': 0.3797152934067656} |
| 6 | E10/causal | ['a4c806cb-22e4-5335-b2e3-2295b28333a6/1m/technical'] | {'down': 0.39225850657298084, 'flat': 0.22802620002025364, 'up': 0.3797152934067656} | [1.9137431359828316, -1.9063417583261688, -0.007401377656671149] | {'down': 0.37319508898971915, 'flat': 0.22795218624368693, 'up': 0.3988527247665939} |
| 7 | E17/scenario | ['dacfd2aa-06c2-5c68-b66d-9914a5936d83', '5a96d769-e578-546a-a53b-6c65f22292dc', '97f5c9b6-87a6-501b-9f93-568ea1879a46', '6fe6a786-d2a1-5b50-b471-dca777c67797'] | {'down': 0.37319508898971915, 'flat': 0.22795218624368693, 'up': 0.3988527247665939} | [0.9835572912227863, 2.592920970622492, -3.5764782618452813] | {'down': 0.39912429869594407, 'flat': 0.19218740362523412, 'up': 0.40868829767882175} |
| 8 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.39912429869594407, 'flat': 0.19218740362523412, 'up': 0.40868829767882175} | [-1.0255328666112895, -0.8953729577271197, 1.9209058243384092] | {'down': 0.39017056911867287, 'flat': 0.2113964618686182, 'up': 0.39843296901270886} |
| 9 | E13/history | [] | {'down': 0.39017056911867287, 'flat': 0.2113964618686182, 'up': 0.39843296901270886} | [0.0, 0.0, 0.0] | {'down': 0.39017056911867287, 'flat': 0.2113964618686182, 'up': 0.39843296901270886} |
| 10 | E18/calibration | ['temperature:1.15'] | {'down': 0.39017056911867287, 'flat': 0.2113964618686182, 'up': 0.39843296901270886} | [-0.7539082626998483, -0.6335038926901904, 1.3874121553900387] | {'down': 0.38383553019177097, 'flat': 0.2252705834225186, 'up': 0.3908938863857104} |
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
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1m",
      "operator": "gt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': '0218742230039dbdd7cc2758453406833371ce5bc8f992606fbf4309e0769167'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': '0218742230039dbdd7cc2758453406833371ce5bc8f992606fbf4309e0769167'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': '0218742230039dbdd7cc2758453406833371ce5bc8f992606fbf4309e0769167'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': '0218742230039dbdd7cc2758453406833371ce5bc8f992606fbf4309e0769167'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': '0218742230039dbdd7cc2758453406833371ce5bc8f992606fbf4309e0769167'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': '0218742230039dbdd7cc2758453406833371ce5bc8f992606fbf4309e0769167'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': '0218742230039dbdd7cc2758453406833371ce5bc8f992606fbf4309e0769167'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:f0c0dbc45e99da4f6dc69e51b3308397836a6d55048aa8c797553b5465cf41fe'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_rsi_14', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_rsi_14@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_trend_alignment', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_trend_alignment@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'preferred_volume_z', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#preferred_volume_z@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:067cf6adb61ecff28f1b7aef1a7f3422f0e1fdb7c031782aad595d3db3625c97#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-06-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:79b9ebf92f6eaa9a51eaa3f27157a2bcecc365016e8b276b42f96bc1fa5df518#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:19af1f429399240d9ac6c97dc0970beda7dcd213183f5308ec93f0e73b3bd903#us_10y_yield@2026-09-18T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "a4c806cb-22e4-5335-b2e3-2295b28333a6/1y/technical",
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
    "atr": 24085.97942892576,
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
      1027,
      1034
    ],
    "bottom_score": 0.0,
    "rsi": 63.840396085983556,
    "sma": [
      196640.0,
      131914.16666666666,
      91521.25
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
      1029,
      1037
    ],
    "top_score": 0.1,
    "volume_ratio": 0.6998822366568738
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'a4c806cb-22e4-5335-b2e3-2295b28333a6/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.010000000000000002, 'regime_effect': -0.015}
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
    "hypothesis_id": "cf2c6a9e-d75c-505d-801c-8ac38f55a16f",
    "node_ids": [
      "samsung_common_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_common_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_common_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "samsung_preferred_price_to_preferred",
      "preferred_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "cf2c6a9e-d75c-505d-801c-8ac38f55a16f",
    "node_ids": [
      "samsung_preferred_price",
      "module:preferred",
      "preferred_price"
    ],
    "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
    "root_evidence_group": "samsung_preferred_price",
    "sign": 1,
    "strength": 0.2025
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_volume_z_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "cf2c6a9e-d75c-505d-801c-8ac38f55a16f",
    "node_ids": [
      "preferred_volume_z",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_volume_z",
    "sign": 1,
    "strength": 0.19035
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_trend_alignment_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "cf2c6a9e-d75c-505d-801c-8ac38f55a16f",
    "node_ids": [
      "preferred_trend_alignment",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_trend_alignment",
    "sign": 1,
    "strength": 0.19035
  },
  {
    "confidence": 0.9025,
    "edge_ids": [
      "preferred_rsi_14_to_market_regime",
      "market_regime_to_price"
    ],
    "graph_version": "fixture-dag-v1:3ca2d9a63eb0247663b7f4e2adfcf82a1fe417700ac723222b7b2ae126f096e6",
    "hypothesis_id": "cf2c6a9e-d75c-505d-801c-8ac38f55a16f",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": 1,
    "strength": 0.08695668515218423
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
    "hypothesis_id": "fb0e16b8-decb-5104-a4c3-c1c95c8f69da",
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
        "samsung_common_price"
      ],
      "factor_id": "samsung_common_price",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 65000.0,
      "unit": "krw_per_share"
    },
    {
      "evidence_refs": [
        "samsung_preferred_price"
      ],
      "factor_id": "samsung_preferred_price",
      "horizon": "1y",
      "operator": "gt",
      "threshold": 52000.0,
      "unit": "krw_per_share"
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
