"""Generate synthetic research inputs, never expected engine outputs."""
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import uuid5, NAMESPACE_URL
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from reasoning.fixture import Fixture

ROOT = Path(__file__).resolve().parents[1]
CUTOFF = datetime(2026,9,9,tzinfo=timezone.utc)


def build():
    # baseline, scale, economic sign, observed displacement; mixed evidence.
    rows = [
        ('us_10y_yield','macro',4.,1.,-1,-.35,'percent'),
        ('usdkrw','macro',1350.,150.,-1,-.3,'krw_per_usd'),
        ('hyperscaler_capex','ai_demand',200000.,50000.,1,.8,'usd_million'),
        ('gpu_demand_growth','ai_demand',15.,20.,1,.7,'percent'),
        ('dram_contract_asp','memory',100.,20.,1,.65,'index'),
        ('hbm_demand','memory',100.,30.,1,.8,'index'),
        ('cxmt_memory_capacity','supply',100000.,30000.,-1,.3,'wafers_per_month'),
        ('samsung_eps','earnings',6000.,1500.,1,.6,'krw_per_share'),
        ('samsung_eps_revision','earnings',0.,10.,1,.5,'percent'),
        ('foreign_net_buy','capital_flow',0.,100000.,1,.7,'krw_million'),
        ('institution_net_buy','capital_flow',0.,100000.,1,.3,'krw_million'),
        ('program_net_buy','capital_flow',0.,100000.,1,.4,'krw_million'),
        ('semiconductor_relative_flow','capital_flow',0.,.1,1,.5,'ratio'),
        ('samsung_forward_per','valuation',12.,4.,-1,.2,'ratio'),
        ('equity_discount_rate','valuation',8.,2.,-1,-.3,'percent'),
        ('samsung_common_price','preferred',65000.,10000.,1,.2,'krw_per_share'),
        ('samsung_preferred_price','preferred',52000.,8000.,1,.2,'krw_per_share'),
        ('preferred_volume_z','market_regime',0.,2.,1,.6,'z_score'),
        ('preferred_trend_alignment','market_regime',0.,1.,1,.4,'score'),
        ('preferred_rsi_14','market_regime',50.,30.,1,.3,'rsi'),
    ]
    factors=[]; observations=[]; edges=[]
    for fid,module,baseline,scale,sign,shift,unit in rows:
        factors.append(dict(factor_id=fid,module=module,baseline=baseline,scale=scale,sign=sign,
                            root_group=fid,critical=fid in ('us_10y_yield','usdkrw','dram_contract_asp','samsung_preferred_price'),unit=unit))
        for i in range(4):
            t=CUTOFF-timedelta(days=4-i)
            observations.append(dict(observation_id=str(uuid5(NAMESPACE_URL,f'{fid}/{i}')),factor_id=fid,
                source_id='synthetic_fixture',revision_id='r1',unit=unit,value=baseline+scale*shift*(i+1)/4,
                observed_at=t.isoformat(),published_at=t.isoformat(),available_at=t.isoformat()))
        edges.append(dict(edge_id=f'{fid}_to_{module}',source=fid,target=f'module:{module}',sign=sign,
                          strength=.9,confidence=.95,lag_days=0.,duration_days=1.))
    for module in sorted({x[1] for x in rows}):
        edges.append(dict(edge_id=f'{module}_to_price',source=f'module:{module}',target='preferred_price',
                          sign=1,strength=.9,confidence=.95,lag_days=0.,duration_days=1.))
    # Sharp first low, slower second low with contracting volume, followed by
    # two closed neckline breaks. No reversal labels are supplied to the model.
    knots=[(0,58.),(95,55.),(105,56.),(117,47.),(125,54.),(140,46.8),(148,55.),(159,60.)]
    def price(i):
        for (a,x),(b,y) in zip(knots,knots[1:]):
            if a<=i<=b:
                return (x+(y-x)*(i-a)/(b-a))*1000
        raise ValueError(i)
    bars={}
    for tf,step in [('30m',timedelta(minutes=30)),('1d',timedelta(days=1)),('1w',timedelta(weeks=1)),('1mo',timedelta(days=30))]:
        series=[]
        for i in range(160):
            c=price(i); o=price(max(0,i-1))
            spread=350. if i<130 else 220.
            volume=1600. if 115<=i<=119 else 700. if 138<=i<=142 else 2200. if i>=148 else 1000.
            series.append(dict(closed_at=(CUTOFF-step*(159-i)).isoformat(),open=o,close=c,
                               high=max(o,c)+spread,low=min(o,c)-spread,volume=volume))
        bars[tf]=series
    event=dict(event_id='fomc_fixture',text='fomc fed us_10y_yield 4.0 percent',
               occurred_at=(CUTOFF-timedelta(days=1)).isoformat(),published_at=(CUTOFF-timedelta(days=1)).isoformat(),
               consensus_at=(CUTOFF-timedelta(days=3)).isoformat(),consensus=[3.8,4.,4.2],
               pre_move=.01,expected_move=.2,pre_start=(CUTOFF-timedelta(days=5)).isoformat(),pre_end=(CUTOFF-timedelta(days=2)).isoformat())
    raw=dict(fixture_version='synthetic-samsung-preferred-v1',data_cutoff=CUTOFF.isoformat(),factors=factors,
             observations=observations,edges=edges,events=[event],bars=bars,
             history=[dict(case_id='synthetic_analogy_1',matured_at=(CUTOFF-timedelta(days=400)).isoformat(),
                           vector=[.3,.7,.6,-.2,.5,.4,-.1,.2,.3],regime='risk_on',outcome='up')],
             accounting=dict(production=80.,capacity=100.,revenue=1000.,units_sold=10.,unit_price=100.,
                             cash_flow=200.,operating_cash=350.,capex=150.))
    return Fixture.model_validate(raw)


if __name__=='__main__':
    p=ROOT/'fixtures/samsung-preferred-v1.json';p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(build().model_dump(mode='json'),indent=2)+'\n',encoding='utf-8')
