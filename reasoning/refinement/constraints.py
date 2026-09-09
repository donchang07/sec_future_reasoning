"""E11 v2: company, memory business and industry supply have distinct scopes."""
from typing import Literal
from pydantic import model_validator
from ..schemas.contracts import Contract, Number


class CompanyFinancials(Contract):
    scope: Literal['company_consolidated']='company_consolidated'
    period: str
    unit: Literal['krw_million']='krw_million'
    assets: Number | None=None
    liabilities: Number | None=None
    equity: Number | None=None
    revenue: Number | None=None
    operating_cash: Number | None=None
    capex_ppe_cash: Number | None=None
    capex_intangibles: Number | None=None
    reported_free_cash_flow: Number | None=None
    investing_cash: Number | None=None
    financing_cash: Number | None=None
    fx_cash_effect: Number | None=None
    cash_change: Number | None=None
    cash_begin: Number | None=None
    cash_end: Number | None=None
    debt: Number | None=None
    source_refs: tuple[str,...]=()

    @model_validator(mode='after')
    def magnitudes(self):
        if any(x is not None and x<0 for x in (self.capex_ppe_cash,self.capex_intangibles,self.debt)):
            raise ValueError('cash CAPEX and debt require nonnegative magnitudes')
        return self


class MemoryBusiness(Contract):
    scope: Literal['memory_segment']='memory_segment'
    period: str
    currency: Literal['usd','krw']='usd'
    volume_unit: Literal['chips','bits']='chips'
    asp_unit: Literal['usd_per_chip','usd_per_bit','krw_per_chip','krw_per_bit']='usd_per_chip'
    revenue: Number | None=None
    volume: Number | None=None
    asp: Number | None=None
    source_refs: tuple[str,...]=()

    @model_validator(mode='after')
    def dimensions(self):
        if self.asp_unit != self.currency+'_per_'+self.volume_unit[:-1]:
            raise ValueError('memory revenue/volume/ASP units mismatch')
        return self


class IndustrySupply(Contract):
    scope: Literal['industry_supply']='industry_supply'
    period: str
    capacity_unit: Literal['wafers_per_month']='wafers_per_month'
    bit_supply_unit: Literal['bits_per_month']='bits_per_month'
    capacity: Number | None=None
    production: Number | None=None
    yield_rate: Number | None=None
    bit_supply: Number | None=None
    bits_per_wafer: Number | None=None
    new_capacity: Number | None=None
    source_refs: tuple[str,...]=()


class Check(Contract):
    name: str
    status: Literal['passed','failed','non_applicable']
    lhs: Number | None=None
    rhs: Number | None=None
    residual: Number | None=None
    missing: tuple[str,...]=()
    source_refs: tuple[str,...]=()


class DomainResult(Contract):
    status: Literal['passed','failed','non_applicable']
    checks: tuple[Check,...]
    missing: tuple[str,...]
    metrics: dict[str, Number | None]


class LayeredConstraints(Contract):
    engine_id: Literal['E11']='E11'
    version: Literal['e11-real-world-v2.0.0']='e11-real-world-v2.0.0'
    company: DomainResult
    memory: DomainResult
    industry: DomainResult
    fatal: bool


def _check(name,record,fields,formula,inequality=False):
    missing=tuple(k for k in fields if record is None or getattr(record,k) is None)
    if missing:return Check(name=name,status='non_applicable',missing=missing)
    lhs,rhs=formula(record);valid=lhs<=rhs+.01 if inequality else abs(lhs-rhs)<=.01
    return Check(name=name,status='passed' if valid else 'failed',lhs=lhs,rhs=rhs,residual=lhs-rhs,source_refs=record.source_refs)


def _domain(checks,metrics=None):
    statuses={c.status for c in checks}
    return DomainResult(status='failed' if 'failed' in statuses else 'passed' if 'passed' in statuses else 'non_applicable',
        checks=tuple(checks),missing=tuple(sorted({k for c in checks for k in c.missing})),metrics=metrics or {})


def evaluate_e11(company=None,memory=None,industry=None):
    if company is not None:company=CompanyFinancials.model_validate(company)
    if memory is not None:memory=MemoryBusiness.model_validate(memory)
    if industry is not None:industry=IndustrySupply.model_validate(industry)
    c=company
    capex=(c.capex_ppe_cash+c.capex_intangibles) if c and c.capex_ppe_cash is not None and c.capex_intangibles is not None else None
    fcf=c.operating_cash-capex if c and c.operating_cash is not None and capex is not None else None
    company_checks=[
        _check('balance_sheet',c,('assets','liabilities','equity'),lambda x:(x.assets,x.liabilities+x.equity)),
        _check('cash_components',c,('cash_change','operating_cash','investing_cash','financing_cash','fx_cash_effect'),lambda x:(x.cash_change,x.operating_cash+x.investing_cash+x.financing_cash+x.fx_cash_effect)),
        _check('cash_rollforward',c,('cash_begin','cash_end','cash_change'),lambda x:(x.cash_end-x.cash_begin,x.cash_change)),
        _check('reported_fcf_identity',c,('reported_free_cash_flow','operating_cash','capex_ppe_cash','capex_intangibles'),lambda x:(x.reported_free_cash_flow,x.operating_cash-x.capex_ppe_cash-x.capex_intangibles)),
    ]
    cm=_domain(company_checks,{'operating_cash_flow':c.operating_cash if c else None,'capex_ppe_cash':c.capex_ppe_cash if c else None,
        'capex_total_cash':capex,'free_cash_flow':fcf,'cash_debt_ratio':c.cash_end/c.debt if c and c.cash_end is not None and c.debt is not None and c.debt>0 else None})
    mm=_domain([_check('memory_revenue_identity',memory,('revenue','volume','asp'),lambda x:(x.revenue,x.volume*x.asp))])
    checks=[_check('production_capacity',industry,('production','capacity'),lambda x:(x.production,x.capacity),True),
        _check('bit_supply_bound',industry,('bit_supply','capacity','yield_rate','bits_per_wafer'),lambda x:(x.bit_supply,x.capacity*x.yield_rate*x.bits_per_wafer),True)]
    for name in ('yield_rate','new_capacity'):
        val=getattr(industry,name) if industry else None
        if val is None:checks.append(Check(name=name,status='non_applicable',missing=(name,)))
        else:
            valid=0<=val<=1 if name=='yield_rate' else val>=0
            checks.append(Check(name=name,status='passed' if valid else 'failed',lhs=val,rhs=1. if name=='yield_rate' else 0.,source_refs=industry.source_refs))
    im=_domain(checks)
    return LayeredConstraints(company=cm,memory=mm,industry=im,fatal=any(d.status=='failed' for d in (cm,mm,im)))


def company_from_evidence(evidence):
    items=[e for e in evidence if e.economic_scope=='company_consolidated']
    if not items:return None
    latest=max(e.effective_at for e in items);items=[e for e in items if e.effective_at==latest]
    aliases={'total_assets':'assets','total_liabilities':'liabilities','total_equity':'equity'}
    values={}
    for e in items:
        k=e.factor_id.removeprefix('samsung_');k=aliases.get(k,k)
        if k in CompanyFinancials.model_fields and k not in ('scope','period','unit','source_refs'):
            if k in values and values[k]!=e.value:raise ValueError('conflicting financial evidence')
            values[k]=e.value
    return CompanyFinancials(period=latest.isoformat(),source_refs=tuple(sorted({r for e in items for r in e.source_refs})),**values)
