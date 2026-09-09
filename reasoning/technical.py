"""OHLCV timing computations; none of these functions decide forecast direction."""
from statistics import mean
from .fixture import Bar, Fixture
from .schemas.contracts import Contract, Probability


class Wave(Contract):
    available: bool
    bottom_score: Probability
    top_score: Probability
    bottom_confirmed: bool
    top_confirmed: bool
    rsi: float | None
    sma: tuple[float,...]
    atr: float | None
    volume_ratio: float | None
    bottom_features: dict[str,bool]
    top_features: dict[str,bool]
    bottom_neckline: float | None
    top_neckline: float | None
    bottom_pivots: tuple[int,...]
    top_pivots: tuple[int,...]


class TechnicalEvidence(Contract):
    batch_id: str
    primary: str
    higher: str
    wave: Wave
    higher_wave: Wave
    bullish_alignment: Probability | None
    bearish_alignment: Probability | None
    buy_liquidity: Probability | None
    sell_liquidity: Probability | None
    regime_effect: float
    flow_effect: float
    reflexivity_effect: float
    evidence_refs: tuple[str,...]


def wilder(values,period=14):
    result=[None]*len(values)
    if len(values)>=period:
        result[period-1]=mean(values[:period])
        for i in range(period,len(values)):
            result[i]=(result[i-1]*(period-1)+values[i])/period
    return result


def analyze_wave(bars: tuple[Bar,...]) -> Wave:
    if len(bars)<150:
        return Wave(available=False,bottom_score=0.,top_score=0.,bottom_confirmed=False,top_confirmed=False,
                    rsi=None,sma=(),atr=None,volume_ratio=None,bottom_features={},top_features={},bottom_neckline=None,
                    top_neckline=None,bottom_pivots=(),top_pivots=())
    c=[b.close for b in bars]; n=len(c)
    gains=wilder([max(0.,c[i]-c[i-1]) if i else 0. for i in range(n)])
    losses=wilder([max(0.,c[i-1]-c[i]) if i else 0. for i in range(n)])
    rsi=[None if g is None else 50. if g==l==0 else 100. if l==0 else 100.-100./(1+g/l) for g,l in zip(gains,losses)]
    atr=wilder([max(b.high-b.low,abs(b.high-c[i-1]),abs(b.low-c[i-1])) if i else b.high-b.low for i,b in enumerate(bars)])
    sma=tuple(mean(c[-p:]) for p in (20,60,120))
    vol_ratio=bars[-1].volume/max(mean([b.volume for b in bars[-21:-1]]),1e-12)
    def side(bottom):
        values=[b.low if bottom else b.high for b in bars]
        # Plateaus get one deterministic rightmost pivot, no future beyond cutoff.
        piv=[i for i in range(n-60,n-2) if (values[i] <= min(values[i-2:i]) and values[i]<min(values[i+1:i+3]) if bottom else values[i]>=max(values[i-2:i]) and values[i]>max(values[i+1:i+3]))]
        pairs=[(a,b) for a in piv for b in piv if 5<=b-a<=40]
        pair=max(pairs,key=lambda p:(p[1],p[0])) if pairs else ()
        features=dict(double=False,divergence=False,extreme=False,volume=False,atr=False,neckline=False,ma=False)
        neckline=None
        if pair:
            a,b=pair
            features['double']=abs(values[b]-values[a])<=.5*max(atr[a],atr[b])
            features['divergence']=(rsi[b]>=rsi[a]+3. and values[b]<=values[a]+.5*atr[b]) if bottom else (rsi[b]<=rsi[a]-3. and values[b]>=values[a]-.5*atr[b])
            features['extreme']=min(rsi[a],rsi[b])<=30. if bottom else max(rsi[a],rsi[b])>=70.
            v1=mean([x.volume for x in bars[a-1:a+2]]);v2=mean([x.volume for x in bars[b-1:b+2]])
            features['volume']=v2/max(v1,1e-12)<=.8 and vol_ratio>=1.2
            features['atr']=atr[b]/max(atr[a],1e-12)<=.9
            neckline=max(x.high for x in bars[a+1:b]) if bottom else min(x.low for x in bars[a+1:b])
            features['neckline']=all(x>neckline for x in c[-2:]) if bottom else all(x<neckline for x in c[-2:])
            # A reclaim/loss requires actual pivot-to-current crossing, not merely position.
            features['ma']=sum(c[-1]>s and c[b]<s for s in sma)>=2 if bottom else sum(c[-1]<s and c[b]>s for s in sma)>=2
        weights=dict(double=.20,divergence=.15,extreme=.10,volume=.10,atr=.10,neckline=.20,ma=.15)
        score=sum(weights[k] for k,v in features.items() if v)
        confirmed=features['double'] and features['neckline'] and features['ma'] and score>=(.75 if bottom else .65)
        return min(1.,score),confirmed,features,neckline,pair
    bottom=side(True);top=side(False)
    return Wave(available=True,bottom_score=bottom[0],top_score=top[0],bottom_confirmed=bottom[1],top_confirmed=top[1],
                rsi=rsi[-1],sma=sma,atr=atr[-1],volume_ratio=vol_ratio,bottom_features=bottom[2],top_features=top[2],
                bottom_neckline=bottom[3],top_neckline=top[3],bottom_pivots=bottom[4],top_pivots=top[4])


def technical_evidence(fixture: Fixture,horizon,run_id):
    primary,higher={'1w':('30m','1d'),'1m':('1d','1w'),'1y':('1w','1mo')}[horizon]
    bars=fixture.bars.get(primary,()); upper=fixture.bars.get(higher,())
    w=analyze_wave(bars);h=analyze_wave(upper)
    bull=bear=None
    if w.available and h.available:
        above=sum(upper[-1].close>s for s in h.sma)/3
        bull=.4*w.bottom_confirmed+.4*above+.2*h.bottom_confirmed
        bear=.4*w.top_confirmed+.4*(1-above)+.2*h.top_confirmed
        if above==0: bull=min(.69,bull)
        if above==1: bear=min(.69,bear)
    from .schemas.contracts import select_as_of
    obs=select_as_of(fixture.observations,fixture.data_cutoff)
    flows=[];refs=[]
    for fid in ('foreign_net_buy','institution_net_buy','program_net_buy','semiconductor_relative_flow'):
        matches=[o for o in obs if o.factor_id==fid]
        if not matches: break
        latest=max(o.observed_at for o in matches);values=[o for o in matches if o.observed_at==latest]
        spec=next(s for s in fixture.factors if s.factor_id==fid)
        if (fixture.data_cutoff-latest).total_seconds()/86400>spec.max_age_days:break
        if len({o.value for o in values})>1: break
        flows.append(values[0].value);refs.append(str(values[0].observation_id))
    buy=sell=None
    if len(flows)==4 and w.available:
        buy=.2*(sum(v>0 for v in flows)+(bars[-1].close>bars[-2].close and w.volume_ratio>=1.2))
        sell=.2*(sum(v<0 for v in flows)+(bars[-1].close<bars[-2].close and w.volume_ratio>=1.2))
    timing=w.bottom_score-w.top_score
    # Feedback modifies interpretation once; raw flows are not added a second time.
    return TechnicalEvidence(batch_id=f'{run_id}/{horizon}/technical',primary=primary,higher=higher,wave=w,higher_wave=h,
        bullish_alignment=bull,bearish_alignment=bear,buy_liquidity=buy,sell_liquidity=sell,
        regime_effect=.15*timing if w.available else 0.,flow_effect=.1*timing if buy is not None else 0.,
        reflexivity_effect=.1*timing if bull is not None else 0.,evidence_refs=tuple(refs+[f'bars:{primary}',f'bars:{higher}']))
