import json
import subprocess
from datetime import date
from pathlib import Path

import pytest

from publication.email_delivery import (
    EMAIL_VERSION,
    DeliveryError,
    deliver_pending,
    render_email_envelope,
    run_codex,
    select_pending,
)


def system(run_id="00000000-0000-0000-0000-000000000001", timestamp="2026-09-14T22:00:11+00:00"):
    technical = {
        "wave": {"bottom_score": 0.1, "top_score": 0.2},
        "bullish_alignment": 0.1333333333,
        "bearish_alignment": 0.2666666667,
        "buy_liquidity": None,
        "sell_liquidity": None,
    }
    return {
        "run_id": run_id,
        "data_mode": "live_forward",
        "contract_version": "real-world-contract-v2.0.0",
        "mapping_version": "semantic-mapping-v1.0.0",
        "held": False,
        "prediction_timestamp": timestamp,
        "data_cutoff": timestamp,
        "operating_policy": {"run_kind": "official_preopen"},
        "p0": {
            "value": 183400.0,
            "unit": "krw_per_share",
            "effective_at": "2026-09-14T06:30:00+00:00",
            "definition": "last eligible completed close, not execution quote",
        },
        "sources": [
            {"status": "fresh", "used_by_model": True},
            {"status": "fresh", "used_by_model": False},
            {"status": "unavailable", "used_by_model": False},
        ],
        "horizons": [
            {
                "horizon": "1w",
                "final": {"probabilities": {"up": 0.359, "down": 0.420, "flat": 0.221}, "confidence": 0.051},
                "decision": {"action": "WAIT", "reasons": ["future_up", "confidence", "liquidity"]},
                "passed_gates": ["meta_check"],
                "technical": technical,
                "assessment": {"eligible": True, "reasons": [], "strong_missing": ["foreign_net_buy"]},
            },
            {
                "horizon": "1m",
                "final": {"probabilities": {"up": 0.372, "down": 0.404, "flat": 0.224}, "confidence": 0.040},
                "decision": {"action": "WAIT", "reasons": ["future_up", "confidence", "alignment", "liquidity"]},
                "passed_gates": ["meta_check"],
                "technical": technical,
                "assessment": {"eligible": True, "reasons": [], "strong_missing": ["dram_contract_asp"]},
            },
            {
                "horizon": "1y",
                "final": None,
                "decision": {"action": "WAIT", "reasons": ["meta_check", "confidence", "liquidity"]},
                "passed_gates": [],
                "technical": technical,
                "assessment": {"eligible": False, "reasons": ["coverage:memory"], "strong_missing": ["hbm_demand"]},
            },
        ],
    }


def record(**changes):
    item = system()
    item.update(changes)
    return {"system": item}


def config(tmp_path, **changes):
    executable = tmp_path / "codex.exe"
    executable.write_bytes(b"test")
    value = {
        "version": 1,
        "enabled": True,
        "recipient": "briefing@example.invalid",
        "activation_date_kst": "2026-09-15",
        "codex_executable": str(executable.resolve()),
        "model": "gpt-5.6-luna",
    }
    value.update(changes)
    return value


def write_config(root, value):
    state = root / "artifacts/local/publication"
    state.mkdir(parents=True, exist_ok=True)
    (state / "email-config.json").write_text(json.dumps(value), encoding="utf-8")


def test_email_envelope_matches_approved_professional_format():
    envelope = render_email_envelope(system(), "briefing@example.invalid")
    assert envelope["version"] == 1 and envelope["renderer_version"] == EMAIL_VERSION
    assert envelope["subject"] == "[SEC Future Reasoning] 2026-09-15 삼성전자우 데일리 브리핑 — 관망(WAIT)"
    assert envelope["payload"]["mime_type"] == "multipart/alternative"
    plain, html = (part["body"]["content"] for part in envelope["payload"]["parts"])
    assert "오늘의 결론: 관망 (WAIT)" in plain
    assert "1주: 상승 35.9% / 하락 42.0% / 보합 22.1%" in plain
    assert "유동성 확인 불가" in plain and "Price Wave/Reversal은 방향이 아니라 타이밍" in plain
    assert "background:#081A33" in html and "#4DB6D0" in html and "#C8A96A" in html
    assert "TODAY'S DECISION" in html and "오늘의 주요 예측" in html
    assert "35.9%" in html and "42.0%" in html and "확률 산출 보류" in html
    assert "research-only" in html and "실행 가능 호가가 아닙니다" in html
    assert "<script" not in html.lower() and "<img" not in html.lower()
    assert "multipart/alternative" not in html


def test_email_renderer_escapes_journal_text_and_keeps_unknown_explicit():
    item = system()
    item["run_id"] = "00000000-0000-0000-0000-000000000001<script>alert(1)</script>"
    envelope = render_email_envelope(item, "briefing@example.invalid")
    html = envelope["payload"]["parts"][1]["body"]["content"]
    assert "<script>alert" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert "확인 불가" in html and "산출 보류" in html


def test_select_pending_only_official_daily_after_activation_and_latest_per_day():
    first = record()
    later = record(run_id="00000000-0000-0000-0000-000000000002", prediction_timestamp="2026-09-14T22:01:00+00:00")
    event = record(operating_policy={"run_kind": "event"})
    held = record(held=True)
    old = record(run_id="00000000-0000-0000-0000-000000000003", prediction_timestamp="2026-09-13T22:00:00+00:00")
    next_day = record(run_id="00000000-0000-0000-0000-000000000004", prediction_timestamp="2026-09-15T22:00:00+00:00")
    selected = select_pending([event, held, first, old, next_day, later], date(2026, 9, 15), [])
    assert [r["system"]["run_id"] for r in selected] == [
        "00000000-0000-0000-0000-000000000002",
        "00000000-0000-0000-0000-000000000004",
    ]


def test_select_pending_skips_matching_ledger_delivery():
    item = record()
    ledger = [{
        "run_id": item["system"]["run_id"],
        "recipient": "briefing@example.invalid",
        "renderer_version": EMAIL_VERSION,
    }]
    assert select_pending([item], date(2026, 9, 15), ledger, "briefing@example.invalid") == []


def test_run_codex_is_bounded_windowless_and_validates_result(tmp_path, monkeypatch):
    root = tmp_path
    package = root / "publication"
    package.mkdir()
    schema = package / "email-delivery-result.schema.json"
    schema.write_text("{}", encoding="utf-8")
    envelope = render_email_envelope(system(), "briefing@example.invalid")
    envelope_path = root / "envelope.json"
    envelope_path.write_text(json.dumps(envelope), encoding="utf-8")
    result_path = root / "result.json"
    captured = {}

    class Result:
        returncode = 0
        stdout = "transport output"
        stderr = ""

    def fake_run(command, **kwargs):
        captured.update(command=command, **kwargs)
        result_path.write_text(json.dumps({
            "status": "sent",
            "message_id": "gmail-message",
            "thread_id": "gmail-thread",
            "run_id": envelope["run_id"],
            "to": envelope["to"],
            "subject": envelope["subject"],
        }), encoding="utf-8")
        return Result()

    monkeypatch.setattr("publication.email_delivery.subprocess.run", fake_run)
    result = run_codex(root, envelope_path, result_path, config(root))
    expected = subprocess.CREATE_NO_WINDOW if hasattr(subprocess, "CREATE_NO_WINDOW") else 0
    assert result["message_id"] == "gmail-message"
    assert captured["command"][0].endswith("codex.exe")
    assert "exec" in captured["command"] and "--ephemeral" in captured["command"]
    assert "--ignore-rules" in captured["command"] and "read-only" in captured["command"]
    assert "gpt-5.6-luna" in captured["command"] and 'model_reasoning_effort="low"' in captured["command"]
    assert str(schema.resolve()) in captured["command"]
    assert captured["timeout"] == 180 and captured["capture_output"] is True
    assert captured["creationflags"] == expected and captured["shell"] is False
    assert "Gmail tools only" in captured["command"][-1]


@pytest.mark.parametrize("mode", ["nonzero", "missing", "mismatch"])
def test_run_codex_fails_closed(tmp_path, monkeypatch, mode):
    package = tmp_path / "publication"
    package.mkdir()
    (package / "email-delivery-result.schema.json").write_text("{}", encoding="utf-8")
    envelope = render_email_envelope(system(), "briefing@example.invalid")
    envelope_path = tmp_path / "envelope.json"
    envelope_path.write_text(json.dumps(envelope), encoding="utf-8")
    result_path = tmp_path / "result.json"

    class Result:
        returncode = 1 if mode == "nonzero" else 0
        stdout = ""
        stderr = "failed for briefing@example.invalid"

    def fake_run(*_args, **_kwargs):
        if mode == "mismatch":
            result_path.write_text(json.dumps({
                "status": "sent", "message_id": "id", "thread_id": "",
                "run_id": envelope["run_id"], "to": "other@example.invalid", "subject": envelope["subject"],
            }), encoding="utf-8")
        return Result()

    monkeypatch.setattr("publication.email_delivery.subprocess.run", fake_run)
    with pytest.raises(DeliveryError) as caught:
        run_codex(tmp_path, envelope_path, result_path, config(tmp_path))
    assert "briefing@example.invalid" not in str(caught.value)


def test_deliver_pending_records_atomic_ledger_and_then_noops(tmp_path):
    cfg = config(tmp_path)
    write_config(tmp_path, cfg)
    records = [record()]

    class Store:
        def runs(self):
            return tuple(records)

    calls = []

    def runner(_root, envelope_path, _result_path, _config):
        calls.append(envelope_path)
        envelope = json.loads(envelope_path.read_text(encoding="utf-8"))
        return {
            "status": "already_sent",
            "message_id": "existing-message",
            "thread_id": "existing-thread",
            "run_id": envelope["run_id"],
            "to": envelope["to"],
            "subject": envelope["subject"],
        }

    first = deliver_pending(tmp_path, Store(), runner=runner)
    second = deliver_pending(tmp_path, Store(), runner=runner)
    ledger_path = tmp_path / "artifacts/local/publication/email-ledger.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    assert first == {"status": "complete", "delivered": 1, "runs": [system()["run_id"]], "recovered": 1}
    assert second == {"status": "noop", "reason": "No pending official Daily briefing"}
    assert len(calls) == 1 and not ledger_path.with_suffix(".json.tmp").exists()
    assert ledger["deliveries"][0]["message_id"] == "existing-message"


def test_deliver_pending_is_disabled_without_local_config(tmp_path):
    class Store:
        def runs(self):
            raise AssertionError("disabled delivery must not read runs")

    assert deliver_pending(tmp_path, Store()) == {"status": "disabled", "reason": "Local email configuration not found"}


def test_corrupt_ledger_fails_closed_without_calling_runner(tmp_path):
    write_config(tmp_path, config(tmp_path))
    state = tmp_path / "artifacts/local/publication"
    (state / "email-ledger.json").write_text("not-json", encoding="utf-8")

    class Store:
        def runs(self):
            return (record(),)

    with pytest.raises(DeliveryError, match="ledger"):
        deliver_pending(tmp_path, Store(), runner=lambda *_args: pytest.fail("must not send"))

