# 23-fact semantic mapping audit

Contract: real-world-contract-v2.0.0; mapping: semantic-mapping-v1.0.0

This is an offline contract audit, not a Prediction Journal. Original observations and their unmapped flags are unchanged.

Directly mappable: 19. Derived evidence mappable: 4. Still unmapped: 0 under the validated source scopes. Mapping availability is not directional evidence availability.

| Source field | Disposition | New factor | Transform | Horizon | Reason |
|---|---|---|---|---|---|
| samsung_total_assets | directly mappable | samsung_total_assets | identity | 1w,1m,1y | Long financial solvency anchor; value only, no directional comparator |
| samsung_total_liabilities | directly mappable | samsung_total_liabilities | identity | 1w,1m,1y | Long financial solvency anchor; value only, no directional comparator |
| samsung_total_equity | directly mappable | samsung_total_equity | identity | 1w,1m,1y | Long financial solvency anchor; value only, no directional comparator |
| samsung_operating_cash | directly mappable | samsung_operating_cash | identity | 1w,1m,1y | Cash generation; value only, no directional comparator |
| samsung_ppe_acquisition | derived evidence mappable | samsung_capex_ppe_cash | cash_outflow_magnitude | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_investing_cash | directly mappable | samsung_investing_cash | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_financing_cash | directly mappable | samsung_financing_cash | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_fx_cash_effect | directly mappable | samsung_fx_cash_effect | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_cash_change | directly mappable | samsung_cash_change | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_cash_begin | directly mappable | samsung_cash_begin | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_cash_end | directly mappable | samsung_cash_end | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_revenue | directly mappable | samsung_revenue | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| samsung_operating_profit | directly mappable | samsung_operating_profit | identity | 1w,1m,1y | Accounting diagnostics; do not duplicate coverage; value only, no directional comparator |
| dram_spot_ddr5_16gb_2gx8_4800_5600 | directly mappable | dram_spot_price | identity | 1w,1m | SKU spot only; no long realization assumption; value only, no directional comparator |
| dram_spot_ddr5_16gb_2gx8_ett | directly mappable | dram_spot_price | identity | 1w,1m | SKU spot only; no long realization assumption; value only, no directional comparator |
| dram_spot_ddr4_16gb_2gx8_3200 | directly mappable | dram_spot_price | identity | 1w,1m | SKU spot only; no long realization assumption; value only, no directional comparator |
| dram_spot_ddr4_16gb_2gx8_ett | directly mappable | dram_spot_price | identity | 1w,1m | SKU spot only; no long realization assumption; value only, no directional comparator |
| dram_spot_ddr4_8gb_1gx8_3200 | directly mappable | dram_spot_price | identity | 1w,1m | SKU spot only; no long realization assumption; value only, no directional comparator |
| dram_spot_ddr4_8gb_1gx8_ett | directly mappable | dram_spot_price | identity | 1w,1m | SKU spot only; no long realization assumption; value only, no directional comparator |
| dram_spot_ddr3_4gb_512mx8_1600_1866 | directly mappable | dram_spot_price | identity | 1w,1m | SKU spot only; no long realization assumption; value only, no directional comparator |
| semiconductor_export_demand | derived evidence mappable | semiconductor_export_momentum | reported_yoy | 1w,1m,1y | Broad nominal export demand proxy; explicit comparable-period signal |
| semiconductor_export_demand | derived evidence mappable | semiconductor_export_momentum | reported_yoy | 1w,1m,1y | Broad nominal export demand proxy; explicit comparable-period signal |
| semiconductor_export_demand | derived evidence mappable | semiconductor_export_momentum | reported_yoy | 1w,1m,1y | Broad nominal export demand proxy; explicit comparable-period signal |

## Constraints and unavailable derived facts
Three company identities passed: balance sheet, cash-flow components and cash rollforward. Memory business and industry supply remain non_applicable.
PPE cash CAPEX is available; total cash CAPEX/FCF are unavailable without intangible CAPEX. Debt ratio is unavailable without debt. All seven Spot levels lack a comparable prior quote; no rising/falling signal was invented.
August v1 is superseded by August v2; July final is a separate month. No working-day adjustment or cross-coverage acceleration was invented.

## Preserved journal
Original sealed journal hash: `ffe85d54f1e805c898bfc31d941b66c680b2950cbe515716c5942be9e2a15cae`.
Original file hash: `c88e2cc2aa6bffbd2360616013f964e207b6d36a1f42af2ecbd9f3473a406d5e`. No probabilities or Decisions were recalculated.
The full audit retains each mapping rule, raw reference, mapping confidence, reporting period, derived signals and output evidence ID in the [JSON audit](real-world-contract-refinement.mapping-audit.json).
