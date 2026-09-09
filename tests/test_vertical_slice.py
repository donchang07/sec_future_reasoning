"""Core executable acceptance cases; oracles assert behavior, not fitted outputs."""
import json
from pathlib import Path
import pytest
from reasoning.fixture import Fixture
from reasoning.workflow import run_fixture
from reasoning.technical import analyze_wave
from reasoning.decision import decide
from reasoning.journal import SealedRun, write_journal, read_journal

ROOT = Path(__file__).resolve().parents[1]


def data():
    return json.loads((ROOT / "fixtures/samsung-preferred-v1.json").read_text())


def execute(raw):
    return run_fixture(Fixture.model_validate(raw))


def polar(raw, direction):
    specs = {x['factor_id']: x for x in raw['factors']}
    for o in raw['observations']:
        s = specs[o['factor_id']]
        o['value'] = s['baseline'] + direction * s['sign'] * s['scale'] * .9
    return raw


def test_all_positive():
    assert all(h.final.probabilities.up > h.final.probabilities.down for h in execute(polar(data(), 1)).horizons)


def test_all_negative():
    assert all(h.final.probabilities.down > h.final.probabilities.up for h in execute(polar(data(), -1)).horizons)


def test_hawkish_fomc():
    raw = data()
    baseline = execute(raw)
    raw['events'][0]['text'] = 'fomc fed us_10y_yield 6.0 percent'
    changed = execute(raw)
    assert changed.horizons[0].final.probabilities.down > baseline.horizons[0].final.probabilities.down


def test_priced_in_event():
    raw = data()
    raw['events'][0]['text'] = 'fomc fed us_10y_yield 6.0 percent'
    before = execute(raw)
    raw['events'][0]['pre_move'] = raw['events'][0]['expected_move']
    after = execute(raw)
    assert after.horizons[0].final.probabilities.down < before.horizons[0].final.probabilities.down


def test_missing_data():
    raw = data()
    raw['observations'] = [x for x in raw['observations'] if x['factor_id'] != 'us_10y_yield']
    assert all(x.final is None and x.decision.action == 'WAIT' for x in execute(raw).horizons)


def test_conflicting_source():
    raw = data()
    baseline = execute(raw)
    import uuid
    o = dict(next(x for x in reversed(raw['observations']) if x['factor_id'] == 'us_10y_yield'))
    o.update(source_id='conflicting_source', observation_id=str(uuid.UUID(int=999)), value=9.)
    raw['observations'].append(o)
    assert execute(raw).horizons[0].final.confidence < baseline.horizons[0].final.confidence


def test_double_count_prevention():
    raw = data()
    before = execute(raw)
    edge = dict(raw['edges'][0]); edge['edge_id'] += '_duplicate'
    raw['edges'].append(edge)
    after = execute(raw)
    assert after.horizons[0].final.probabilities == before.horizons[0].final.probabilities
    assert any('duplicate_root' in x.adjustment_codes for r in after.executions if r.engine_id == 'E09' for x in r.result.output_artifact.payload.items)


def test_horizon_divergence():
    raw = polar(data(), 1)
    specs = {s['factor_id']: s for s in raw['factors']}
    for o in raw['observations']:
        s = specs[o['factor_id']]
        if s['module'] in ('macro','capital_flow','market_regime','preferred'):
            o['value'] = s['baseline'] - s['sign'] * s['scale'] * .9
    h = execute(raw).horizons
    assert h[0].final.probabilities.down > h[0].final.probabilities.up
    assert h[2].final.probabilities.up > h[2].final.probabilities.down


def test_false_bottom():
    raw = data()
    for b in raw['bars']['30m'][-2:]:
        b.update(open=49000., close=49000., low=48500., high=49500.)
    wave = analyze_wave(Fixture.model_validate(raw).bars['30m'])
    assert not wave.bottom_confirmed


def test_true_bottom():
    assert analyze_wave(Fixture.model_validate(data()).bars['30m']).bottom_confirmed


def gates(**changes):
    values = dict(up=.8, down=.1, no_history_up=.8, no_history_down=.1, confidence=.8,
                  bottom=.9, top=.9, bottom_confirmed=True, top_confirmed=True,
                  bullish_alignment=.9, bearish_alignment=.9, buy_liquidity=.8,
                  sell_liquidity=.8, fatal=False, held=False)
    values.update(changes)
    return decide(**values)


def test_low_confidence_no_action():
    assert gates(confidence=.69).action == 'WAIT'


@pytest.mark.parametrize('up,action', [(.79,'WAIT'),(.80,'ENTRY')])
def test_entry_boundary(up, action):
    assert gates(up=up, no_history_up=up).action == action


@pytest.mark.parametrize('down,action', [(.69,'HOLD'),(.70,'SELL')])
def test_sell_boundary(down, action):
    assert gates(up=.1, down=down, no_history_down=down, held=True).action == action


def test_technical_only_forbidden():
    assert gates(up=.4, down=.35).action == 'WAIT'
    assert gates(bottom_confirmed=False).action == 'WAIT'
    assert gates(buy_liquidity=.59).action == 'WAIT'
    assert gates(no_history_up=.79).action == 'WAIT'


def test_determinism_ledger_feedback_and_seal(tmp_path):
    first = execute(data()); second = execute(data())
    assert first == second
    assert len(first.executions) == 114
    assert all(r.result.status == 'success' for r in first.executions)
    for h in first.horizons:
        assert h.initial.probabilities != h.final.probabilities
        p = list(h.final.prior.vector())
        for row in h.final.ledger:
            p = [a+b/100 for a,b in zip(p,row.delta_pp)]
        assert p == pytest.approx(h.final.probabilities.vector())
        assert h.positive_paths and h.negative_paths
    sealed = SealedRun.seal(first)
    path = tmp_path/'journal.json'
    write_journal(path,sealed); write_journal(path,sealed)
    assert read_journal(path) == sealed
    raw = json.loads(path.read_text()); raw['snapshot']['horizons'][0]['explanation'] += 'tamper'
    with pytest.raises(ValueError):
        SealedRun.model_validate(raw)
