# First live forward evidence
Prediction timestamp: 2026-09-09T05:51:04.715969+00:00
Data cutoff: 2026-09-09T05:51:04.715969+00:00
Data mode: live_forward
Run ID: 427e887c-48e2-5b7f-af46-e64e621d6be8
Raw snapshot hash: e8794c232727717feef50b95d845943b94788ce685ecac7521a43210b72be3c3
Core algorithms frozen: {'engines.py': '74949c6bbbfcdc335f0f3b6a643672c62a8f6aa1a943a4636137a6420daa0d18', 'technical.py': '1514bb5dd637b20158cd2d3784d8967d627003ede431fd5a16fef306b8819f30', 'decision.py': '63c5b4a3193481e0d863f3122ebe8fc20543ef0e759bd35ad5ecac9d5664bb34'}

## Sources
| Source | Provider/authority | Status | Effective | Collected | Age hours | Rows | Model use |
|---|---|---|---|---|---:|---:|---|
| preferred_30m | Yahoo Finance/public_vendor_fallback | fresh | 2026-09-09 05:30:00+00:00 | 2026-09-09 05:51:03.751683+00:00 | 0.3513099913888889 | 263 | True |
| preferred_daily | Yahoo Finance/public_vendor_fallback | fresh | 2026-09-08 06:30:00+00:00 | 2026-09-09 05:51:04.650355+00:00 | 23.351309991388888 | 4931 | True |
| common_daily | Yahoo Finance/public_vendor_fallback | fresh | 2026-09-08 06:30:00+00:00 | 2026-09-09 05:51:04.158652+00:00 | 23.351309991388888 | 4933 | True |
| treasury_10y | US Treasury/official_original | fresh | 2026-09-09 03:59:59+00:00 | 2026-09-09 05:51:03.781911+00:00 | 1.8515877691666667 | 172 | True |
| usdkrw | Yahoo Finance/public_vendor_fallback | fresh | 2026-09-08 22:59:59+00:00 | 2026-09-09 05:51:04.326133+00:00 | 6.851587769166667 | 218 | True |
| kospi | Yahoo Finance/public_vendor_fallback | fresh | 2026-09-08 06:30:00+00:00 | 2026-09-09 05:51:04.327131+00:00 | 23.351309991388888 | 243 | False |
| dxy | Yahoo Finance/public_vendor_fallback | fresh | 2026-09-09 03:59:59+00:00 | 2026-09-09 05:51:04.715969+00:00 | 1.8515877691666667 | 251 | False |
| foreign_net_buy | not_connected/unavailable | unavailable | None | 2026-09-09 05:51:04.326133+00:00 | None | 0 | False |
| institution_net_buy | not_connected/unavailable | unavailable | None | 2026-09-09 05:51:04.326133+00:00 | None | 0 | False |
| program_net_buy | not_connected/unavailable | unavailable | None | 2026-09-09 05:51:04.326133+00:00 | None | 0 | False |
| dram_contract_asp | not_connected/unavailable | unavailable | None | 2026-09-09 05:51:04.326133+00:00 | None | 0 | False |

Released-at is unknown unless supplied explicitly; collection time is the conservative known-at bound.
Missing factors from E01: hyperscaler_capex, gpu_demand_growth, dram_contract_asp, hbm_demand, cxmt_memory_capacity, samsung_eps, samsung_eps_revision, foreign_net_buy, institution_net_buy, program_net_buy, semiconductor_relative_flow, samsung_forward_per, equity_discount_rate
Conflicting factors: ()
E01 coverage: 35.0%. Existing E06/E14 confidence penalties retained.
KOSPI/DXY are captured context feeds; no invented causal edges were added to the frozen model.
Accounting and event/consensus evidence are unavailable, not synthetic. E11 identities are not reported as passed.

## Horizon 1w
Before feedback: null / insufficient_evidence
After feedback: null / insufficient_evidence
Confidence: null; no publishable forecast
Feedback passes: 1; Regime/Flow/Actor interpretation consumes technical evidence.
Wave primary/context: 30m/1d
Bottom/Top reversal score: 0.0/0.2; calibrated probability: unavailable.
Bottom/Top confirmed: False/False
Bottom features: {'double': False, 'divergence': False, 'extreme': False, 'volume': False, 'atr': False, 'neckline': False, 'ma': False}
Top features: {'double': False, 'divergence': False, 'extreme': True, 'volume': True, 'atr': False, 'neckline': False, 'ma': False}
Alignment bullish/bearish: 0.4/0.0
Liquidity buy/sell: None/None
Final decision: WAIT
Failed gates: future_up, without_history_up, confidence, bottom_timing, alignment, liquidity, meta_check
Passed ENTRY gates: 

Positive drivers (up to 5)
- samsung_common_price_to_preferred/preferred_to_price; sign=1, strength=0.810000, confidence=0.902500, root=samsung_common_price
- samsung_preferred_price_to_preferred/preferred_to_price; sign=1, strength=0.810000, confidence=0.902500, root=samsung_preferred_price
- preferred_trend_alignment_to_market_regime/market_regime_to_price; sign=1, strength=0.785700, confidence=0.902500, root=preferred_trend_alignment
- preferred_rsi_14_to_market_regime/market_regime_to_price; sign=1, strength=0.117986, confidence=0.902500, root=preferred_rsi_14
- usdkrw_to_macro/macro_to_price; sign=1, strength=0.034722, confidence=0.902500, root=usdkrw

Negative drivers (up to 5)
- us_10y_yield_to_macro/macro_to_price; sign=-1, strength=0.648000, confidence=0.902500, root=us_10y_yield
- preferred_volume_z_to_market_regime/market_regime_to_price; sign=-1, strength=0.129088, confidence=0.902500, root=preferred_volume_z

### Probability contribution ledger
No numeric final probability or delta exists: critical input is missing. Prior is not relabeled as a forecast. Causal effects remain inspectable below.

### E09 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E09",
  "items": [
    {
      "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
      "original_effect": 0.10648274527906856,
      "adjusted_effect": 0.10648274527906856,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_rsi_14"
    },
    {
      "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
      "original_effect": 0.70909425,
      "adjusted_effect": 0.70909425,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_trend_alignment"
    },
    {
      "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
      "original_effect": -0.11650152041926994,
      "adjusted_effect": -0.11650152041926994,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_volume_z"
    },
    {
      "path_id": "samsung_common_price_to_preferred/preferred_to_price",
      "original_effect": 0.731025,
      "adjusted_effect": 0.731025,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "samsung_common_price"
    },
    {
      "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
      "original_effect": 0.731025,
      "adjusted_effect": 0.731025,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "samsung_preferred_price"
    },
    {
      "path_id": "us_10y_yield_to_macro/macro_to_price",
      "original_effect": -0.5848199999999999,
      "adjusted_effect": -0.5848199999999999,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "us_10y_yield"
    },
    {
      "path_id": "usdkrw_to_macro/macro_to_price",
      "original_effect": 0.03133686676025391,
      "adjusted_effect": 0.03133686676025391,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "usdkrw"
    }
  ]
}
```

### E12 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E12",
  "items": [
    {
      "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
      "horizon": "1w",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.006388964716744113
    },
    {
      "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
      "horizon": "1w",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.042545654999999995
    },
    {
      "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
      "horizon": "1w",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": -0.006990091225156196
    },
    {
      "path_id": "samsung_common_price_to_preferred/preferred_to_price",
      "horizon": "1w",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.03655125
    },
    {
      "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
      "horizon": "1w",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.03655125
    },
    {
      "path_id": "us_10y_yield_to_macro/macro_to_price",
      "horizon": "1w",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": -0.05848199999999999
    },
    {
      "path_id": "usdkrw_to_macro/macro_to_price",
      "horizon": "1w",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.0031336866760253916
    }
  ]
}
```

### E13 structured reasoning
```json
{
  "applicable": false,
  "reason": "No mature same-regime analogy above similarity gate",
  "kind": "E13",
  "case_ids": [],
  "similarity": null,
  "recency": null,
  "sample_count": 0,
  "regime_match": false,
  "relevance": 0.0,
  "capped_delta": [
    0.0,
    0.0,
    0.0
  ]
}
```

### E19 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E19",
  "publishable": false,
  "failed_checks": [
    "missing_forecast",
    "fatal_challenge"
  ],
  "offending_engines": [
    "E18",
    "E14"
  ],
  "driver_refs": [
    "us_10y_yield_to_macro/macro_to_price",
    "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "samsung_common_price_to_preferred/preferred_to_price",
    "samsung_preferred_price_to_preferred/preferred_to_price",
    "preferred_volume_z_to_market_regime/market_regime_to_price"
  ],
  "falsifiers": [],
  "error_class": "insufficient_evidence"
}
```

### What Would Change My Mind
Supply genuine critical DRAM evidence and missing flow/accounting sources, then create a NEW forward prediction. Do not edit this one.
- up: usdkrw gt 1350.0 krw_per_usd
- up: samsung_common_price lt 65000.0 krw_per_share
- up: samsung_preferred_price lt 52000.0 krw_per_share
- down: us_10y_yield lt 4.0 percent
- down: preferred_volume_z gt 0.0 z_score

## Horizon 1m
Before feedback: null / insufficient_evidence
After feedback: null / insufficient_evidence
Confidence: null; no publishable forecast
Feedback passes: 1; Regime/Flow/Actor interpretation consumes technical evidence.
Wave primary/context: 1d/1w
Bottom/Top reversal score: 0.45000000000000007/0.2; calibrated probability: unavailable.
Bottom/Top confirmed: False/False
Bottom features: {'double': True, 'divergence': False, 'extreme': False, 'volume': False, 'atr': True, 'neckline': False, 'ma': True}
Top features: {'double': True, 'divergence': False, 'extreme': False, 'volume': False, 'atr': False, 'neckline': False, 'ma': False}
Alignment bullish/bearish: 0.4/0.0
Liquidity buy/sell: None/None
Final decision: WAIT
Failed gates: future_up, without_history_up, confidence, bottom_timing, alignment, liquidity, meta_check
Passed ENTRY gates: 

Positive drivers (up to 5)
- samsung_common_price_to_preferred/preferred_to_price; sign=1, strength=0.810000, confidence=0.902500, root=samsung_common_price
- samsung_preferred_price_to_preferred/preferred_to_price; sign=1, strength=0.810000, confidence=0.902500, root=samsung_preferred_price
- preferred_trend_alignment_to_market_regime/market_regime_to_price; sign=1, strength=0.810000, confidence=0.902500, root=preferred_trend_alignment
- preferred_rsi_14_to_market_regime/market_regime_to_price; sign=1, strength=0.172661, confidence=0.902500, root=preferred_rsi_14
- usdkrw_to_macro/macro_to_price; sign=1, strength=0.034722, confidence=0.902500, root=usdkrw

Negative drivers (up to 5)
- us_10y_yield_to_macro/macro_to_price; sign=-1, strength=0.648000, confidence=0.902500, root=us_10y_yield
- preferred_volume_z_to_market_regime/market_regime_to_price; sign=-1, strength=0.074413, confidence=0.902500, root=preferred_volume_z

### Probability contribution ledger
No numeric final probability or delta exists: critical input is missing. Prior is not relabeled as a forecast. Causal effects remain inspectable below.

### E09 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E09",
  "items": [
    {
      "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
      "original_effect": 0.15582693277906856,
      "adjusted_effect": 0.15582693277906856,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_rsi_14"
    },
    {
      "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
      "original_effect": 0.731025,
      "adjusted_effect": 0.731025,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_trend_alignment"
    },
    {
      "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
      "original_effect": -0.06715733291926992,
      "adjusted_effect": -0.06715733291926992,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_volume_z"
    },
    {
      "path_id": "samsung_common_price_to_preferred/preferred_to_price",
      "original_effect": 0.731025,
      "adjusted_effect": 0.731025,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "samsung_common_price"
    },
    {
      "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
      "original_effect": 0.731025,
      "adjusted_effect": 0.731025,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "samsung_preferred_price"
    },
    {
      "path_id": "us_10y_yield_to_macro/macro_to_price",
      "original_effect": -0.5848199999999999,
      "adjusted_effect": -0.5848199999999999,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "us_10y_yield"
    },
    {
      "path_id": "usdkrw_to_macro/macro_to_price",
      "original_effect": 0.03133686676025391,
      "adjusted_effect": 0.03133686676025391,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "usdkrw"
    }
  ]
}
```

### E12 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E12",
  "items": [
    {
      "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
      "horizon": "1m",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.0036359617648449335
    },
    {
      "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
      "horizon": "1m",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.017057250000000003
    },
    {
      "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
      "horizon": "1m",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": -0.0015670044347829652
    },
    {
      "path_id": "samsung_common_price_to_preferred/preferred_to_price",
      "horizon": "1m",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.029241000000000003
    },
    {
      "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
      "horizon": "1m",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.029241000000000003
    },
    {
      "path_id": "us_10y_yield_to_macro/macro_to_price",
      "horizon": "1m",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": -0.04386149999999999
    },
    {
      "path_id": "usdkrw_to_macro/macro_to_price",
      "horizon": "1m",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 1.0,
      "effect": 0.0023502650070190436
    }
  ]
}
```

### E13 structured reasoning
```json
{
  "applicable": false,
  "reason": "No mature same-regime analogy above similarity gate",
  "kind": "E13",
  "case_ids": [],
  "similarity": null,
  "recency": null,
  "sample_count": 0,
  "regime_match": false,
  "relevance": 0.0,
  "capped_delta": [
    0.0,
    0.0,
    0.0
  ]
}
```

### E19 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E19",
  "publishable": false,
  "failed_checks": [
    "missing_forecast",
    "fatal_challenge"
  ],
  "offending_engines": [
    "E18",
    "E14"
  ],
  "driver_refs": [
    "us_10y_yield_to_macro/macro_to_price",
    "samsung_common_price_to_preferred/preferred_to_price",
    "samsung_preferred_price_to_preferred/preferred_to_price",
    "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "preferred_rsi_14_to_market_regime/market_regime_to_price"
  ],
  "falsifiers": [],
  "error_class": "insufficient_evidence"
}
```

### What Would Change My Mind
Supply genuine critical DRAM evidence and missing flow/accounting sources, then create a NEW forward prediction. Do not edit this one.
- up: usdkrw gt 1350.0 krw_per_usd
- up: samsung_common_price lt 65000.0 krw_per_share
- up: samsung_preferred_price lt 52000.0 krw_per_share
- down: us_10y_yield lt 4.0 percent
- down: preferred_volume_z gt 0.0 z_score

## Horizon 1y
Before feedback: null / insufficient_evidence
After feedback: null / insufficient_evidence
Confidence: null; no publishable forecast
Feedback passes: 1; Regime/Flow/Actor interpretation consumes technical evidence.
Wave primary/context: 1w/1mo
Bottom/Top reversal score: 0.0/0.1; calibrated probability: unavailable.
Bottom/Top confirmed: False/False
Bottom features: {'double': False, 'divergence': False, 'extreme': False, 'volume': False, 'atr': False, 'neckline': False, 'ma': False}
Top features: {'double': False, 'divergence': False, 'extreme': True, 'volume': False, 'atr': False, 'neckline': False, 'ma': False}
Alignment bullish/bearish: 0.4/0.0
Liquidity buy/sell: None/None
Final decision: WAIT
Failed gates: future_up, without_history_up, confidence, bottom_timing, alignment, liquidity, meta_check
Passed ENTRY gates: 

Positive drivers (up to 5)
- samsung_common_price_to_preferred/preferred_to_price; sign=1, strength=0.810000, confidence=0.902500, root=samsung_common_price
- samsung_preferred_price_to_preferred/preferred_to_price; sign=1, strength=0.810000, confidence=0.902500, root=samsung_preferred_price
- preferred_trend_alignment_to_market_regime/market_regime_to_price; sign=1, strength=0.797850, confidence=0.902500, root=preferred_trend_alignment
- preferred_rsi_14_to_market_regime/market_regime_to_price; sign=1, strength=0.130136, confidence=0.902500, root=preferred_rsi_14
- usdkrw_to_macro/macro_to_price; sign=1, strength=0.034722, confidence=0.902500, root=usdkrw

Negative drivers (up to 5)
- us_10y_yield_to_macro/macro_to_price; sign=-1, strength=0.648000, confidence=0.902500, root=us_10y_yield
- preferred_volume_z_to_market_regime/market_regime_to_price; sign=-1, strength=0.116938, confidence=0.902500, root=preferred_volume_z

### Probability contribution ledger
No numeric final probability or delta exists: critical input is missing. Prior is not relabeled as a forecast. Causal effects remain inspectable below.

### E09 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E09",
  "items": [
    {
      "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
      "original_effect": 0.11744812027906856,
      "adjusted_effect": 0.11744812027906856,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_rsi_14"
    },
    {
      "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
      "original_effect": 0.720059625,
      "adjusted_effect": 0.720059625,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_trend_alignment"
    },
    {
      "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
      "original_effect": -0.10553614541926994,
      "adjusted_effect": -0.10553614541926994,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "preferred_volume_z"
    },
    {
      "path_id": "samsung_common_price_to_preferred/preferred_to_price",
      "original_effect": 0.731025,
      "adjusted_effect": 0.731025,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "samsung_common_price"
    },
    {
      "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
      "original_effect": 0.731025,
      "adjusted_effect": 0.731025,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "samsung_preferred_price"
    },
    {
      "path_id": "us_10y_yield_to_macro/macro_to_price",
      "original_effect": -0.5848199999999999,
      "adjusted_effect": -0.5848199999999999,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "us_10y_yield"
    },
    {
      "path_id": "usdkrw_to_macro/macro_to_price",
      "original_effect": 0.03133686676025391,
      "adjusted_effect": 0.03133686676025391,
      "adjustment_codes": [],
      "competing_refs": [],
      "root_group": "usdkrw"
    }
  ]
}
```

### E12 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E12",
  "items": [
    {
      "path_id": "preferred_rsi_14_to_market_regime/market_regime_to_price",
      "horizon": "1y",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 0.9123050849124498,
      "effect": 0.0017858086224000543
    },
    {
      "path_id": "preferred_trend_alignment_to_market_regime/market_regime_to_price",
      "horizon": "1y",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 0.9123050849124498,
      "effect": 0.01094856762212753
    },
    {
      "path_id": "preferred_volume_z_to_market_regime/market_regime_to_price",
      "horizon": "1y",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 0.9123050849124498,
      "effect": -0.0016046860351343285
    },
    {
      "path_id": "samsung_common_price_to_preferred/preferred_to_price",
      "horizon": "1y",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 0.9123050849124498,
      "effect": 0.02334212386443433
    },
    {
      "path_id": "samsung_preferred_price_to_preferred/preferred_to_price",
      "horizon": "1y",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 0.9123050849124498,
      "effect": 0.02334212386443433
    },
    {
      "path_id": "us_10y_yield_to_macro/macro_to_price",
      "horizon": "1y",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 0.9123050849124498,
      "effect": -0.02667671298792494
    },
    {
      "path_id": "usdkrw_to_macro/macro_to_price",
      "horizon": "1y",
      "lag_hours": 0.0,
      "active_fraction": 1.0,
      "decay": 0.9123050849124498,
      "effect": 0.0014294391445301786
    }
  ]
}
```

### E13 structured reasoning
```json
{
  "applicable": false,
  "reason": "No mature same-regime analogy above similarity gate",
  "kind": "E13",
  "case_ids": [],
  "similarity": null,
  "recency": null,
  "sample_count": 0,
  "regime_match": false,
  "relevance": 0.0,
  "capped_delta": [
    0.0,
    0.0,
    0.0
  ]
}
```

### E19 structured reasoning
```json
{
  "applicable": true,
  "reason": null,
  "kind": "E19",
  "publishable": false,
  "failed_checks": [
    "missing_forecast",
    "fatal_challenge"
  ],
  "offending_engines": [
    "E18",
    "E14"
  ],
  "driver_refs": [
    "us_10y_yield_to_macro/macro_to_price",
    "samsung_common_price_to_preferred/preferred_to_price",
    "samsung_preferred_price_to_preferred/preferred_to_price",
    "preferred_trend_alignment_to_market_regime/market_regime_to_price",
    "preferred_rsi_14_to_market_regime/market_regime_to_price"
  ],
  "falsifiers": [],
  "error_class": "insufficient_evidence"
}
```

### What Would Change My Mind
Supply genuine critical DRAM evidence and missing flow/accounting sources, then create a NEW forward prediction. Do not edit this one.
- up: usdkrw gt 1350.0 krw_per_usd
- up: samsung_common_price lt 65000.0 krw_per_share
- up: samsung_preferred_price lt 52000.0 krw_per_share
- down: us_10y_yield lt 4.0 percent
- down: preferred_volume_z gt 0.0 z_score

## Outcome links (pending)
- 1d: 2026-09-10T05:51:04.715969+00:00 — append-only outcome; no future value collected.
- 1w: 2026-09-16T05:51:04.715969+00:00 — append-only outcome; no future value collected.
- 1m: 2026-10-09T05:51:04.715969+00:00 — append-only outcome; no future value collected.

## Completion blockers
- numeric_forecast_unavailable_critical_inputs_missing
- accounting_identity_inputs_unavailable
