"""Typed, offline inputs and a versioned, inspectable causal graph."""
from typing import Annotated, Literal
from datetime import timedelta
from pydantic import AwareDatetime, Field, model_validator
from .schemas.contracts import Contract, Observation, Number, Probability, ModuleId, Slug, DataMode


class FactorSpec(Contract):
    factor_id: Slug
    module: ModuleId
    baseline: Number
    scale: Annotated[float, Field(gt=0)]
    sign: Literal[-1,1]
    root_group: str
    critical: bool = False
    unit: str
    max_age_days: float = 45.


class Edge(Contract):
    edge_id: str
    source: str
    target: str
    sign: Literal[-1,1]
    strength: Probability
    confidence: Probability
    lag_days: float
    duration_days: float


class RawEvent(Contract):
    event_id: str
    text: str
    occurred_at: AwareDatetime
    published_at: AwareDatetime
    consensus_at: AwareDatetime
    consensus: tuple[Number,...]
    pre_move: Number
    expected_move: Annotated[float, Field(gt=0)]
    pre_start: AwareDatetime
    pre_end: AwareDatetime


class Bar(Contract):
    closed_at: AwareDatetime
    open: Annotated[float, Field(gt=0)]
    high: Annotated[float, Field(gt=0)]
    low: Annotated[float, Field(gt=0)]
    close: Annotated[float, Field(gt=0)]
    volume: Annotated[float, Field(ge=0)]

    @model_validator(mode='after')
    def valid_ohlc(self):
        if self.low > min(self.open,self.close) or self.high < max(self.open,self.close):
            raise ValueError('OHLC bounds')
        return self


class HistoryCase(Contract):
    case_id: str
    matured_at: AwareDatetime
    vector: tuple[Number,...]
    regime: str
    outcome: Literal['up','down','flat']


class Accounting(Contract):
    production: Number
    capacity: Number
    revenue: Number
    units_sold: Number
    unit_price: Number
    cash_flow: Number
    operating_cash: Number
    capex: Number


class Fixture(Contract):
    data_mode: DataMode = 'synthetic_fixture'
    fixture_version: str
    data_cutoff: AwareDatetime
    factors: tuple[FactorSpec,...]
    observations: tuple[Observation,...]
    events: tuple[RawEvent,...]
    edges: tuple[Edge,...]
    bars: dict[str,tuple[Bar,...]]
    history: tuple[HistoryCase,...]
    accounting: Accounting | None
    held: bool = False
    seed: int = 240901

    @model_validator(mode='after')
    def validate_inputs(self):
        specs = {x.factor_id:x for x in self.factors}
        if len(specs) != len(self.factors):
            raise ValueError('duplicate factor')
        for o in self.observations:
            if o.data_mode != self.data_mode:
                raise ValueError('mixed data mode in input batch')
            if o.factor_id not in specs or o.unit != specs[o.factor_id].unit:
                raise ValueError('unknown factor or unit mismatch')
        for bars in self.bars.values():
            if any(b.closed_at > self.data_cutoff for b in bars):
                raise ValueError('future bar')
            if any(a.closed_at >= b.closed_at for a,b in zip(bars,bars[1:])):
                raise ValueError('bars must be ordered and unique')
        for e in self.events:
            if not e.consensus_at < e.occurred_at <= e.published_at <= self.data_cutoff:
                raise ValueError('event/consensus look-ahead')
            if not e.pre_start < e.pre_end < e.occurred_at:
                raise ValueError('pre-event window look-ahead')
        if any(h.matured_at > self.data_cutoff for h in self.history):
            raise ValueError('unmatured historical outcome')
        if len({e.edge_id for e in self.edges}) != len(self.edges):
            raise ValueError('duplicate edge id')
        graph = {}
        for e in self.edges:
            if e.lag_days < 0 or e.duration_days <= 0:
                raise ValueError('invalid causal lag')
            graph.setdefault(e.source,[]).append(e.target)
        def visit(node,active):
            if node in active:
                raise ValueError('causal graph cycle')
            for target in graph.get(node,[]):
                visit(target,active|{node})
        for node in graph:
            visit(node,set())
        return self
