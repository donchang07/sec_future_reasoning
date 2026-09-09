"""Ex-ante requirement matrix. Levels are not causal or horizon weights."""
from .types import FactorRequirement, Requirement as R, MappingRule, MAPPING_VERSION

MATRIX = {}


def add(names,module,bucket,levels,rationale,age=45.):
    for name in names.split():
        MATRIX[name]=FactorRequirement(factor_id=name,module=module,bucket=bucket,
            levels=dict(zip(('1w','1m','1y'),levels)),rationale=rationale,max_age_days=age)


H,S,B,O,U=R.HARD,R.STRONG,R.SUPPORTING,R.OPTIONAL,R.UNAVAILABLE_ALLOWED
add('samsung_preferred_price','price_regime','price',(H,H,H),'Instrument anchor',4.)
add('preferred_trend_alignment preferred_volume_z preferred_rsi_14','price_regime','regime',(S,B,O),'Short regime; correlated indicators share one bucket',4.)
add('samsung_common_price','price_regime','regime',(B,B,B),'Relative-share context',4.)
add('us_10y_yield','macro','rates',(S,S,S),'Discount-rate evidence',7.)
add('usdkrw','macro','fx',(S,S,S),'Currency and foreign allocation',4.)
add('dram_contract_asp','memory','price',(B,S,S),'Contract realization differs from spot',45.)
add('dram_spot_price','memory','price',(B,B,U),'SKU spot only; no long realization assumption',4.)
add('hbm_price','memory','price',(O,S,S),'HBM pricing distinct from demand',120.)
add('hbm_demand','memory','demand',(O,S,S),'HBM demand distinct from commodity price',120.)
add('memory_inventory memory_bit_shipment','memory','balance',(O,B,S),'Inventory and physical balance',120.)
add('semiconductor_export_momentum','memory','demand',(B,B,B),'Broad nominal export demand proxy',45.)
add('samsung_eps samsung_eps_revision samsung_operating_margin','earnings','profitability',(B,S,S),'Earnings level/revision with explicit period',150.)
add('samsung_operating_cash samsung_free_cash_flow','earnings','cash_generation',(O,B,S),'Cash generation',150.)
add('samsung_total_assets samsung_total_liabilities samsung_total_equity','earnings',None,(O,B,H),'Long financial solvency anchor',150.)
add('samsung_revenue samsung_operating_profit samsung_capex_ppe_cash samsung_capex_intangibles samsung_capex samsung_cash_begin samsung_cash_end samsung_cash_change samsung_investing_cash samsung_financing_cash samsung_fx_cash_effect samsung_debt samsung_cash_debt_ratio','earnings',None,(O,O,O),'Accounting diagnostics; do not duplicate coverage',150.)
add('foreign_net_buy','flow','foreign',(S,S,B),'Marginal foreign demand; transaction liquidity separate',4.)
add('institution_net_buy','flow','domestic',(S,S,B),'Domestic allocation',4.)
add('program_net_buy semiconductor_relative_flow','flow','domestic',(B,B,O),'Correlated supporting flow',4.)
add('hyperscaler_capex gpu_demand_growth','ai_demand','investment',(O,B,S),'Investment demand duration',150.)
add('cxmt_memory_capacity fab_capacity yield_rate bit_supply new_capacity','supply','capacity',(U,B,S),'Physical supply duration and scope',150.)
add('samsung_forward_per equity_discount_rate','valuation','valuation',(B,B,S),'Valuation duration')

BUCKETS={'macro':('rates','fx'),'memory':('price','demand','balance'),
    'earnings':('profitability','cash_generation'),'flow':('foreign','domestic'),
    'price_regime':('price','regime'),'ai_demand':('investment',),'supply':('capacity',),'valuation':('valuation',)}
MINIMUMS={'1w':{'macro':.4,'price_regime':.6},
    '1m':{'macro':.4,'memory':.25,'earnings':.4,'price_regime':.6},
    '1y':{'macro':.4,'memory':.5,'earnings':.8,'price_regime':.4}}
MEMORY_FAMILIES=('dram_contract_asp','dram_spot_price','hbm_demand','hbm_price','memory_inventory','memory_bit_shipment','semiconductor_export_momentum')

# Explicit unit/scope registry, independent of SourceObservation field labels.
UNITS={
 'us_10y_yield':'percent','usdkrw':'krw_per_usd','dram_contract_asp':'index',
 'dram_spot_price':'usd_per_chip','hbm_demand':'index','hbm_price':'usd_per_chip',
 'memory_inventory':'days','memory_bit_shipment':'bits','semiconductor_export_momentum':'percent',
 'samsung_preferred_price':'krw_per_share','samsung_common_price':'krw_per_share',
 'preferred_rsi_14':'rsi','preferred_volume_z':'z_score','preferred_trend_alignment':'score',
 'samsung_eps':'krw_per_share','samsung_eps_revision':'percent','samsung_operating_margin':'percent',
 'semiconductor_relative_flow':'ratio','hyperscaler_capex':'usd_million','gpu_demand_growth':'percent',
 'cxmt_memory_capacity':'wafers_per_month','fab_capacity':'wafers_per_month','new_capacity':'wafers_per_month',
 'yield_rate':'ratio','bit_supply':'bits','samsung_forward_per':'ratio','equity_discount_rate':'percent',
 'samsung_cash_debt_ratio':'ratio'}
for name in MATRIX:
    if name not in UNITS: UNITS[name]='krw_million'


def scope_for(factor):
    module=MATRIX[factor].module
    if factor=='dram_spot_price':return 'memory_spot'
    if factor=='dram_contract_asp':return 'memory_contract'
    if factor=='semiconductor_export_momentum':return 'semiconductor_exports'
    return {'price_regime':'market','earnings':'company_consolidated','supply':'industry_supply',
        'memory':'memory_business'}.get(module,module)


def rule_for(field,version=MAPPING_VERSION):
    factor = 'dram_spot_price' if field.startswith('dram_spot_') else field
    transform='identity';unit=None
    if field=='samsung_ppe_acquisition':factor='samsung_capex_ppe_cash';transform='cash_outflow_magnitude'
    if field=='semiconductor_export_demand':factor='semiconductor_export_momentum';transform='reported_yoy';unit='usd_million'
    if factor not in MATRIX:return None
    # Derived ratios must be generated from explicit operands, not claimed by a raw field.
    if factor in ('samsung_operating_margin','samsung_capex','samsung_free_cash_flow','samsung_cash_debt_ratio'):
        return None
    spec=MATRIX[factor]
    return MappingRule(source_field=field,source_unit=unit or UNITS[factor],factor_id=factor,
        economic_meaning=spec.rationale,transform=transform,
        mapping_confidence=.95 if factor=='dram_spot_price' else .8 if factor=='semiconductor_export_momentum' else 1.,
        valid_horizon=tuple(h for h,level in spec.levels.items() if level!=U),valid_regime=('*',),
        mapping_version=version,economic_scope=scope_for(factor))
