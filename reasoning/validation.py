"""Offline schema, source provenance and release-readiness checks."""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

from .registry import Registry
from .schemas.artifacts import Artifact, EngineResult, PAYLOAD_TYPES
from .schemas.contracts import Forecast, Observation, SealedJournal, MODULE_IDS

DESIGN = "docs/02-design/features/sec-future-reasoning-v1-1/factor-registry.md"
PRD = "docs/samsung_future_reasoning_prd_v1.1.html"
CASE_IDS = {f"T{i:02}" for i in range(1, 71)} | {f"MT{i:02}" for i in range(1, 11)}
SCHEMAS = {"artifact": Artifact, "engine-result": EngineResult, "forecast": Forecast,
           "observation": Observation, "sealed-journal": SealedJournal, "registry": Registry}


def json_text(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n"


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json_text(value), encoding="utf-8")


def build_registry(root: Path) -> dict:
    rows = []
    for line in (root / DESIGN).read_text(encoding="utf-8").splitlines():
        if re.match(r"^\| \d{2} \|", line):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
    if len(rows) != 49:
        raise ValueError("reviewed Factor table must have 49 rows")
    units = ("percent percent percent percent thousand_persons index krw_per_usd usd_per_barrel "
             "usd_million percent percent percent ratio index usd_per_unit index days percent percent "
             "wafers_per_month wafers_per_month wafers_per_month wafers_per_month months "
             "krw_billion percent krw_per_share krw_billion percent krw_billion "
             "krw_million krw_million krw_million ratio percentage_points ratio ratio percent percent "
             "krw_per_share krw_per_share ratio ratio ratio rsi score ratio z_score percentile").split()
    names = ("미국2년금리 미국10년금리 연준정책금리 미국CPI 미국고용증감 달러지수 원달러환율 WTI유가 "
             "하이퍼스케일러투자 GPU수요증가 AI매출증가 AI사용량증가 AI투자수익대용지표 DRAM계약가격 DRAM현물가격 "
             "HBM수요 메모리재고일수 메모리비트증가 HBM주문증가 삼성생산능력 SK하이닉스생산능력 마이크론생산능력 "
             "CXMT생산능력 팹가동소요기간 삼성매출 삼성영업이익률 삼성EPS 삼성FCF 삼성EPS수정 삼성설비투자 "
             "외국인순매수 기관순매수 프로그램순매수 반도체상대자금흐름 외국인지분변화 삼성선행PER 삼성PBR "
             "주식위험프리미엄 주식할인율 삼성보통주가격 삼성우선주가격 우선주할인율 우선주배당수익률 우선주회전율 "
             "우선주RSI 우선주추세정렬 우선주실현변동성 우선주거래량Z 우선주과열백분위").split()
    if len(units) != 49 or len(names) != 49:
        raise ValueError("unit/name transcription count mismatch")
    short = {"samsung_preferred_price", "us_10y_yield", "usdkrw", "foreign_net_buy",
             "preferred_volume_z", "preferred_trend_alignment"}
    medium = short | {"dram_contract_asp", "hbm_demand", "samsung_eps_revision"}
    long = medium | {"hyperscaler_capex", "cxmt_memory_capacity", "samsung_eps",
                     "samsung_forward_per", "equity_discount_rate"}
    dependencies = {
        "preferred_discount": ("samsung_preferred_price", "samsung_common_price"),
        "samsung_forward_per": ("samsung_common_price",),
        "samsung_pbr": ("samsung_common_price",),
        "preferred_dividend_yield": ("samsung_preferred_price",),
        "equity_discount_rate": ("equity_risk_premium",),
    }
    auxiliary = {
        "ai_capex_roi_proxy": ("incremental_ai_gross_profit", "lagged_capex"),
        "samsung_forward_per": ("forward_eps_consensus",),
        "samsung_pbr": ("book_value_per_share",),
        "samsung_fcf": ("operating_cash_flow", "capex_cash_flow"),
        "preferred_dividend_yield": ("cash_dividends",),
        "preferred_turnover_ratio": ("market_bars", "free_float_shares"),
        "equity_discount_rate": ("risk_free_rate", "equity_beta"),
        "semiconductor_relative_flow": ("sector_net_flow", "sector_turnover", "market_flow_ratio"),
    }
    factors = []
    for index, (_, factor_id, module, definition, cadence_sla, source, provenance) in enumerate(rows):
        # cadence may itself contain '/', so the delimiter includes surrounding spaces.
        cadence, sla = cadence_sla.split(" / ")
        age_match = re.search(r"\d+", sla)
        basis = "trading_days" if "trading" in sla else "bars" if "bar" in sla else "calendar_days" if age_match else "event"
        transform = definition.rsplit(" / ", 1)[-1]
        transform = next((kind for kind in ("log_return", "pct_change", "yoy", "diff", "ratio") if kind in transform), "level")
        warmup = 150 if "30m" in cadence else 12 if "monthly" in cadence else 8 if "quarterly" in cadence else 60
        if factor_id == "preferred_overheat_percentile":
            warmup = 252
        factors.append(dict(
            factor_id=factor_id, module_id=module, name_ko=names[index], value_definition=definition,
            unit=units[index], transform=transform, comparison_period=("year" if transform == "yoy" else "previous_observation"),
            warmup=warmup, cadence=cadence, expected_release_at=None,
            freshness_sla=dict(basis=basis, maximum_age=int(age_match[0]) if age_match else None, source_definition=sla),
            critical_for_horizons=[h for h, required in (("1d", short), ("1w", short), ("1m", medium), ("3m", long), ("1y", long)) if factor_id in required],
            source_candidates=source.split("/"), source_status="not_connected", source_id=None, series_id=None,
            timezone=None, provenance_class=provenance[0], prd_reference=provenance,
            derived_from=dependencies.get(factor_id, ()),
            auxiliary_inputs=auxiliary.get(factor_id, ("market_bars",) if module == "market_regime" else ()),
            economic_sign_by_regime="graph_defined", quality_tolerance_rule="quality-rule-experimental-v1",
            ontology_version="ontology-design-v1", unresolved_fields=["provider", "series_id", "release_schedule", "timezone"],
        ))
    return Registry.model_validate(dict(ontology_version="ontology-design-v1",
        modules=[dict(module_id=module, name=module.replace("_", " ")) for module in MODULE_IDS], factors=factors)).model_dump(mode="json")


class CaseParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = []
        self.cells = []
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.cells = []
        elif tag == "td":
            self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag == "td" and self.cell is not None:
            self.cells.append("".join(self.cell).strip())
            self.cell = None
        elif tag == "tr" and self.cells and self.cells[0] in CASE_IDS:
            self.rows.append(self.cells)


def build_catalog(root: Path) -> dict:
    # Git autocrlf must not change source identity across Windows/Linux runners.
    source = (root / PRD).read_text(encoding="utf-8-sig").encode("utf-8")
    parser = CaseParser()
    parser.feed(source.decode("utf-8-sig"))
    if len(parser.rows) != 80 or {row[0] for row in parser.rows} != CASE_IDS:
        raise ValueError("Golden source IDs incomplete or duplicated")
    return {"schema_version": "1.0.0", "source_path": PRD, "source_hash_format": "utf8-lf",
            "source_sha256": hashlib.sha256(source).hexdigest(),
            "cases": [{"case_id": row[0], "source_columns": row[1:], "execution_status": "unresolved",
                       "assumptions": []} for row in parser.rows]}


def export_schemas(root: Path) -> None:
    for name, model in SCHEMAS.items():
        write_json(root / f"packages/schemas/{name}.schema.json", model.model_json_schema())


def validate_repository(root: Path) -> dict:
    registry = json.loads((root / "ontology/registry.json").read_text(encoding="utf-8"))
    Registry.model_validate_json(json.dumps(registry))
    if registry != build_registry(root):
        raise ValueError("registry drift from reviewed design")
    catalog = json.loads((root / "tests/golden/catalog.json").read_text(encoding="utf-8"))
    if catalog != build_catalog(root):
        raise ValueError("Golden catalog drift from source; results belong in separate run artifacts")
    for name, model in SCHEMAS.items():
        expected = json_text(model.model_json_schema())
        if (root / f"packages/schemas/{name}.schema.json").read_text(encoding="utf-8") != expected:
            raise ValueError(f"generated schema drift: {name}")
    return dict(factors=49, modules=9, engines=len(PAYLOAD_TYPES), golden_cases=80)


def release_ready(results: dict) -> bool:
    cases = results.get("cases", [])
    if len(cases) != 80 or {case.get("case_id") for case in cases} != CASE_IDS:
        return False
    return all(case.get("execution_status") == "passed" and case.get("run_id")
               and case.get("fixture_hash") and case.get("versions") for case in cases)
