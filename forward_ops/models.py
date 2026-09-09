"""Dimensioned shadow evidence. No model factors or probabilities are produced."""
from datetime import date,datetime
from statistics import mean,pstdev
from typing import Literal
from zoneinfo import ZoneInfo
from pydantic import BaseModel,ConfigDict,AwareDatetime,Field,model_validator

KST=ZoneInfo('Asia/Seoul')


class Record(BaseModel):
    model_config=ConfigDict(extra='forbid',frozen=True,allow_inf_nan=False)


class Position(Record):
    provenance: Literal['human_supplied_market_close']='human_supplied_market_close'
    venue: Literal['kospi_spot','index_futures','stock_futures','program','usd_futures','stock_spot','sector_relative']
    instrument: str=Field(min_length=1,max_length=80)
    investor: Literal['foreign','institution','program','all']
    measure: Literal['net_buy_value','net_buy_contracts','net_position_contracts','relative_flow']
    unit: Literal['krw_million','contracts','ratio']
    value: float
    trade_date: date
    effective_at: AwareDatetime
    released_at: AwareDatetime
    source_ref: str=Field(min_length=1,max_length=1000)
    submitter: str=Field(min_length=1,max_length=120)
    market_timezone: Literal['Asia/Seoul']='Asia/Seoul'
    session: Literal['regular_close']='regular_close'
    expiry: str | None=None
    revision_of: str | None=None
    operands: dict[str,float] | None=None

    @model_validator(mode='after')
    def dimensions(self):
        if self.effective_at>self.released_at:raise ValueError('release precedes effective time')
        local=self.effective_at.astimezone(KST)
        if local.date()!=self.trade_date or (local.hour,local.minute)<(15,30):raise ValueError('not regular close/date')
        if self.venue.endswith('futures'):
            import re
            if self.unit!='contracts' or self.measure not in ('net_buy_contracts','net_position_contracts') or not self.expiry or not re.fullmatch(r'\d{4}-(0[1-9]|1[0-2])',self.expiry):
                raise ValueError('futures requires contracts measure and expiry')
        elif self.venue=='sector_relative':
            keys={'sector_net_buy','sector_turnover','market_net_buy','market_turnover'}
            if self.unit!='ratio' or self.measure!='relative_flow' or not self.operands or set(self.operands)!=keys:
                raise ValueError('relative flow operands required')
            o=self.operands
            if o['sector_turnover']<=0 or o['market_turnover']<=0:raise ValueError('positive turnover required')
            actual=o['sector_net_buy']/o['sector_turnover']-o['market_net_buy']/o['market_turnover']
            if abs(actual-self.value)>1e-9:raise ValueError('relative flow identity')
        elif self.unit!='krw_million' or self.measure!='net_buy_value':raise ValueError('cash requires KRW million net purchases')
        return self

    def key(self):return (self.trade_date.isoformat(),self.venue,self.instrument,self.investor,self.measure,self.expiry)


class Event(Record):
    event_id: str=Field(pattern=r'^[a-zA-Z0-9_-]{1,100}$')
    event_type: Literal['FOMC','CPI','employment','samsung_earnings']
    field: str=Field(min_length=1)
    unit: str=Field(min_length=1)
    actual: float
    released_at: AwareDatetime
    source_ref: str=Field(min_length=1)
    consensus: tuple[float,...]=()
    consensus_at: AwareDatetime | None=None
    consensus_ref: str | None=None
    pre_move: float | None=Field(default=None,ge=-1,le=1)
    expected_price_move: float | None=Field(default=None,ge=-1,le=1)
    pre_start: AwareDatetime | None=None
    pre_end: AwareDatetime | None=None
    yield_before: float | None=None
    yield_after: float | None=None
    yield_before_at: AwareDatetime | None=None
    yield_after_at: AwareDatetime | None=None
    yield_source_ref: str | None=None

    @model_validator(mode='after')
    def chronology(self):
        if self.consensus and (not self.consensus_at or not self.consensus_ref or self.consensus_at>=self.released_at):
            raise ValueError('consensus must precede release with provenance')
        if self.pre_move is not None and (not self.pre_start or not self.pre_end or not self.pre_start<self.pre_end<self.released_at):
            raise ValueError('pre-move window must precede event')
        if self.yield_before is not None or self.yield_after is not None:
            if any(v is None for v in (self.yield_before,self.yield_after,self.yield_before_at,self.yield_after_at)) or not self.yield_source_ref:
                raise ValueError('yield response provenance required')
            if not self.yield_before_at<=self.released_at<=self.yield_after_at:raise ValueError('yield response chronology')
        return self


def event_diagnostic(event,cutoff):
    event=Event.model_validate(event)
    if event.released_at>cutoff or (event.yield_after_at and event.yield_after_at>cutoff):raise ValueError('event after cutoff')
    expectation=mean(event.consensus) if event.consensus else None
    scale=pstdev(event.consensus) if len(event.consensus)>=2 else 0.
    surprise=(event.actual-expectation)/scale if scale else None
    priced=None
    if event.pre_move is not None and event.expected_price_move not in (None,0.):
        priced=min(1.,abs(event.pre_move/event.expected_price_move)) if event.pre_move*event.expected_price_move>0 else 0.
    return {'event':event.model_dump(mode='json'),'expectation':expectation,'surprise':surprise,'surprise_unit':'consensus_standard_deviations',
        'priced_in_fraction':priced,'residual_surprise':surprise*(1-priced) if surprise is not None and priced is not None else None,
        'yield_change_pp':event.yield_after-event.yield_before if event.yield_after is not None else None,
        'model_influence':False,'equity_direction':'unknown',
        'challenger_scenarios':['Expectation already priced; headline surprise may not be equity surprise.',
            'Long-yield response and earnings/demand can oppose the headline interpretation.',
            'Selloff may continue: require frozen Future, Bottom, Confidence, Alignment and Liquidity gates.'],
        'contract_finding':'FE-F02: shadow only; no event injection into frozen v2'}


def position_diagnostics(rows,cutoff):
    valid=[]
    for row in rows:
        p=Position.model_validate(row)
        if p.released_at<=cutoff:
            valid.append({**p.model_dump(mode='json'),'equity_direction':'unknown',
                'valid_horizons':['1w','1m'],'long_horizon_limitation':'Longitudinal holdings evidence unavailable',
                'freshness':'fresh' if (cutoff-p.effective_at).total_seconds()<=4*86400 else 'stale'})
    # One latest point per series, never count yesterday and today as two votes.
    history=valid;latest={}
    for row in history:
        key=(row['venue'],row['instrument'],row['investor'],row['measure'],row['expiry'])
        if key not in latest or row['effective_at']>latest[key]['effective_at']:latest[key]=row
    valid=list(latest.values());interactions=[]
    for cash in valid:
        if cash['venue'] not in ('kospi_spot','stock_spot'):continue
        for future in valid:
            if future['venue'] not in ('index_futures','stock_futures'):continue
            if (cash['investor'],cash['trade_date'])!=(future['investor'],future['trade_date']):continue
            sign=cash['value']*future['value']
            interactions.append({'actor':cash['investor'],'cash_instrument':cash['instrument'],'future_instrument':future['instrument'],
                'expiry':future['expiry'],'relationship':'concurrent_positioning' if sign>0 else 'opposing_positioning_possible_hedge' if sign<0 else 'indeterminate',
                'certainty':'unknown hedge intent; net trading is not change in open positions','horizons':['1w','1m']})
    return {'rows':valid,'historical_rows':history,'interactions':interactions,'conflicts':[],'model_influence':False,
        'contract_finding':'FE-F01: separate Market Positioning Diagnostic, not E09/E10 replacement'}
