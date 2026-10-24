# Published frozen prediction

This is a copy of the sealed public system output. Unavailable reversal scores are not measured zero probabilities. Raw captures, human forecasts and outer shadow records are kept local.

# live-forward-v2 — sealed forward evidence

Run: e22c7027-9bf8-5005-8db9-0243bb9420fd
Cutoff / prediction: 2026-10-23T22:22:21.113905+00:00
Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0
P0: {'definition': 'last eligible completed close, not execution quote', 'effective_at': '2026-10-23T06:30:00+00:00', 'source_refs': ['raw:b4736274f5402a044e25347d4ae5d7764b63232384ebb26930bb8fa460da274b'], 'timeframe': '30m', 'unit': 'krw_per_share', 'value': 167900.0}

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment bull/bear | Liquidity buy/sell | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1w | 39.5500% | 38.9711% | 21.4789% | 6.3480% | 10.0000% | 0.0000% | 0.0/0.4 | None/None | WAIT |
| 1m | 39.9077% | 38.1610% | 21.9313% | 3.1912% | 0.0000% | 0.0000% | 0.26666666666666666/0.13333333333333336 | None/None | WAIT |
| 1y | — | — | — | — | 0.0000% | 40.0000% | 0.4/0.0 | None/None | WAIT |

## Feedback probability (Up / Down / Flat)
| Horizon | Before | After | Delta pp |
|---|---|---|---|
| 1w | 39.0998% / 39.4568% / 21.4435% | 39.5500% / 38.9711% / 21.4789% | [0.45023520419178453, -0.4856732090861571, 0.03543800489436699] |
| 1m | 39.9077% / 38.1610% / 21.9313% | 39.9077% / 38.1610% / 21.9313% | [0.0, 0.0, 0.0] |
| 1y | insufficient_evidence | insufficient_evidence | None |

## Sources / freshness
```json
[
  {
    "age_hours": 15.872531640277778,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-23T22:22:20.473475Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 0,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "b4736274f5402a044e25347d4ae5d7764b63232384ebb26930bb8fa460da274b",
    "reason": null,
    "released_at": null,
    "rows": 217,
    "source_id": "preferred_30m",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.872531640277778,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-23T22:22:20.721306Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 4,
      "off_grid": 0
    },
    "instrument": "005935.KS",
    "latest_effective_at": "2026-10-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4",
    "reason": null,
    "released_at": null,
    "rows": 4933,
    "source_id": "preferred_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 15.872531640277778,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-23T22:22:20.778621Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 2,
      "off_grid": 0
    },
    "instrument": "005930.KS",
    "latest_effective_at": "2026-10-23T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add",
    "reason": null,
    "released_at": null,
    "rows": 4935,
    "source_id": "common_daily",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": 2.872531640277778,
    "authority": "official_original",
    "collected_at": "2026-10-23T22:22:20.608172Z",
    "excluded": {},
    "instrument": "daily_par_yield_10y",
    "latest_effective_at": "2026-10-23T19:30:00Z",
    "provider": "US Treasury",
    "raw_sha256": "205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97",
    "reason": null,
    "released_at": null,
    "rows": 204,
    "source_id": "treasury_10y",
    "status": "fresh",
    "used_by_model": true
  },
  {
    "age_hours": null,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-23T22:22:20.860086Z",
    "excluded": {},
    "instrument": "KRW=X",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "beb5d275f47d5d50ec94cccb06d8bc19c375d62259231f2b618ebfe9eecc86ca",
    "reason": "unverified_FX_daily_window_not_US_cash_session",
    "released_at": null,
    "rows": 0,
    "source_id": "usdkrw",
    "status": "unavailable",
    "used_by_model": false
  },
  {
    "age_hours": 39.87253164027778,
    "authority": "public_vendor_fallback",
    "collected_at": "2026-10-23T22:22:21.034521Z",
    "excluded": {
      "incomplete": 0,
      "invalid": 1,
      "off_grid": 0
    },
    "instrument": "%5EKS11",
    "latest_effective_at": "2026-10-22T06:30:00Z",
    "provider": "Yahoo Finance",
    "raw_sha256": "c511172fc8bedda98455ed35cfecfe42a76e418790c70c20c5ffac7daff57ed9",
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
    "collected_at": "2026-10-23T22:22:21.113905Z",
    "excluded": {},
    "instrument": "DX-Y.NYB",
    "latest_effective_at": null,
    "provider": "Yahoo Finance",
    "raw_sha256": "e5690db895e1a55a82ab83cf685e5c3a005ca61f36e7dd47ec84e3e564965928",
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
    "collected_at": "2026-10-23T22:22:20.779164Z",
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
    "collected_at": "2026-10-23T22:22:20.779164Z",
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
    "collected_at": "2026-10-23T22:22:20.779164Z",
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
    "collected_at": "2026-10-23T22:22:20.779164Z",
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
Bar boundaries: {'1d': {'count': 4933, 'last': '2026-10-23T06:30:00+00:00'}, '1mo': {'count': 239, 'last': '2026-09-30T14:59:59+00:00'}, '1w': {'count': 1043, 'last': '2026-10-23T06:30:00+00:00'}, '30m': {'count': 217, 'last': '2026-10-23T06:30:00+00:00'}}
Raw Observation timestamps, released_at (null when unknown), effective_at, collected_at and prior references are retained in the immutable journal.

## 1w
Eligibility: True; reasons: []
Coverage: {'ai_demand': 0.0, 'earnings': 0.5, 'flow': 0.0, 'macro': 0.5, 'memory': 0.31666666666666665, 'price_regime': 1.0, 'supply': 0.0, 'valuation': 0.0}; confidence multiplier: 0.405
Confidence-lowering Strong Evidence: ['foreign_net_buy', 'institution_net_buy', 'usdkrw']
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c511172fc8bedda98455ed35cfecfe42a76e418790c70c20c5ffac7daff57ed9'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-16T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 30m/1d
```json
{
  "batch_id": "e22c7027-9bf8-5005-8db9-0243bb9420fd/1w/technical",
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
    "atr": 10686.893255585524,
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
    "rsi": 40.21350302943155,
    "sma": [
      186920.0,
      186470.0,
      190947.5
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
      4914,
      4930
    ],
    "top_score": 0.0,
    "volume_ratio": 0.5649990848845862
  },
  "primary": "30m",
  "reflexivity_effect": 0.010000000000000002,
  "regime_effect": 0.015,
  "sell_liquidity": null,
  "wave": {
    "atr": 1980.7625138467913,
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
    "bottom_neckline": 174800.0,
    "bottom_pivots": [
      188,
      208
    ],
    "bottom_score": 0.1,
    "rsi": 55.00722449127959,
    "sma": [
      165365.0,
      168513.33333333334,
      170749.16666666666
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
    "top_neckline": 159000.0,
    "top_pivots": [
      193,
      206
    ],
    "top_score": 0.0,
    "volume_ratio": 0.0
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'e22c7027-9bf8-5005-8db9-0243bb9420fd/1w/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.010000000000000002, 'regime_effect': 0.015}
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
    "hypothesis_id": "41f00074-3ea2-5bc5-a948-b121aa8edf17",
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
    "hypothesis_id": "41f00074-3ea2-5bc5-a948-b121aa8edf17",
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
    "hypothesis_id": "968c929f-835b-5627-a6cf-9bb171b112b3",
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
    "hypothesis_id": "968c929f-835b-5627-a6cf-9bb171b112b3",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2277854182053482
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-1.2235416859382564, 1.5356833025769956, -0.3121416166387253] | {'down': 0.36535683302576993, 'flat': 0.24687858383361275, 'up': 0.38776458314061746} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.36535683302576993, 'flat': 0.24687858383361275, 'up': 0.38776458314061746} | [4.762804883957189, -3.5909396587452793, -1.171865225211921] | {'down': 0.32944743643831714, 'flat': 0.23515993158149354, 'up': 0.43539263198018935} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.32944743643831714, 'flat': 0.23515993158149354, 'up': 0.43539263198018935} | [4.866860307656634, -3.5302535229626955, -1.336606784693939] | {'down': 0.2941449012086902, 'flat': 0.22179386373455415, 'up': 0.4840612350567557} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.2941449012086902, 'flat': 0.22179386373455415, 'up': 0.4840612350567557} | [-7.6481498412275695, 8.988202714000765, -1.3400528727732008] | {'down': 0.38402692834869784, 'flat': 0.20839333500682214, 'up': 0.40757973664448} |
| 4 | E10/causal | ['e22c7027-9bf8-5005-8db9-0243bb9420fd/1w/technical'] | {'down': 0.38402692834869784, 'flat': 0.20839333500682214, 'up': 0.40757973664448} | [0.024919404675616263, -0.024608863268849035, -0.0003105414067672285] | {'down': 0.38378083971600935, 'flat': 0.20839022959275447, 'up': 0.40782893069123616} |
| 5 | E17/scenario | ['d754a613-cbf1-5721-821e-5ab428d2bf43', '5a8c97be-7fcd-5e26-ae46-1ba4f5fa4aea', 'e924b731-a0a2-5d48-91f7-4bbedeb131b2', '4d3d27fd-a901-50c4-88fc-5e24e6dca8e7'] | {'down': 0.38378083971600935, 'flat': 0.20839022959275447, 'up': 0.40782893069123616} | [0.575154655265181, 2.203367671931411, -2.778522327196589] | {'down': 0.40581451643532346, 'flat': 0.18060500632078857, 'up': 0.41358047724388797} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.40581451643532346, 'flat': 0.18060500632078857, 'up': 0.41358047724388797} | [-1.0150382437857097, -0.9168073680648203, 1.93184561185053] | {'down': 0.39664644275467525, 'flat': 0.19992346243929388, 'up': 0.40343009480603087} |
| 7 | E13/history | [] | {'down': 0.39664644275467525, 'flat': 0.19992346243929388, 'up': 0.40343009480603087} | [0.0, 0.0, 0.0] | {'down': 0.39664644275467525, 'flat': 0.19992346243929388, 'up': 0.40343009480603087} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.39664644275467525, 'flat': 0.19992346243929388, 'up': 0.40343009480603087} | [-0.7930008115170473, -0.693561605303139, 1.486562416820178] | {'down': 0.38971082670164386, 'flat': 0.21478908660749566, 'up': 0.3955000866908604} |
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
Unmapped/conflicting evidence: [{'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c511172fc8bedda98455ed35cfecfe42a76e418790c70c20c5ffac7daff57ed9'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-16T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1d/1w
```json
{
  "batch_id": "e22c7027-9bf8-5005-8db9-0243bb9420fd/1m/technical",
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
    "atr": 24001.64406678333,
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
    "rsi": 46.03053508942934,
    "sma": [
      194125.0,
      140224.16666666666,
      95441.25
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
      1033,
      1038
    ],
    "top_score": 0.4,
    "volume_ratio": 0.7441564963793168
  },
  "primary": "1d",
  "reflexivity_effect": 0.0,
  "regime_effect": 0.0,
  "sell_liquidity": null,
  "wave": {
    "atr": 10686.893255585524,
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
    "rsi": 40.21350302943155,
    "sma": [
      186920.0,
      186470.0,
      190947.5
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
      4914,
      4930
    ],
    "top_score": 0.0,
    "volume_ratio": 0.5649990848845862
  }
}
```
Passed gates: ['meta_check']; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity']
Feedback applied once: {'batch_id': 'e22c7027-9bf8-5005-8db9-0243bb9420fd/1m/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': 0.0, 'regime_effect': 0.0}
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
    "hypothesis_id": "a63bf526-de93-570e-ae4e-88b6dab81a54",
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
    "hypothesis_id": "a63bf526-de93-570e-ae4e-88b6dab81a54",
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
    "hypothesis_id": "6798664e-d4d5-5537-ad55-73e4ace63376",
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
    "hypothesis_id": "6798664e-d4d5-5537-ad55-73e4ace63376",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.2642354182053482
  }
]
```

### Probability contribution reconstruction
Prior: {'down': 0.35, 'flat': 0.25, 'up': 0.4}
| Sequence | Engine/stage | Evidence | Before | Delta pp | After |
|---|---|---|---|---|---|
| 0 | E12/causal | ['preferred_rsi_14'] | {'down': 0.35, 'flat': 0.25, 'up': 0.4} | [-0.5514033049223599, 0.6893822074655054, -0.13797890254314826] | {'down': 0.35689382207465503, 'flat': 0.24862021097456852, 'up': 0.3944859669507764} |
| 1 | E12/causal | ['samsung_common_price'] | {'down': 0.35689382207465503, 'flat': 0.24862021097456852, 'up': 0.3944859669507764} | [3.8104264784704744, -2.850455802103935, -0.9599706763665367] | {'down': 0.3283892640536157, 'flat': 0.23902050421090315, 'up': 0.43259023173548117} |
| 2 | E12/causal | ['samsung_preferred_price'] | {'down': 0.3283892640536157, 'flat': 0.23902050421090315, 'up': 0.43259023173548117} | [3.880193905745349, -2.812795238590593, -1.067398667154762] | {'down': 0.30026131166770975, 'flat': 0.22834651753935553, 'up': 0.47139217079293466} |
| 3 | E12/causal | ['us_10y_yield'] | {'down': 0.30026131166770975, 'flat': 0.22834651753935553, 'up': 0.47139217079293466} | [-5.662854761371117, 6.683813299084856, -1.020958537713748] | {'down': 0.3670994446585583, 'flat': 0.21813693216221805, 'up': 0.4147636231792235} |
| 4 | E10/causal | ['e22c7027-9bf8-5005-8db9-0243bb9420fd/1m/technical'] | {'down': 0.3670994446585583, 'flat': 0.21813693216221805, 'up': 0.4147636231792235} | [-0.42918840646288814, 0.4188857280908398, 0.010302678372065] | {'down': 0.3712883019394667, 'flat': 0.2182399589459387, 'up': 0.4104717391145946} |
| 5 | E17/scenario | ['e72e2c7d-d23b-5b32-b895-774b1527f612', '24d27c79-af8d-58e9-8294-8cbe497b61a5', '1dd52d23-dfb7-5c34-a254-d66f80e91b9a', 'cb99f946-2f45-583c-aac8-62f39e8505cb'] | {'down': 0.3712883019394667, 'flat': 0.2182399589459387, 'up': 0.4104717391145946} | [0.8156938661705748, 2.390698830741056, -3.206392696911642] | {'down': 0.3951952902468773, 'flat': 0.18617603197682228, 'up': 0.41862867777630036} |
| 6 | E14/challenge | ['bearish_counterevidence', 'bullish_counterevidence'] | {'down': 0.3951952902468773, 'flat': 0.18617603197682228, 'up': 0.41862867777630036} | [-1.082915190560052, -0.7854033921422532, 1.8683185827023163] | {'down': 0.38734125632545474, 'flat': 0.20485921780384544, 'up': 0.40779952587069984} |
| 7 | E13/history | [] | {'down': 0.38734125632545474, 'flat': 0.20485921780384544, 'up': 0.40779952587069984} | [0.0, 0.0, 0.0] | {'down': 0.38734125632545474, 'flat': 0.20485921780384544, 'up': 0.40779952587069984} |
| 8 | E18/calibration | ['temperature:1.15'] | {'down': 0.38734125632545474, 'flat': 0.20485921780384544, 'up': 0.40779952587069984} | [-0.8722378047044677, -0.5731470125168392, 1.4453848172213095] | {'down': 0.38160978620028635, 'flat': 0.21931306597605854, 'up': 0.39907714782365517} |
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
Unmapped/conflicting evidence: [{'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr3_4gb_512mx8_1600_1866', 'source_ref': 'eaceac9a671be709d6717a0cbdbdcb8f0e30fa5560e9ad0fd2a47d42a91f6d94'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_3200', 'source_ref': 'eaceac9a671be709d6717a0cbdbdcb8f0e30fa5560e9ad0fd2a47d42a91f6d94'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_16gb_2gx8_ett', 'source_ref': 'eaceac9a671be709d6717a0cbdbdcb8f0e30fa5560e9ad0fd2a47d42a91f6d94'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_3200', 'source_ref': 'eaceac9a671be709d6717a0cbdbdcb8f0e30fa5560e9ad0fd2a47d42a91f6d94'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr4_8gb_1gx8_ett', 'source_ref': 'eaceac9a671be709d6717a0cbdbdcb8f0e30fa5560e9ad0fd2a47d42a91f6d94'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_4800_5600', 'source_ref': 'eaceac9a671be709d6717a0cbdbdcb8f0e30fa5560e9ad0fd2a47d42a91f6d94'}, {'reason': 'horizon_excluded', 'source_field': 'dram_spot_ddr5_16gb_2gx8_ett', 'source_ref': 'eaceac9a671be709d6717a0cbdbdcb8f0e30fa5560e9ad0fd2a47d42a91f6d94'}, {'reason': 'no_mapping_rule', 'source_field': 'kospi', 'source_ref': 'raw:c511172fc8bedda98455ed35cfecfe42a76e418790c70c20c5ffac7daff57ed9'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_common_price', 'source_ref': 'raw:60abbefb1300c32591d7d6e84428bbad1fe0555beab1117c4d0062964fc29add#samsung_common_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-07-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-05T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-20T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-24T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-25T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-26T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-27T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-08-31T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-03T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-04T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-09T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-10T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-11T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-17T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-18T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-21T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-22T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-23T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-28T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-29T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-09-30T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-01T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-02T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-06T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-07T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-08T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-12T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-13T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-14T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-15T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-16T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'samsung_preferred_price', 'source_ref': 'raw:35ccf73fc6ef0eb1584354c486efed04fab78381bc631818821e467dcf8850a4#samsung_preferred_price@2026-10-19T06:30:00+00:00'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': '2a766cbca78a04908254a94ee6db4cf399c87075227841ace5b04a4c4bcf2096'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'c0c0939e7fa7cef27e9ebaee19f0d1873779f63927237d87957de1d2418a2931'}, {'reason': 'stale', 'source_field': 'semiconductor_export_demand', 'source_ref': 'ecac01fbf10a876e4595fa8f50f574f6a2b810e3e022854ac1815d75c6ad3767'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-07T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-08T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-14T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-15T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-16T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-21T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-22T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-28T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-29T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-01-30T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-09T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-10T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-11T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-12T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-13T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-17T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-18T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-19T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-20T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-23T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-24T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-25T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-26T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-02-27T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-02T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-03T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-04T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-05T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-06T20:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-03-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-04-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-05-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-06-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-07-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-12T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-19T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-20T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-26T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-27T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-08-31T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-03T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-04T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-10T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-11T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-16T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-17T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-18T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-21T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-22T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-23T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-24T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-25T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-28T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-29T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-09-30T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-01T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-02T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-05T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-06T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-07T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-08T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-09T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-13T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-14T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-15T19:30:00+00:00'}, {'reason': 'stale', 'source_field': 'us_10y_yield', 'source_ref': 'raw:205d5b564c19eca524fa83485a2aeabe52c2f195ab807e48f847fbe9df217a97#us_10y_yield@2026-10-16T19:30:00+00:00'}]
E11: company=passed, memory=non_applicable, industry=non_applicable
Primary/context: 1w/1mo
```json
{
  "batch_id": "e22c7027-9bf8-5005-8db9-0243bb9420fd/1y/technical",
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
  "reflexivity_effect": -0.04000000000000001,
  "regime_effect": -0.06,
  "sell_liquidity": null,
  "wave": {
    "atr": 24001.64406678333,
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
    "rsi": 46.03053508942934,
    "sma": [
      194125.0,
      140224.16666666666,
      95441.25
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
      1033,
      1038
    ],
    "top_score": 0.4,
    "volume_ratio": 0.7441564963793168
  }
}
```
Passed gates: []; failed gates: ['future_up', 'without_history_up', 'confidence', 'bottom_timing', 'alignment', 'liquidity', 'meta_check']
Feedback applied once: {'batch_id': 'e22c7027-9bf8-5005-8db9-0243bb9420fd/1y/technical', 'flow_applied': False, 'flow_effect': 0.0, 'reflexivity_effect': -0.04000000000000001, 'regime_effect': -0.06}
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
    "hypothesis_id": "8517e8d5-0b33-52b7-b806-b63d340c1551",
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
    "hypothesis_id": "8517e8d5-0b33-52b7-b806-b63d340c1551",
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
    "hypothesis_id": "abc3afe8-5f6e-5bae-b31a-cfc954e3be71",
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
    "hypothesis_id": "abc3afe8-5f6e-5bae-b31a-cfc954e3be71",
    "node_ids": [
      "preferred_rsi_14",
      "module:market_regime",
      "preferred_price"
    ],
    "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
    "root_evidence_group": "preferred_rsi_14",
    "sign": -1,
    "strength": 0.41003541820534817
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
