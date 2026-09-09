"""Adapter tests use authored mock documents, never published as live evidence."""
import base64
import hashlib
import io
import zipfile
from datetime import datetime, timedelta, timezone
import pytest
from reasoning.act_sources import (
    Document, Fact, assess, export_fact, financial_facts, select_nowcasts,
    spot_facts, statement_checks, hwpx_text, collect_document,
)
from reasoning.live import write_immutable

NOW = datetime(2026, 9, 9, 7, tzinfo=timezone.utc)


def document(source='samsung_bs', body=b'mock', fmt='pdf'):
    return Document(source_id=source, provider='authored test response', url='https://example.invalid', format=fmt,
        requested_at=NOW-timedelta(seconds=1), collected_at=NOW, status='available', http_status=200,
        body_base64=base64.b64encode(body).decode(), sha256=hashlib.sha256(body).hexdigest())


HEADER = 'Samsung Electronics Co., Ltd. and its subsidiaries\nIn millions of Korean won\nJune 30, December 31, Notes 2026 2025 2026 2025\n'


def test_financial_independent_balance_identity():
    facts = financial_facts(document(), HEADER+'Total assets 300 200 3 2\nTotal liabilities 100 50 1 0\nTotal equity 200 150 2 1\nTotal liabilities and equity 300 200 3 2')
    assert statement_checks(facts)[0].passed
    changed = [f.model_copy(update={'value': 90.}) if f.factor_id == 'samsung_total_liabilities' else f for f in facts]
    check = statement_checks(changed)[0]
    assert not check.passed and check.residual == 10.


def test_financial_h1_is_not_quarter_or_usd():
    facts = financial_facts(document('samsung_soi'), HEADER+'Revenue 27 10 20 30 40 50 60 70 80\nOperating profit 27 1 2 3 4 5 6 7 8')
    assert [f.value for f in facts] == [50., 5.]
    assert all(f.unit == 'krw_million' and f.mapping == 'unmapped' for f in facts)


def test_financial_column_drift_rejected():
    with pytest.raises(ValueError, match='column count'):
        financial_facts(document(), HEADER+'Total assets 1 2\nTotal liabilities 1 2\nTotal equity 1 2')


def test_wrong_issuer_rejected():
    with pytest.raises(ValueError, match='issuer'):
        financial_facts(document(), HEADER.replace('Electronics', 'Electro-Mechanics'))


def spot_html():
    headers = ['Item', 'Daily High', 'Daily Low', 'Session High', 'Session Low', 'Session Average', 'Session Change', 'History']
    cells = ['DDR4 8Gb (1Gx8) 3200', '12', '8', '11', '9', '10', '1 %', '']
    return ('<div id="dram_spot">Last Update 2026-09-09 11:00 (GMT+8)<table><tr>'+
        ''.join('<th>'+h+'</th>' for h in headers)+'</tr><tr>'+''.join('<td>'+c+'</td>' for c in cells)+'</tr></table></div>').encode()


def test_spot_scoped_not_contract_or_hbm():
    f = spot_facts(document('dram_spot', spot_html(), 'html'))[0]
    assert f.value == 10. and f.factor_id.startswith('dram_spot_')
    assert f.effective_at.astimezone(timezone.utc).hour == 3
    assert f.mapping == 'unmapped' and f.factor_id != 'dram_contract_asp'


def test_contract_table_cannot_satisfy_spot():
    with pytest.raises(ValueError, match='table missing'):
        spot_facts(document('dram_spot', spot_html().replace(b'id="dram_spot"', b'id="dram_contract"'), 'html'))


def test_spot_schema_drift():
    with pytest.raises(ValueError, match='columns changed'):
        spot_facts(document('dram_spot', spot_html().replace(b'Session Average', b'Average'), 'html'))


def export_text(day=10, amount=100, yoy=5):
    return f'배포 2026. 8. {day+1}.(화) 09:00 2026년 8월 1일 ~ 8월 {day}일 수출입 현황 백만 달러 붙임 주요품목 반도체 {amount} {yoy} 반도체 500 8 주요국가'


def test_customs_exports_not_imports():
    f = export_fact(document('exports_10'), export_text())
    assert f.value == 100. and f.yoy_percent == 5. and f.coverage_days == 10
    assert f.released_at.astimezone(timezone.utc).hour == 0


def test_nowcast_same_month_deduplicated():
    a = export_fact(document('exports_10'), export_text())
    b = export_fact(document('exports_20'), export_text(20, 200, 6))
    assert select_nowcasts([a, b, a], NOW) == (b,)


def test_full_month_replaces_partials_not_added():
    a = export_fact(document('exports_10'), export_text())
    monthly = a.model_copy(update={'value': 500., 'coverage_days': 31, 'released_at': NOW-timedelta(days=1)})
    assert select_nowcasts([monthly, a], NOW) == (monthly,)


def test_customs_monthly_acceptance_not_shipment_table():
    text = '배포 2026. 8. 18.(화) 09:00 2026년 7월 월간 수출입 현황 백만 달러 수출입 상세 통계표 수리일 기준 (반 도 체) 100 150 50.0 200 300 50.0 2. 수입 실적 (반도체) 800 900 12.5'
    f = export_fact(document('exports_month'), text)
    assert f.value == 150. and f.yoy_percent == 50. and f.coverage_days == 31


def test_conflicting_same_release_rejected():
    a = export_fact(document('exports_10'), export_text())
    b = a.model_copy(update={'value': 111.})
    with pytest.raises(ValueError, match='conflicting'):
        select_nowcasts([a, b], NOW)


def test_future_revision_excluded():
    a = export_fact(document('exports_10'), export_text())
    b = a.model_copy(update={'collected_at': NOW+timedelta(days=1), 'released_at': NOW+timedelta(days=1), 'value': 200.})
    assert select_nowcasts([a, b], NOW) == (a,)


def test_fact_release_lookahead_rejected():
    a = export_fact(document('exports_10'), export_text())
    data = a.model_dump(); data['released_at'] = NOW+timedelta(days=1)
    with pytest.raises(ValueError, match='look-ahead'):
        Fact.model_validate(data)


def test_document_cutoff_and_hash():
    d = document()
    with pytest.raises(ValueError, match='cutoff'):
        assess([d], NOW-timedelta(seconds=1))
    data = d.model_dump(); data['body_base64'] = base64.b64encode(b'altered').decode()
    with pytest.raises(ValueError, match='hash'):
        Document.model_validate(data)


def test_unknown_release_and_staleness():
    f = financial_facts(document(), HEADER+'Total assets 300 200 3 2\nTotal liabilities 100 50 1 0\nTotal equity 200 150 2 1')[0]
    assert f.released_at is None and not f.eligible(NOW-timedelta(seconds=1))
    assert f.stale(NOW+timedelta(days=180))


def test_hwpx_nested_unit_and_replay():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr('Contents/section0.xml', '<root xmlns:h="urn:test"><h:t>unit <span>USD million</span></h:t></root>')
    d = document('exports_10', buf.getvalue(), 'hwpx')
    assert hwpx_text(d) == 'unit USD million'
    assert hwpx_text(Document.model_validate_json(d.model_dump_json())) == hwpx_text(d)


def test_offline_acquisition_failure(monkeypatch):
    def fail(*args, **kwargs):
        raise OSError('network unavailable')
    monkeypatch.setattr('urllib.request.urlopen', fail)
    d = collect_document(('test', 'test', 'https://example.invalid', 'html'))
    assert d.status == 'unavailable' and not d.bytes()


def test_extra_evidence_cannot_mark_original_e11_passed():
    bundle = assess([], NOW)
    assert 'units_sold' in bundle.original_e11_missing
    assert bundle.missing_critical == ('dram_contract_asp',)
    assert not bundle.checks


def test_new_journal_cannot_overwrite_first(tmp_path):
    first = tmp_path/'first.json'
    write_immutable(first, {'run_id': 'first'})
    before = first.read_bytes()
    with pytest.raises(ValueError, match='immutable'):
        write_immutable(first, {'run_id': 'second'})
    assert first.read_bytes() == before
