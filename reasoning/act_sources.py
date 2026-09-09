"""Official documentary evidence, kept separate from incompatible model factors.

No prices, accounting values or expected predictions are embedded in adapters.
The manifest pins public documents, not their contents. Raw bytes are replay inputs.
"""
import base64
import calendar
import hashlib
import io
import re
import urllib.request
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html import unescape
from typing import Literal
from zoneinfo import ZoneInfo
from pydantic import AwareDatetime, model_validator
from pypdf.errors import PdfReadError
from .schemas.contracts import Contract, Number

UTC = timezone.utc
KST = ZoneInfo('Asia/Seoul')
MAX_BYTES = 8_000_000
SAMSUNG = 'https://images.samsung.com/is/content/samsung/assets/global/ir/docs/'
CUSTOMS = 'https://www.customs.go.kr/common/nttFileDownload.do?fileKey='
DOCUMENTS = (
    ('samsung_bs', 'Samsung Electronics IR', SAMSUNG+'2026_con_quarter02_bs.pdf', 'pdf'),
    ('samsung_cf', 'Samsung Electronics IR', SAMSUNG+'2026_con_quarter02_cf.pdf', 'pdf'),
    ('samsung_soi', 'Samsung Electronics IR', SAMSUNG+'2026_con_quarter02_soi.pdf', 'pdf'),
    ('dram_spot', 'TrendForce', 'https://www.trendforce.com/price/dram/dram_spot', 'html'),
    ('exports_10', 'Korea Customs Service', CUSTOMS+'b5ec31151ca51f476827b35864928525', 'hwpx'),
    ('exports_20', 'Korea Customs Service', CUSTOMS+'8cc25c364d861276e01149a8aa642480', 'hwpx'),
    ('exports_month', 'Korea Customs Service', CUSTOMS+'cf65caf623927ad258568c9a8a6b0e4d', 'hwpx'),
    ('krx_access', 'KRX', 'https://openapi.krx.co.kr/contents/OPP/INFO/OPPINFO003.jsp', 'html'),
)


class Document(Contract):
    source_id: str
    provider: str
    url: str
    format: Literal['pdf', 'html', 'hwpx']
    data_mode: Literal['live_forward'] = 'live_forward'
    requested_at: AwareDatetime
    collected_at: AwareDatetime
    status: Literal['available', 'unavailable']
    http_status: int | None = None
    body_base64: str
    sha256: str
    error: str | None = None

    def bytes(self):
        return base64.b64decode(self.body_base64, validate=True)

    @model_validator(mode='after')
    def valid(self):
        body = self.bytes()
        if len(body) > MAX_BYTES or hashlib.sha256(body).hexdigest() != self.sha256:
            raise ValueError('document hash/size')
        if self.requested_at > self.collected_at:
            raise ValueError('collection chronology')
        if self.status == 'available' and (not body or self.http_status != 200):
            raise ValueError('available document requires HTTP 200 bytes')
        return self


class Fact(Contract):
    factor_id: str
    value: Number
    unit: str
    scope: str
    source_id: str
    source_ref: str
    data_mode: Literal['live_forward'] = 'live_forward'
    observed_at: AwareDatetime
    effective_at: AwareDatetime
    released_at: AwareDatetime | None
    collected_at: AwareDatetime
    market_timezone: str
    authority: Literal['official_original', 'original_price_publisher']
    revisable: bool = True
    freshness_days: Number
    freshness_basis: Literal['effective_at', 'released_at'] = 'effective_at'
    mapping: Literal['unmapped'] = 'unmapped'
    mapping_reason: str
    month: str | None = None
    coverage_days: int | None = None
    yoy_percent: Number | None = None

    @model_validator(mode='after')
    def chronological(self):
        if self.observed_at > self.effective_at or self.effective_at > self.collected_at:
            raise ValueError('fact look-ahead')
        if self.released_at and not self.effective_at <= self.released_at <= self.collected_at:
            raise ValueError('release look-ahead')
        if self.freshness_days <= 0:
            raise ValueError('freshness must be positive')
        if self.freshness_basis == 'released_at' and self.released_at is None:
            raise ValueError('release freshness requires release timestamp')
        return self

    def eligible(self, cutoff):
        return self.collected_at <= cutoff and self.effective_at <= cutoff and (self.released_at is None or self.released_at <= cutoff)

    def stale(self, cutoff):
        basis = self.released_at if self.freshness_basis == 'released_at' else self.effective_at
        return (cutoff-basis).total_seconds() > self.freshness_days*86400


class IdentityCheck(Contract):
    name: str
    left: Number
    right: Number
    residual: Number
    passed: bool
    source_refs: tuple[str, ...]
    scope: str = 'Samsung consolidated statements; KRW million'
    engine_mapping: str = 'supplementary validation; not a replacement for original E11 identities'


class EvidenceBundle(Contract):
    facts: tuple[Fact, ...]
    selected_exports: tuple[Fact, ...]
    checks: tuple[IdentityCheck, ...]
    source_status: dict[str, str]
    original_e11_missing: tuple[str, ...] = ('production', 'capacity', 'units_sold', 'unit_price', 'independently_reported_free_cash_flow')
    missing_critical: tuple[str, ...] = ('dram_contract_asp',)
    model_mapping_status: str = 'No compatible supplementary mapping in frozen profile; forecast remains subject to original critical-input gate.'


def collect_document(spec):
    source_id, provider, url, fmt = spec
    requested = datetime.now(UTC)
    body, code, error = b'', None, None
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'SEC-Future-Reasoning-Research/1.0'})
        with urllib.request.urlopen(request, timeout=30) as response:
            body, code = response.read(MAX_BYTES+1), response.status
        if len(body) > MAX_BYTES:
            raise ValueError('document too large')
    except Exception as exc:
        code = getattr(exc, 'code', code)
        error = f'{type(exc).__name__}: source unavailable'
        body = b''
    return Document(source_id=source_id, provider=provider, url=url, format=fmt,
        requested_at=requested, collected_at=datetime.now(UTC), status='unavailable' if error else 'available',
        http_status=code, body_base64=base64.b64encode(body).decode(), sha256=hashlib.sha256(body).hexdigest(), error=error)


def fact(doc, factor_id, value, unit, scope, effective, *, release=None, freshness=150, **extra):
    return Fact(factor_id=factor_id, value=value, unit=unit, scope=scope, source_id=doc.source_id,
        source_ref=doc.sha256, observed_at=effective, effective_at=effective, released_at=release,
        collected_at=doc.collected_at, market_timezone='Asia/Taipei' if doc.source_id == 'dram_spot' else 'Asia/Seoul',
        authority='original_price_publisher' if doc.source_id == 'dram_spot' else 'official_original',
        freshness_days=freshness, mapping_reason='Source scope/unit does not identify a compatible frozen model input.', **extra)


def financial_text(doc):
    from pypdf import PdfReader
    return '\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(doc.bytes())).pages)


def financial_facts(doc, text=None):
    text = financial_text(doc) if text is None else text
    flat = ' '.join(text.split())
    if 'Samsung Electronics Co., Ltd. and its subsidiaries' not in flat or 'In millions of Korean won' not in flat:
        raise ValueError('issuer/unit mismatch')
    # This adapter supports the discovered H1 format only; never guess a new column layout.
    period = re.search(r'June 30,.*?Notes (20\d{2}) (20\d{2})', flat)
    if not period or int(period[1])-int(period[2]) != 1:
        raise ValueError('unsupported statement period/columns')
    effective = datetime(int(period[1]), 6, 30, 23, 59, 59, tzinfo=KST)
    labels = {
        'samsung_bs': [('total_assets', 'Total assets'), ('total_liabilities', 'Total liabilities'), ('total_equity', 'Total equity')],
        'samsung_cf': [('operating_cash', 'Net cash from operating activities'), ('ppe_acquisition', 'Acquisition of property, plant and equipment'),
            ('investing_cash', 'Net cash used in investing activities'), ('financing_cash', 'Net cash used in financing activities'),
            ('fx_cash_effect', 'Effect of foreign exchange rate changes'), ('cash_change', 'Net increase (decrease) in cash and cash equivalents'),
            ('cash_begin', 'Cash and cash equivalents, beginning of the period'), ('cash_end', 'Cash and cash equivalents, end of the period')],
        'samsung_soi': [('revenue', 'Revenue'), ('operating_profit', 'Operating profit')],
    }[doc.source_id]
    result = []
    for key, label in labels:
        matches = [line for line in text.splitlines() if re.match(re.escape(label)+r'\s+\(?\d', line.strip())]
        if len(matches) != 1:
            raise ValueError('missing/ambiguous financial row: '+key)
        row = re.sub(r',\s+(?=\d)', ',', matches[0].strip()[len(label):])
        row = re.sub(r',(\d{1,2})\s+(\d{1,2})(?=\s|,|$)',
            lambda m: ','+m[1]+m[2] if len(m[1]+m[2]) == 3 else m[0], row)
        numbers = re.findall(r'\(?-?\d[\d,]*(?:\.\d+)?\)?', row)
        count = 8 if doc.source_id == 'samsung_soi' else 4
        if len(numbers) not in (count, count+1):
            raise ValueError('financial column count: '+key)
        # Numeric note index, when present, precedes the data columns.
        value = numbers[-count:][4 if count == 8 else 0]
        amount = float(value.replace(',', '').strip('()')) * (-1 if value.startswith('(') else 1)
        result.append(fact(doc, 'samsung_'+key, amount, 'krw_million', 'Consolidated H1; balance sheet at period end, flows six-month cumulative', effective))
    return result


def statement_checks(facts):
    values = {f.factor_id: f for f in facts}
    checks = []
    for name, lhs, rhs in (
        ('assets_equal_liabilities_plus_equity', 'samsung_total_assets', ('samsung_total_liabilities', 'samsung_total_equity')),
        ('cash_change_equals_cashflow_components', 'samsung_cash_change', ('samsung_operating_cash', 'samsung_investing_cash', 'samsung_financing_cash', 'samsung_fx_cash_effect')),
    ):
        if all(k in values for k in (lhs, *rhs)):
            left, right = values[lhs].value, sum(values[k].value for k in rhs)
            checks.append(IdentityCheck(name=name, left=left, right=right, residual=left-right, passed=abs(left-right)<=.01,
                source_refs=tuple(sorted({values[k].source_ref for k in (lhs, *rhs)}))))
    if all(k in values for k in ('samsung_cash_begin', 'samsung_cash_end', 'samsung_cash_change')):
        left = values['samsung_cash_end'].value-values['samsung_cash_begin'].value
        right = values['samsung_cash_change'].value
        checks.append(IdentityCheck(name='cash_rollforward', left=left, right=right, residual=left-right, passed=abs(left-right)<=.01,
            source_refs=(values['samsung_cash_end'].source_ref,)))
    return tuple(checks)


def plain_html(text):
    return ' '.join(unescape(re.sub('<[^>]+>', ' ', text)).split())


def spot_facts(doc):
    html = doc.bytes().decode('utf-8')
    section = re.search(r'<div\s+id="dram_spot"[^>]*>(.*?)</table>', html, re.S)
    if not section:
        raise ValueError('DRAM spot table missing')
    headers = [plain_html(x) for x in re.findall(r'<th(?:\s[^>]*)?>(.*?)</th>', section[1], re.S)]
    if headers != ['Item', 'Daily High', 'Daily Low', 'Session High', 'Session Low', 'Session Average', 'Session Change', 'History']:
        raise ValueError('spot columns changed')
    updated = re.search(r'Last Update (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \(GMT\+8\)', section[1])
    if not updated:
        raise ValueError('spot timestamp missing')
    effective = datetime.strptime(updated[1], '%Y-%m-%d %H:%M').replace(tzinfo=ZoneInfo('Asia/Taipei'))
    result = []
    for row in re.findall(r'<tr[^>]*>(.*?)</tr>', section[1], re.S):
        cells = [plain_html(x) for x in re.findall(r'<td(?:\s[^>]*)?>(.*?)</td>', row, re.S)]
        if not cells:
            continue
        if len(cells) != 8 or not cells[0].startswith(('DDR3 ', 'DDR4 ', 'DDR5 ')):
            raise ValueError('spot row schema changed')
        high, low, session_high, session_low, avg = map(float, cells[1:6])
        if not 0 < low <= session_low <= avg <= session_high <= high:
            raise ValueError('spot price bounds')
        suffix = re.sub('[^a-z0-9]+', '_', cells[0].lower()).strip('_')
        result.append(fact(doc, 'dram_spot_'+suffix, avg, 'usd_per_chip',
            cells[0]+'; spot session average only; not contract ASP, HBM or total DRAM', effective, release=effective, freshness=4))
    if not result or len({f.factor_id for f in result}) != len(result):
        raise ValueError('empty/duplicate spot table')
    return result


def hwpx_text(doc):
    parts = []
    with zipfile.ZipFile(io.BytesIO(doc.bytes())) as archive:
        sections = sorted(n for n in archive.namelist() if re.fullmatch(r'Contents/section\d+\.xml', n))
        if sum(archive.getinfo(n).file_size for n in sections) > MAX_BYTES:
            raise ValueError('expanded HWPX too large')
        for name in sections:
            root = ET.fromstring(archive.read(name))
            parts.extend(''.join(t.itertext()) for t in root.iter() if t.tag.endswith('}t'))
    if not parts:
        raise ValueError('HWPX text missing')
    return ' '.join(' '.join(parts).split())


def export_fact(doc, text=None):
    text = hwpx_text(doc) if text is None else text
    release = re.search(r'배포 (\d{4})\.\s*(\d+)\.\s*(\d+)\.\([^)]*\)\s*(\d+):(\d+)', text)
    period = re.search(r'(\d{4})년\s*(\d+)월\s*(?:1일\s*~\s*\d+월\s*(10|20)일|월간)\s*수출입 현황', text)
    if not release or not period or '백만 달러' not in text:
        raise ValueError('customs release/period/unit missing')
    year, month = int(period[1]), int(period[2])
    coverage = int(period[3]) if period[3] else calendar.monthrange(year, month)[1]
    effective = datetime(year, month, coverage, 23, 59, 59, tzinfo=KST)
    released = datetime(*map(int, release.groups()), tzinfo=KST)
    if period[3]:
        # Attachment's first half is exports; second half is imports. Do not use headline rounded USD billions.
        scope = text.split('붙임', 1)[1].split('주요국가', 1)[0]
        match = re.search(r'반도체\s+([\d,]+)\s+([△\-\d.]+)\s+반도체\s+', scope)
        if not match:
            raise ValueError('customs partial export row missing')
        amount, yoy = match[1], match[2]
    else:
        # Customs acceptance-date table, before imports and shipment-date tables.
        scope = text.split('수출입 상세 통계표', 1)[1].split('2. 수입 실적', 1)[0]
        match = re.search(r'\(반\s*도\s*체\)\s+[\d,]+\s+([\d,]+)\s+([△\-\d.]+)\s+', scope)
        if not match:
            raise ValueError('customs monthly export row missing')
        amount, yoy = match[1], match[2]
    return fact(doc, 'semiconductor_export_demand', float(amount.replace(',', '')), 'usd_million',
        'KCS semiconductor exports by declaration acceptance; cumulative covered period, not full-month extrapolation', effective,
        release=released, freshness=45, freshness_basis='released_at', month=f'{year:04d}-{month:02d}',
        coverage_days=coverage, yoy_percent=float(yoy.replace('△', '-')))


def select_nowcasts(facts, cutoff):
    groups = {}
    for item in facts:
        if item.factor_id != 'semiconductor_export_demand' or not item.eligible(cutoff):
            continue
        groups.setdefault(item.month, []).append(item)
    selected = []
    for month, items in sorted(groups.items()):
        latest_release = max(x.released_at for x in items)
        latest = [x for x in items if x.released_at == latest_release]
        if len({(x.value, x.yoy_percent, x.coverage_days) for x in latest}) > 1:
            raise ValueError('conflicting nowcast revision: '+str(month))
        selected.append(max(latest, key=lambda x: (x.collected_at, x.source_ref)))
    return tuple(selected)


def assess(documents, cutoff):
    facts, statuses = [], {}
    for doc in documents:
        if doc.collected_at > cutoff:
            raise ValueError('document collected after cutoff')
        if doc.status != 'available':
            statuses[doc.source_id] = 'unavailable: '+str(doc.error)
            continue
        try:
            if doc.source_id.startswith('samsung_'):
                rows = financial_facts(doc)
            elif doc.source_id == 'dram_spot':
                rows = spot_facts(doc)
            elif doc.source_id.startswith('exports_'):
                rows = [export_fact(doc)]
            elif doc.source_id == 'krx_access':
                statuses[doc.source_id] = 'documentation_only; foreign/institution/program unavailable; no approved data API response'
                continue
            else:
                raise ValueError('unknown documentary source')
            facts.extend(rows)
            statuses[doc.source_id] = 'stale' if any(f.stale(cutoff) for f in rows) else 'available_unmapped'
        except (ValueError, IndexError, KeyError, zipfile.BadZipFile, ET.ParseError, PdfReadError, UnicodeError) as exc:
            statuses[doc.source_id] = 'invalid: '+str(exc)
    try:
        selected = select_nowcasts(facts, cutoff)
    except ValueError as exc:
        selected = ()
        statuses['semiconductor_export_demand'] = 'conflict: '+str(exc)
    return EvidenceBundle(facts=tuple(facts), selected_exports=selected, checks=statement_checks(facts), source_status=statuses)
