# real-world-contract-refinement — Design v2.0.0

2026-09-09. Contract release `real-world-contract-v2.0.0`, mapping release `semantic-mapping-v1.0.0`. [Plan](../../01-plan/features/real-world-contract-refinement.plan.md). The policies below are fixed before writing tests/code and before any new prediction. They are research eligibility policies, not estimated market parameters.

## 1. Boundary and economic rationale

Keep legacy `engines.py`, `technical.py`, `decision.py`, `live.py`, `act_live.py`, fixtures and live model profile unchanged. Implement a separately versioned `reasoning/refinement` library. Its public pipeline is `SourceObservation → semantic_map → FactorEvidence → ModuleState / E11 → CoverageAssessment → publish_candidate`. It assesses an existing engine-produced candidate; it does not invent a candidate from priors. The next live feature must explicitly select v2 and connect its structured module states to the causal engine workflow. This feature neither runs that live integration nor emits Prediction Journals.

Short-term market repricing can have adequate rates/FX and price/regime context without a monthly contract-price publication. A one-year semiconductor forecast needs business cash generation and multiple independent memory mechanisms. Therefore DRAM contract ASP is not individually hard-required for every horizon; absence of long-horizon memory evidence still withholds the long forecast. Technical evidence alone cannot satisfy the macro gate. Flow missingness is distinguished from the unchanged transaction liquidity gate.

The [PRD](../../samsung_future_reasoning_prd_v1.1.html) differentiates horizon inputs and includes price, demand, inventory, supply, earnings and cash flow. [TrendForce's methodology](https://www.dramexchange.com/intelligence/priceinformation) separately describes spot transactions and OEM contract-price inquiries with different update frequencies. Neither measures HBM demand. [Samsung official statements](https://www.samsung.com/global/ir/financial-information/audited-financial-statements/) disclose consolidated accounting, not one company-wide physical sales unit. These source distinctions motivate the design; the numerical coverage cutoffs below are explicit conservative engineering assumptions, not claims established by those sources.

## 2. Five levels and full active-factor matrix

H = Hard Required: missing, stale, conflicted or unmapped withholds. S = Strong Evidence: absence lowers confidence. B = Supporting Evidence: eligible facts can support state/direction; no individual missingness penalty. O = Optional: diagnostic/context use; no coverage credit. U = Unavailable Allowed: explicitly excluded from that horizon, even if observed. Level is not a causal weight. Unknown never receives a neutral signal.

Each named factor in grouped rows receives its own registry entry. This covers every frozen-profile factor plus new memory and accounting/supply factors; the wider unconnected 49-factor product ontology is outside this release.

| Factors | Module | 1w | 1m | 1y | Reason |
|---|---|---|---|---|---|
| samsung_preferred_price | price_regime | H | H | H | Instrument anchor required |
| preferred_trend_alignment, preferred_volume_z, preferred_rsi_14 | price_regime | S | B | O | Short timing/regime; correlated indicators share one bucket |
| samsung_common_price | price_regime | B | B | B | Relative-share context |
| us_10y_yield, usdkrw | macro | S | S | S | Rates/FX repricing; either can supply one independent macro bucket |
| dram_contract_asp | memory | B | S | S | Contract realization; monthly/long cash earnings relevance |
| dram_spot_price | memory | B | B | U | Specific spot SKU; no one-year realization assumption |
| hbm_demand, hbm_price | memory | O | S | S | Different demand and pricing mechanisms |
| memory_inventory, memory_bit_shipment | memory | O | B | S | Inventory balance and physical shipments |
| semiconductor_export_momentum | memory | B | B | B | Broad nominal exports, not DRAM price |
| samsung_eps, samsung_eps_revision | earnings | B | S | S | Earnings level/revisions; scope must be explicit |
| samsung_operating_margin | earnings | B | S | S | Derived consolidated profitability |
| samsung_operating_cash, samsung_free_cash_flow | earnings | O | B | S | Cash generation; shared bucket |
| samsung_total_assets, samsung_total_liabilities, samsung_total_equity | earnings | O | B | H | Long-horizon solvency/accounting anchor |
| samsung_revenue, samsung_operating_profit | earnings | O | O | O | Inputs to margin/constraints, not independent direction votes |
| samsung_capex_ppe_cash, samsung_capex_intangibles, samsung_capex, samsung_cash_begin, samsung_cash_end, samsung_cash_change, samsung_investing_cash, samsung_financing_cash, samsung_fx_cash_effect, samsung_debt, samsung_cash_debt_ratio | earnings | O | O | O | Accounting diagnostics; avoid repeated coverage from one statement |
| foreign_net_buy, institution_net_buy | flow | S | S | B | Marginal demand; liquidity gate remains separate |
| program_net_buy, semiconductor_relative_flow | flow | B | B | O | Supporting correlated flow |
| hyperscaler_capex, gpu_demand_growth | ai_demand | O | B | S | Investment demand horizon |
| cxmt_memory_capacity, fab_capacity, yield_rate, bit_supply, new_capacity | supply | U | B | S | Industry supply constraints only at matching scope |
| samsung_forward_per, equity_discount_rate | valuation | B | B | S | Valuation duration |

## 3. Coverage and confidence

Coverage measures economic buckets, not count of rows. Per bucket credit is the maximum eligible mapping confidence among H/S/B facts in it. Unit-invalid, stale, future, mixed-mode or conflicting values receive no credit. Repeated fields/SKUs/derived signals cannot increase a bucket maximum. Module coverage is the mean of its fixed bucket credits; no missing bucket is fabricated.

Buckets: macro = rates / FX; memory = price (contract/spot/HBM price) / demand (HBM demand/exports) / balance (inventory/bit shipment); earnings = profitability (EPS/revision/margin) / cash_generation (OCF/FCF); flow = foreign / domestic (institution/program/relative); price_regime = instrument price / regime (common price/technical indicators). AI/supply/valuation each have one diagnostic bucket. A financial balance-sheet H fact is checked individually but does not manufacture earnings profitability credit.

| Horizon | Macro minimum | Memory minimum | Earnings minimum | Flow minimum | Price/Regime minimum | Additional quorum |
|---|---:|---:|---:|---:|---:|---|
| 1w | 0.40 | none | none | none | 0.60 | Macro prevents technical-only forecast |
| 1m | 0.40 | 0.25 | 0.40 | none | 0.60 | At least one memory mechanism and one financial bucket |
| 1y | 0.40 | 0.50 | 0.80 | none | 0.40 | At least two distinct eligible memory families; Spot excluded |

0.40 permits one well-mapped observation among two economic buckets; 0.60 requires both price/context buckets; 0.25 permits one well-mapped memory bucket; 0.50 requires at least two of three memory buckets; 0.80 requires both earnings buckets. These are deliberately simple ex-ante evidence quorums. They do not guarantee forecast accuracy. Relevant and failed company identities also withhold. Non-applicable segment/industry constraints do not become failures.

Confidence multiplier = minimum coverage over mandatory modules × 0.9 for each module with any missing Strong Evidence factor. Penalty is once per module, not once per missing row or SKU. Missing H and coverage failure yield withheld probability; missing S yields a confidence penalty even when eligible. Supporting facts can improve a bucket and its confidence credit. O/U cannot. An unchanged candidate probability vector is either released unchanged or withheld; it is never blended toward Flat due only to missingness. Candidate confidence is multiplied, never increased. The candidate object remains separate from decision policy and must be supplied by future reasoning, not by technical adapters. Both candidate and assessment are pinned to cutoff, horizon, data mode and contract version.

## 4. Semantic mapping and independent memory evidence

`SourceObservation`: source_id, source_field, source_unit, value, economic_scope, series_id, observed_at, effective_at, released_at nullable, collected_at, data_mode, raw_ref; optional prior_value, reported_yoy, workdays/current and prior, month, coverage_days, vintage_stage. All times aware and as-of eligible. Unknown release uses collection as known-at; a field cannot backdate a collection.

`MappingRule`: source_field pattern, source_unit, factor_id, economic_meaning, transform, mapping_confidence, valid_horizon, valid_regime, mapping_version, scope requirement. Registry is allowlisted; callers cannot label any arbitrary source numeric field a factor. Mapping confidence 1.0 for identity on official facts, 0.95 for a precise SKU spot quote, 0.80 for broad export momentum. These represent semantic scope uncertainty, not investment confidence. A changed mapping version changes evidence IDs/audit hash even when raw observations are identical. Unsupported versions are rejected until explicitly registered; tests register a second policy in memory, not silently in production.

Transforms: identity; negative cash outflow → nonnegative PPE cash CAPEX; reported YoY; percent change against supplied comparable positive prior value; operating margin = operating profit / revenue × 100 for same issuer/scope/period; FCF = OCF − (PPE cash CAPEX + intangible cash CAPEX), only when both cash CAPEX components are available. Cash/debt ratio requires actual debt >0. No annualization, artificial base index, derived selling price or invented working days.

Seven Memory families: `dram_contract_asp`, `dram_spot_price`, `hbm_demand`, `hbm_price`, `memory_inventory`, `memory_bit_shipment`, `semiconductor_export_momentum`. Prices remain SKU and market scoped. A one-point spot quote has value but no directional change. Directional signal for a comparable rate/change is clipped growth/100; inventory change has opposite sign. Family score is the mean of independent economic-root signals weighted by mapping confidence; multiple correlated SKUs share the price-publisher spot-family root. Module memory score is the mean of available family scores, with explicit positive/negative families and contradiction ratio. Unknown families are absent, not zero. This is a typed Memory State estimate, not a direct stock forecast or new horizon weight.

## 5. Export revisions and signals

Stages: 10-day → nowcast_v1; 20-day → nowcast_v2; full-month preliminary → nowcast_v3; full-month confirmed → final. Select highest eligible stage, then latest release/collection; a delayed v1 cannot overwrite final. Same-vintage simultaneous unequal values conflict. Preserve all source vintages but select one per month for state inference. Every derivative shares the original month/root, preventing repeated positive votes.

YoY = reported same-period percentage, or `(current/prior_year_same_period - 1)*100` with real comparator. Working-day-adjusted YoY = `((1+yoy/100)*prior_year_workdays/current_workdays-1)*100`; absent workdays => unavailable. Acceleration = current YoY − immediately previous month's YoY (percentage points), only matching 10/20-day coverage or full-month stages. Never compare v1 with v2 as acceleration, nor sum cumulative totals. Monthly preliminary/final are comparable full-month periods despite different month lengths.

## 6. E11 v2 layered constraints

Company Financial Constraint uses actual same-period consolidated facts: assets = liabilities + equity; cash change = OCF + investing CF + financing CF + FX effect; cash end − cash begin = cash change. Tolerance remains 0.01 in KRW million. Report OCF, correctly scoped cash CAPEX, derived FCF and cash/debt ratio when available. Derived FCF is not an independent identity check unless an independently reported FCF under the same definition exists. Missing components mean individual non_applicable, not zero or failure.

Memory Business Constraint optionally checks memory-segment revenue = physical volume × ASP with consistent unit/currency/segment/period metadata. Consolidated company revenue cannot populate this object. Industry Supply Constraint optionally checks production <= capacity, yield in [0,1], bit supply <= capacity × yield × bits per production unit, and newly installed capacity when matching data exist. No unit-compatible inputs => non_applicable with missing fields listed. Typed caller input cannot mix scope or periods. A domain with some checks remains partially evaluated and records each non-applicable check separately.

## 7. 23 preserved-fact review

Classify 12 official financial amounts as directly mappable to company facts; the signed PPE acquisition as derived-mappable cash CAPEX; seven Spot SKU observations as directly mappable to Spot (no direction without a prior); three export amount/YoY records as derived-mappable export momentum. Expected 19 direct / 4 derived / 0 still-unmapped **only if semantic/time validation passes**. Preserve a still-unmapped disposition for any invalid row; the old journals' mapping='unmapped' remains untouched. Derived operating margin uses revenue and operating profit together. Intangible CAPEX, full FCF, debt ratio, memory business inputs remain unavailable because the 23 facts do not contain them.

The disposition audit is a new contract artifact, not a Prediction Journal and not a recalculation of old predictions. Raw records without an explicit mapping produce no module state, coverage or probability change.

## 8. Golden tests and release

Write tests first for the user's 15 scenarios: missing contract + spot; rising spot / unknown contract; strong export / weak DRAM and reverse; short sufficient / long insufficient; applicable company; non-applicable memory; missing industry; missing S penalty; missing H withholding; raw 23 unmapped facts no effect; unit mismatch; same-month dedup; mapping version change; horizon divergence. Add boundary, mixed mode, cutoff, conflict, same-scope financial, export working-day/acceleration, incomplete CAPEX and unchanged candidate direction/Decision tests.

Code modules: contracts/registry, semantic mapping, export revision, memory/coverage, E11 constraints, public contract assessment and offline audit CLI. A JSON release manifest pins their hashes and the frozen legacy profile/core digests. Test data are synthetic; the CLI only reads existing local facts and outputs classification JSON/Markdown. No collection command is provided. Both old journals are byte-hashed before/after, integrity-verified and replayed at recorded commits (`7c36073`, `1eb1885`). All 129 original tests and new tests must pass on Python 3.11/3.12 before completion.

### Check/Act clarifications before final version tag

RW-01: choose each provider's latest eligible revision first; unequal values for the same series/effective time across providers remain conflicted, regardless of collection ordering. RW-02: company observations/evidence carry `reporting_period` (e.g. `2026-H1`, `2026-Q2`, `2026-FY`). Missing period is unmapped; derived ratios require both period end and reporting period to match. Cross-period E11 operands are rejected before evaluation. The old H1 source scope supplies this key explicitly in the classification bridge.

An older export vintage can be stale for current coverage while still being a known-at-cutoff historical comparator. Such a comparator adds provenance to acceleration, never current coverage or a separate directional vote. Mapping versions other than the published registry version are rejected for real data; synthetic tests alone may instantiate a `semantic-mapping-test-*` version to verify identity changes. The v2.0.0 manifest remains a release candidate until the final immutable version tag after these checks.
