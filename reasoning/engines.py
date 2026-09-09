"""Nineteen deterministic research algorithms using the Foundation payloads."""
from dataclasses import dataclass, field
from datetime import timedelta
from math import exp, log, sqrt, prod
from random import Random
from statistics import mean, pstdev
from uuid import uuid5, NAMESPACE_URL
from .fixture import Fixture
from .technical import TechnicalEvidence
from .schemas.contracts import (VersionBundle, Forecast, ProbabilityVector, Contribution,
    Falsifier, select_as_of, MODULE_IDS, ENGINE_IDS)
from .schemas.artifacts import Artifact, EngineResult, Warning, PAYLOAD_TYPES

DAYS={'1w':7,'1m':30,'1y':365}
WEIGHTS={
    '1w':(.20,.05,.08,.03,.08,.20,.08,.10,.18),
    '1m':(.15,.12,.15,.08,.15,.10,.10,.08,.07),
    '1y':(.10,.15,.15,.15,.18,.03,.12,.07,.05),
}


def clip(x,low=-1.,high=1.): return max(low,min(high,x))
def uid(value): return uuid5(NAMESPACE_URL,str(value))
def softmax(values):
    m=max(values);v=[exp(x-m) for x in values];s=sum(v)
    return tuple(x/s for x in v)
def probability(v): return ProbabilityVector(up=v[0],down=v[1],flat=v[2])


@dataclass
class EngineRunner:
    fixture: Fixture
    versions: VersionBundle
    run_id: object
    horizon: str
    generation: int
    technical: TechnicalEvidence | None = None
    artifacts: dict = field(default_factory=dict)

    def ident(self,key): return uid(f'{self.run_id}/{self.horizon}/{self.generation}/{key}')
    def get(self,engine): return self.artifacts[engine].payload
    @property
    def specs(self): return {x.factor_id:x for x in self.fixture.factors}
    @property
    def signals(self): return {x.factor_id:x for x in self.get('E01').items}
    def refs(self): return tuple(str(o.observation_id) for o in self.fixture.observations if o.available_at<=self.fixture.data_cutoff)

    def execute(self,engine):
        if engine=='E18' and any(self.specs[k].critical for k in self.get('E05').missing_ids):
            return EngineResult(status='insufficient_evidence',trace_id=self.ident(engine+'/trace'),
                warnings=(Warning(code='critical_missing',message='Critical factor unavailable at cutoff',
                                  evidence_refs=self.get('E05').missing_ids),))
        values=getattr(self,engine)()
        if 'items' in values and not values['items']:
            values.update(applicable=False,reason='No eligible inputs after validation')
        payload=PAYLOAD_TYPES[engine].model_validate(values)
        evidence=self.refs() or ('fixture:missing_observations',)
        if self.technical:
            evidence+=self.technical.evidence_refs
        artifact=Artifact(artifact_id=self.ident(engine),run_id=self.run_id,engine_id=engine,
            engine_version=next(x.version for x in self.versions.engines if x.engine_id==engine),
            created_at=self.fixture.data_cutoff,data_cutoff=self.fixture.data_cutoff,
            input_artifact_ids=tuple(x.artifact_id for x in self.artifacts.values()),evidence_refs=evidence,payload=payload)
        self.artifacts[engine]=artifact
        confidence=payload.forecast.confidence if engine=='E18' else getattr(payload,'confidence',None)
        if confidence is None:
            confidence=mean(x.quality for x in self.get('E01').items) if self.get('E01').items else 0.
        return EngineResult(status='success',output_artifact=artifact,confidence=confidence,
            evidence_refs=evidence,trace_id=self.ident(engine+'/trace'))

    def E01(self):
        selected=select_as_of(self.fixture.observations,self.fixture.data_cutoff);items=[]
        for fid,spec in self.specs.items():
            obs=[o for o in selected if o.factor_id==fid]
            if not obs: continue
            times=sorted({o.observed_at for o in obs});latest=times[-1]
            if (self.fixture.data_cutoff-latest).total_seconds()/86400>spec.max_age_days: continue
            levels=[mean(o.value for o in obs if o.observed_at==t) for t in times]
            values=[o.value for o in obs if o.observed_at==latest]
            spread=max(values)-min(values)
            quality=min(1.,len(times)/4)*max(.1,1.-spread/spec.scale)
            change=levels[-1]-levels[-2] if len(levels)>1 else None
            previous=levels[-2]-levels[-3] if len(levels)>2 else None
            items.append(dict(factor_id=fid,observation_ids=tuple(o.observation_id for o in obs),unit=spec.unit,
                level=levels[-1],change=change,velocity=change,acceleration=change-previous if previous is not None else None,
                percentile=sum(v<=levels[-1] for v in levels)/len(levels),
                normalized=clip((levels[-1]-spec.baseline)/spec.scale),quality=quality))
        return dict(items=items)

    def E02(self):
        items=[]
        for raw in self.fixture.events:
            tokens=raw.text.split()
            if len(tokens)!=5: raise ValueError('event grammar: type actor factor actual unit')
            kind,actor,factor,actual,unit=tokens
            if factor not in self.specs or unit!=self.specs[factor].unit or actor not in ('fed','samsung','foreign_investors'):
                raise ValueError('event entity/unit not in fixture ontology')
            items.append(dict(event_id=uid(raw.event_id),event_type=kind,actor_ids=(actor,),factor_refs=(factor,),actual=float(actual),
                unit=unit,occurred_at=raw.occurred_at,published_at=raw.published_at,
                evidence_spans=(dict(evidence_ref=f'event:{raw.event_id}',start=0,end=len(raw.text)),)))
        return dict(items=items)

    def E03(self):
        items=[]
        for e,raw in zip(self.get('E02').items,self.fixture.events):
            known=len(raw.consensus)>=2 and pstdev(raw.consensus)>0
            scale=pstdev(raw.consensus) if known else None
            expected=mean(raw.consensus) if known else None
            items.append(dict(event_id=e.event_id,actual=e.actual,expected=expected,scale=scale,
                surprise=(e.actual-expected)/scale if known else None,
                consensus_ids=tuple(f'consensus:{raw.event_id}:{i}' for i in range(len(raw.consensus)))))
        return dict(items=items)

    def E04(self):
        items=[]
        for surprise,raw in zip(self.get('E03').items,self.fixture.events):
            # Only a pre-move in the same direction can price in a surprise.
            fraction=(clip(abs(raw.pre_move)/raw.expected_move,0.,1.) if raw.pre_move*surprise.surprise>0 else 0.) if surprise.surprise is not None else None
            items.append(dict(event_id=surprise.event_id,surprise_id=uid(f'{surprise.event_id}/surprise'),
                priced_in_fraction=fraction,residual_shock=surprise.surprise*(1-fraction) if fraction is not None else None,
                pre_event_start=raw.pre_start,pre_event_end=raw.pre_end))
        return dict(items=items)

    def factor_effects(self):
        effects={fid:s.normalized*self.specs[fid].sign for fid,s in self.signals.items()}
        for event,residual in zip(self.get('E02').items,self.get('E04').items):
            fid=event.factor_refs[0]
            if fid in effects and residual.residual_shock is not None:
                effects[fid]=clip(effects[fid]+.5*clip(residual.residual_shock)*self.specs[fid].sign)
        return effects

    def E05(self):
        effects=self.factor_effects()
        positive=tuple(k for k,v in effects.items() if v>0);negative=tuple(k for k,v in effects.items() if v<0)
        modules=sorted(MODULE_IDS,key=lambda m:-sum(abs(v) for k,v in effects.items() if self.specs[k].module==m))
        return dict(theme_ids=tuple(f'{m}_pressure' for m in modules[:3]),positive_refs=positive,negative_refs=negative,
            conflict_ids=tuple(k for k,s in self.signals.items() if s.quality<.5),
            missing_ids=tuple(k for k in self.specs if k not in self.signals),dominant_module_ids=tuple(modules[:3]))

    def E06(self):
        effects=self.factor_effects();items=[]
        for module in MODULE_IDS:
            expected=[s for s in self.fixture.factors if s.module==module]
            keys=[s.factor_id for s in expected if s.factor_id in effects]
            coverage=len(keys)/max(1,len(expected))
            contributions={k:effects[k]*self.signals[k].quality/max(1,len(expected)) for k in keys}
            if keys and self.technical and module in ('market_regime','capital_flow'):
                feedback=self.technical.regime_effect if module=='market_regime' else self.technical.flow_effect
                contributions={k:clip(v+feedback/len(keys),-1/len(keys),1/len(keys)) for k,v in contributions.items()}
            score=100*clip(sum(contributions.values())) if keys else None
            items.append(dict(module_id=module,score=score,direction='unknown' if score is None else 'positive' if score>0 else 'negative' if score<0 else 'neutral',
                momentum=mean(self.signals[k].velocity or 0. for k in keys) if keys else None,
                regime='risk_on' if score is not None and score>=0 else 'risk_off' if keys else None,
                confidence=mean(self.signals[k].quality for k in keys)*coverage if keys else None,coverage=coverage,
                top_factors=tuple(dict(factor_id=k,contribution=v) for k,v in contributions.items()),
                outgoing_effects=(dict(target='preferred',effect=(score or 0.)/100,lag_days=0.),) if keys and module!='preferred' else ()))
        return dict(items=items)

    def E07(self):
        s=self.get('E05');items=[]
        for direction in ('up','down','flat'):
            support=s.positive_refs if direction=='up' else s.negative_refs if direction=='down' else s.conflict_ids
            contradict=s.negative_refs if direction=='up' else s.positive_refs if direction=='down' else s.positive_refs+s.negative_refs
            falsifiers=tuple(Falsifier(factor_id=k,operator='lt' if self.specs[k].sign*(1 if direction=='up' else -1)>0 else 'gt',threshold=self.specs[k].baseline,
                unit=self.specs[k].unit,horizon=self.horizon,evidence_refs=(k,)) for k in support[:3] if k in self.specs)
            items.append(dict(hypothesis_id=self.ident(f'hypothesis/{direction}'),direction=direction,horizon=self.horizon,
                claim_codes=(f'{direction}_economic_case',),support_refs=support,contradict_refs=contradict,falsifiers=falsifiers))
        return dict(items=items)

    def E08(self):
        items=[];graph={}
        for edge in self.fixture.edges: graph.setdefault(edge.source,[]).append(edge)
        contributions={x.factor_id:x.contribution for m in self.get('E06').items for x in m.top_factors}
        counts={m:sum(s.module==m for s in self.fixture.factors) for m in MODULE_IDS}
        for fid,value in contributions.items():
            spec=self.specs[fid]
            # State contributions already carry the economic sign; graph edges
            # apply it explicitly during traversal, preserving inspectable paths.
            raw=value*counts[spec.module]*spec.sign
            def walk(node,nodes,edges):
                if node=='preferred_price':
                    effect=raw*prod(e.sign*e.strength for e in edges)
                    direction='up' if effect>=0 else 'down'
                    items.append(dict(path_id='/'.join(e.edge_id for e in edges),hypothesis_id=self.ident(f'hypothesis/{direction}'),
                        node_ids=tuple(nodes),edge_ids=tuple(e.edge_id for e in edges),root_evidence_group=spec.root_group,
                        sign=1 if effect>=0 else -1,strength=min(1.,abs(effect)),confidence=prod(e.confidence for e in edges),graph_version=self.versions.graph))
                    return
                if len(edges)>=6:return
                for edge in sorted(graph.get(node,[]),key=lambda e:e.edge_id):
                    if edge.target not in nodes: walk(edge.target,nodes+[edge.target],edges+[edge])
            walk(fid,[fid],[])
        return dict(items=items)

    def E09(self):
        groups={};items=[]
        for p in self.get('E08').items:groups.setdefault(p.root_evidence_group,[]).append(p)
        for group,paths in sorted(groups.items()):
            representative=min(paths,key=lambda p:(-p.strength*p.confidence,p.path_id))
            for p in sorted(paths,key=lambda p:p.path_id):
                original=p.sign*p.strength*p.confidence
                items.append(dict(path_id=p.path_id,original_effect=original,adjusted_effect=original if p==representative else 0.,
                    adjustment_codes=() if p==representative else ('duplicate_root',),
                    competing_refs=tuple(x.path_id for x in paths if x!=p),root_group=group))
        return dict(items=items)

    def E10(self):
        modules={m.module_id:m for m in self.get('E06').items}
        flow=(modules['capital_flow'].score or 0.)/100;trend=(modules['market_regime'].score or 0.)/100
        response=clip(.15*flow+.1*trend+(self.technical.reflexivity_effect if self.technical else 0.),-.25,.25)
        return dict(items=(dict(actor_id='foreign_investors',trigger_refs=tuple(x.factor_id for x in modules['capital_flow'].top_factors),
            action_code='accumulate' if response>0 else 'distribute' if response<0 else 'hold',
            response_range=dict(low=max(-.25,response-.03),high=min(.25,response+.03)),constraint_refs=('actor_exposure_cap',),
            feedback_refs=(self.technical.batch_id,) if self.technical else ()),))

    def E11(self):
        a=self.fixture.accounting
        rows=[('capacity',a.production,a.capacity,a.production<=a.capacity),
              ('revenue_identity',a.revenue,a.units_sold*a.unit_price,abs(a.revenue-a.units_sold*a.unit_price)<=.01),
              ('cash_identity',a.cash_flow,a.operating_cash-a.capex,abs(a.cash_flow-(a.operating_cash-a.capex))<=.01)]
        return dict(items=tuple(dict(target_id='samsung',constraint_id=k,lhs=l,rhs=r,tolerance=.01,valid=v,evidence_refs=(f'accounting:{k}',)) for k,l,r,v in rows))

    def E12(self):
        paths={p.path_id:p for p in self.get('E08').items};edges={e.edge_id:e for e in self.fixture.edges};items=[]
        weights=dict(zip(MODULE_IDS,WEIGHTS[self.horizon]))
        counts={m:sum(s.module==m for s in self.fixture.factors) for m in MODULE_IDS}
        for a in self.get('E09').items:
            p=paths[a.path_id];es=[edges[k] for k in p.edge_ids];lag=sum(e.lag_days for e in es)
            active=clip((DAYS[self.horizon]-lag)/max(e.duration_days for e in es),0.,1.)
            module=self.specs[p.node_ids[0]].module
            decay=exp(-max(0.,DAYS[self.horizon]-30)/3650)
            effect=a.adjusted_effect*active*decay*weights[module]/max(1,counts[module])
            items.append(dict(path_id=p.path_id,horizon=self.horizon,lag_hours=lag*24,active_fraction=active,decay=decay,effect=effect))
        return dict(items=items)

    def E13(self):
        modules=self.get('E06').items;vector=[(m.score or 0.)/100 for m in modules]
        regime=modules[-1].regime;eligible=[]
        for h in self.fixture.history:
            if len(h.vector)!=len(vector): continue
            denom=sqrt(sum(x*x for x in vector)*sum(x*x for x in h.vector))
            similarity=max(0.,sum(a*b for a,b in zip(vector,h.vector))/denom) if denom else 0.
            if similarity>=.8 and h.regime==regime and all(m.coverage==1 for m in modules):
                eligible.append((h,min(1.,similarity),2**(-(self.fixture.data_cutoff-h.matured_at).days/365)))
        relevance=mean(s*r for h,s,r in eligible)*min(len(eligible)/100,1.) if eligible else 0.
        delta=[0.,0.,0.]
        for h,s,r in eligible:
            for i,direction in enumerate(('up','down','flat')):
                delta[i]+=(float(h.outcome==direction)-1/3)*relevance/max(1,len(eligible))*.05
        return dict(applicable=bool(eligible),reason=None if eligible else 'No mature same-regime analogy above similarity gate',
            case_ids=tuple(h.case_id for h,s,r in eligible),similarity=mean(s for h,s,r in eligible) if eligible else None,
            recency=mean(r for h,s,r in eligible) if eligible else None,sample_count=len(eligible),regime_match=bool(eligible),
            relevance=relevance,capped_delta=tuple(delta))

    def E14(self):
        situation=self.get('E05');temporal=self.get('E12').items
        positive=sum(max(0.,p.effect) for p in temporal);negative=sum(max(0.,-p.effect) for p in temporal)
        conflict=min(positive,negative)/max(positive+negative,1e-12)
        critical=tuple(k for k in situation.missing_ids if self.specs[k].critical)
        invalid=tuple(x.constraint_id for x in self.get('E11').items if not x.valid)
        fatal=bool(critical or invalid)
        quality=mean(m.confidence or 0. for m in self.get('E06').items)
        unknown_consensus=tuple(str(s.event_id) for s in self.get('E03').items if s.surprise is None)
        confidence=clip(quality*(1-.5*conflict)/(1+.25*len(unknown_consensus)),0.,1.)
        refs=critical+invalid+situation.conflict_ids
        claims=[]
        if unknown_consensus:claims.append(dict(claim_code='missing_consensus',evidence_refs=unknown_consensus,confidence=1.))
        if negative: claims.append(dict(claim_code='bearish_counterevidence',evidence_refs=situation.negative_refs or ('causal:negative',),confidence=conflict))
        if positive: claims.append(dict(claim_code='bullish_counterevidence',evidence_refs=situation.positive_refs or ('causal:positive',),confidence=conflict))
        return dict(claims=claims,refutation_refs=refs,severity='fatal' if fatal else 'warning' if refs or conflict>.2 else 'none',
            fatal=fatal,replacement_hypothesis_id=self.ident('hypothesis/flat') if fatal else None,confidence=confidence)

    def E15(self):
        effect=sum(p.effect for p in self.get('E12').items)
        actor=self.get('E10').items[0].response_range
        center=effect*.15+(actor.low+actor.high)/2*.03
        scale=.035*sqrt(DAYS[self.horizon]/7)*(1+(1-self.get('E14').confidence))
        weights=softmax((1.,effect,-effect,-1.5));items=[]
        for kind,offset,w in zip(('base','upside','downside','tail'),(0.,scale,-scale,-2*scale),weights):
            location=center+offset
            items.append(dict(scenario_id=self.ident(f'scenario/{kind}'),scenario_kind=kind,
                hypothesis_id=self.ident('hypothesis/up' if location>=0 else 'hypothesis/down'),prior_weight=w,overrides=(),
                shock_distributions=(dict(distribution_id=f'{kind}_return',factor_id='samsung_preferred_price',family='normal',
                    location=location,scale=scale,version=self.versions.model),),constraint_refs=tuple(x.constraint_id for x in self.get('E11').items)))
        return dict(items=items)

    def E16(self):
        scenarios=self.get('E15').items;weight=sum(s.prior_weight for s in scenarios);items=[]
        constraints=all(c.valid for c in self.get('E11').items)
        hypotheses={h.hypothesis_id for h in self.get('E07').items}
        for s in scenarios:
            errors=[]
            if abs(weight-1)>1e-9:errors.append('scenario_weight_sum')
            if not constraints:errors.append('accounting_violation')
            if s.hypothesis_id not in hypotheses:errors.append('unknown_hypothesis')
            if any(d.factor_id not in self.specs or d.scale<=0 for d in s.shock_distributions):errors.append('invalid_distribution')
            if any(o.factor_id not in self.specs or o.unit!=self.specs[o.factor_id].unit for o in s.overrides):errors.append('invalid_override')
            items.append(dict(scenario_id=s.scenario_id,valid=not errors,violations=tuple(errors),
                accepted_distribution_refs=tuple(d.distribution_id for d in s.shock_distributions) if not errors else ()))
        return dict(items=items)

    def E17(self):
        valid={s.scenario_id for s in self.get('E16').items if s.valid};items=[]
        anchor=self.signals.get('samsung_preferred_price')
        if anchor is None:return dict(items=())
        for index,s in enumerate(self.get('E15').items):
            if s.scenario_id not in valid:continue
            seed=self.fixture.seed+DAYS[self.horizon]*10+index
            rng=Random(seed);d=s.shock_distributions[0];n=2048
            values=sorted(rng.gauss(d.location,d.scale) for _ in range(n))
            band=.01*sqrt(DAYS[self.horizon]/7)
            counts=(sum(x>band for x in values),sum(x<-band for x in values),sum(-band<=x<=band for x in values))
            items.append(dict(scenario_id=s.scenario_id,seed=seed,samples=n,return_quantiles=tuple(values[int((n-1)*q)] for q in (.1,.5,.9)),
                class_counts=counts,price_anchor=anchor.level,distribution_version=self.versions.model))
        return dict(items=items)

    def E18(self):
        prior=(.4,.35,.25);current=prior;ledger=[]
        def append(next_p,engine,stage,refs,edges=()):
            nonlocal current
            ledger.append(Contribution(sequence=len(ledger),stage=stage,engine_id=engine,version=self.versions.model,
                evidence_refs=tuple(refs),edge_ids=tuple(edges),before=probability(current),after=probability(next_p),
                delta_pp=tuple(100*(b-a) for a,b in zip(current,next_p))))
            current=next_p
        paths={p.path_id:p for p in self.get('E08').items}
        for row in self.get('E12').items:
            if not row.effect:continue
            x=3*row.effect;p=paths[row.path_id]
            append(softmax(tuple(log(v)+d for v,d in zip(current,(x,-x,-abs(x)/2)))),'E12','causal',(p.root_evidence_group,),p.edge_ids)
        actor=self.get('E10').items[0];x=(actor.response_range.low+actor.response_range.high)/2
        append(softmax(tuple(log(v)+d for v,d in zip(current,(x,-x,0.)))),'E10','causal',actor.trigger_refs+actor.feedback_refs)
        scenarios={s.scenario_id:s for s in self.get('E15').items};simulation=self.get('E17').items
        if simulation:
            total=sum(scenarios[s.scenario_id].prior_weight for s in simulation)
            sim=tuple(sum(scenarios[s.scenario_id].prior_weight*(s.class_counts[i]+1)/(s.samples+3) for s in simulation)/total for i in range(3))
            append(softmax(tuple(.8*log(p)+.2*log(s) for p,s in zip(current,sim))),'E17','scenario',tuple(str(s.scenario_id) for s in simulation))
        challenge=self.get('E14');mix=.15*(1-challenge.confidence)
        append(tuple((1-mix)*p+mix/3 for p in current),'E14','challenge',tuple(c.claim_code for c in challenge.claims))
        without=softmax(tuple(log(p)/1.15 for p in current))
        history=self.get('E13');delta=history.capped_delta
        scale=min([1.]+[current[i]/-d for i,d in enumerate(delta) if d<0])
        append(tuple(p+scale*d for p,d in zip(current,delta)),'E13','history',history.case_ids)
        append(softmax(tuple(log(max(p,1e-15))/1.15 for p in current)),'E18','calibration',('temperature:1.15',))
        diff=[p-q for p,q in zip(current,without)];maxdiff=max(abs(x) for x in diff);l1=sum(abs(x) for x in diff)
        cap=min(1.,.05/max(maxdiff,1e-12),.10/max(l1,1e-12))
        if cap<1:append(tuple(q+cap*d for q,d in zip(without,diff)),'E13','history_cap',history.case_ids)
        anchor=self.signals['samsung_preferred_price'].level
        low=min((s.return_quantiles[0] for s in simulation),default=0.)
        high=max((s.return_quantiles[2] for s in simulation),default=0.)
        forecast=Forecast(forecast_id=self.ident('forecast'),run_id=self.run_id,horizon=self.horizon,data_cutoff=self.fixture.data_cutoff,
            target_at=self.fixture.data_cutoff+timedelta(days=DAYS[self.horizon]),versions=self.versions,prior=probability(prior),
            probabilities=probability(current),without_history_probabilities=probability(without),ledger=tuple(ledger),
            confidence=challenge.confidence,price_low=max(0.,anchor*(1+low)),price_high=max(0.,anchor*(1+high)),
            calibration_status='unvalidated',evidence_refs=self.refs(),falsifiers=tuple(f for h in self.get('E07').items for f in h.falsifiers))
        return dict(forecast=forecast)

    def E19(self):
        failed=[];offenders=[];forecast=self.get('E18').forecast if 'E18' in self.artifacts else None
        if forecast is None:failed.append('missing_forecast');offenders.append('E18')
        if self.get('E14').fatal:failed.append('fatal_challenge');offenders.append('E14')
        if any(not s.valid for s in self.get('E16').items):failed.append('invalid_scenario');offenders.append('E16')
        if forecast:
            # Revalidation reconstructs every delta and verifies cutoff/normalization.
            Forecast.model_validate_json(forecast.model_dump_json())
            if max(abs(p-q) for p,q in zip(forecast.probabilities.vector(),forecast.without_history_probabilities.vector()))>.050000001:
                failed.append('history_cap');offenders.append('E13')
        drivers=tuple(p.path_id for p in sorted(self.get('E12').items,key=lambda p:-abs(p.effect))[:5])
        if not drivers:failed.append('missing_drivers');offenders.append('E08')
        return dict(publishable=not failed,failed_checks=tuple(failed),offending_engines=tuple(offenders),driver_refs=drivers,
            falsifiers=forecast.falsifiers if forecast else (),error_class='insufficient_evidence' if failed else None)
