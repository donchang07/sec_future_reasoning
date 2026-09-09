"""Computational and failure invariants beyond the fifteen core scenarios."""
import json
from pathlib import Path
import pytest
from reasoning.fixture import Fixture
from reasoning.workflow import run_fixture
from reasoning.technical import analyze_wave
from reasoning.journal import SealedRun,write_journal

ROOT=Path(__file__).resolve().parents[1]


def raw():return json.loads((ROOT/'fixtures/samsung-preferred-v1.json').read_text())
def run(d=None):return run_fixture(Fixture.model_validate(d or raw()))
def payload(j,e,g=1,h='1w'):
    return next(r.result.output_artifact.payload for r in j.executions if (r.engine_id,r.generation,r.horizon)==(e,g,h))


def test_each_engine_computes_structured_output():
    j=run()
    s=payload(j,'E01').items[0]
    # The yield series declines across four observations: latest rank is 1/4.
    assert s.change<0 and s.velocity is not None and s.acceleration is not None and s.percentile==.25
    e=payload(j,'E02').items[0]
    assert e.actual==4. and e.actor_ids==('fed',) and e.evidence_spans[0].end>0
    assert payload(j,'E03').items[0].scale>0
    assert payload(j,'E04').items[0].priced_in_fraction==0.  # No surprise to price in.
    assert payload(j,'E05').positive_refs and payload(j,'E05').negative_refs
    assert len(payload(j,'E06').items)==9 and all(m.score is not None for m in payload(j,'E06').items)
    assert {h.direction for h in payload(j,'E07').items}=={'up','down','flat'}
    assert all(len(p.edge_ids)==2 for p in payload(j,'E08').items)
    assert any(x.adjusted_effect!=0 for x in payload(j,'E09').items)
    actor=payload(j,'E10').items[0]
    assert actor.response_range.low<actor.response_range.high and actor.feedback_refs
    assert all(x.valid for x in payload(j,'E11').items)
    assert any(x.effect!=0 for x in payload(j,'E12').items)
    history=payload(j,'E13')
    assert history.applicable and history.sample_count==1 and history.relevance>0
    assert payload(j,'E14').claims and not payload(j,'E14').fatal
    assert len({s.shock_distributions[0].location for s in payload(j,'E15').items})==4
    assert all(s.valid for s in payload(j,'E16').items)
    assert all(sum(s.class_counts)==s.samples for s in payload(j,'E17').items)
    assert payload(j,'E18').forecast.ledger and payload(j,'E19').publishable


def test_true_top_from_mirrored_raw_bars():
    d=raw()
    for b in d['bars']['30m']:
        o,h,l,c=(b[k] for k in ('open','high','low','close'))
        b.update(open=120000-o,high=120000-l,low=120000-h,close=120000-c)
    w=analyze_wave(Fixture.model_validate(d).bars['30m'])
    assert w.top_confirmed and w.top_features['divergence'] and w.top_features['neckline']
    assert not w.bottom_confirmed


def test_feedback_changes_only_interpretation_not_observations():
    j=run()
    assert payload(j,'E01',0)==payload(j,'E01',1)
    for before,after in zip(payload(j,'E06',0).items,payload(j,'E06',1).items):
        assert (before!=after)==(before.module_id in ('market_regime','capital_flow'))
    assert payload(j,'E10',0)!=payload(j,'E10',1)
    assert {r.generation for r in j.executions}=={0,1}


def test_constraint_violation_blocks_meta_and_decision():
    d=raw();d['accounting']['production']=120.
    j=run(d)
    assert not payload(j,'E19').publishable
    assert payload(j,'E14').fatal
    assert all(h.decision.action=='WAIT' for h in j.horizons)


def test_no_observations_remains_unknown():
    d=raw();d['observations']=[]
    j=run(d)
    assert all(h.final is None for h in j.horizons)
    assert all(m.direction=='unknown' and m.score is None for m in payload(j,'E06').items)


def test_history_cannot_flip_decision_or_exceed_cap():
    d=raw();d['history']=[]
    no_history=run(d);j=run()
    for h,other in zip(j.horizons,no_history.horizons):
        diff=[abs(p-q) for p,q in zip(h.final.probabilities.vector(),h.final.without_history_probabilities.vector())]
        assert max(diff)<=.05 and sum(diff)<=.1
        assert h.final.without_history_probabilities==other.final.probabilities


def test_short_bar_history_blocks_timing():
    d=raw();d['bars']['30m']=d['bars']['30m'][-20:]
    h=run(d).horizons[0]
    assert not h.technical.wave.available and h.technical.bullish_alignment is None
    assert h.decision.action=='WAIT'


@pytest.mark.parametrize('mutation', ['future_bar','future_consensus','cycle','unit'])
def test_invalid_inputs_rejected(mutation):
    d=raw()
    if mutation=='future_bar':d['bars']['30m'][-1]['closed_at']='2030-01-01T00:00:00Z'
    elif mutation=='future_consensus':d['events'][0]['consensus_at']='2030-01-01T00:00:00Z'
    elif mutation=='cycle':
        e=dict(d['edges'][0]);e.update(edge_id='cycle',source=e['target'],target=e['source']);d['edges'].append(e)
    else:d['observations'][0]['unit']='wrong_unit'
    with pytest.raises(ValueError):Fixture.model_validate(d)


def test_no_overwrite_and_resealed_policy_tamper_rejected(tmp_path):
    first=SealedRun.seal(run());p=tmp_path/'journal.json';write_journal(p,first)
    d=raw();d['held']=True
    with pytest.raises(ValueError,match='immutable'):write_journal(p,SealedRun.seal(run(d)))
    d=first.snapshot.model_dump(mode='json');d['horizons'][0]['decision']['action']='ENTRY'
    from reasoning.journal import RunJournal
    with pytest.raises(ValueError,match='policy gates'):RunJournal.model_validate(d)


def test_opposite_pre_move_does_not_price_in_event():
    d=raw();d['events'][0]['text']='fomc fed us_10y_yield 3.0 percent'
    assert payload(run(d),'E04').items[0].priced_in_fraction==0.


def test_missing_consensus_lowers_confidence():
    d=raw();d['events'][0]['consensus']=[]
    assert run(d).horizons[0].final.confidence<run().horizons[0].final.confidence


def test_bear_falsifier_requires_economic_improvement():
    j=run();bear=next(h for h in payload(j,'E07').items if h.direction=='down')
    capacity=next(f for f in bear.falsifiers if f.factor_id=='cxmt_memory_capacity')
    assert capacity.operator=='lt'
