# Professional prediction briefing — Design

> Version: 1.0.0 | Date: 2026-09-15 | Status: Approved
> Level: Enterprise | Plan: `docs/01-plan/features/professional-prediction-briefing.plan.md`

## 1. Architecture and invariants

The professional briefing is a publication-layer projection of an already validated system Journal. It is not part of forecasting or Decision Policy.

```text
sealed local Journal
    -> existing public-field / source / hash validation
    -> exact journal.json                         (unchanged)
    -> full explainability.md audit report        (unchanged)
    -> deterministic Korean briefing.md           (new)
           -> shared navy SVG header               (new)
    -> scoped Git publication + index             (extended)
```

Implement the renderer in a new `publication/briefing.py`. Do not change `reasoning/live_v2.py`, the 19 engines, technical feedback, Decision Policy, source collection, operations manifests, or sealed Journal contracts. `publication.publisher.export_record` calls the renderer only after the existing privacy and integrity checks pass.

## 2. Public artifact contract

For each eligible run, retain:

```text
docs/predictions/YYYY-MM-DD/run_id/
├── briefing.md          # new primary reader surface
├── explainability.md    # existing full audit; immutable
├── journal.json         # exact sealed bytes; immutable
└── outcomes/            # linked immutable outcomes when present
```

The shared `docs/predictions/assets/daily-briefing-navy.svg` is created through the same `immutable` function and included in the publisher's allowlisted path set. Each briefing references it as `../../assets/daily-briefing-navy.svg`.

`briefing.md` is also immutable: an existing byte-identical file is accepted; different bytes raise an immutable collision. Renderer version `professional-briefing-v1.0.0` is disclosed in the briefing footer.

## 3. Visual and information design

### 3.1 Navy header

Use a 1400×260 accessible SVG with:

- deep navy `#081A33` background;
- cyan `#4DB6D0` and muted gold `#C8A96A` accents;
- white/off-white typography;
- title `DAILY MARKET BRIEFING`;
- subtitle `Samsung Electronics Preferred · Explainable Forecast`;
- `<title>` and `role="img"` for accessibility.

The SVG is static and contains no script, external font, remote image, tracking, or user data.

### 3.2 Briefing hierarchy

1. Navy header.
2. Briefing metadata: KST timestamp, instrument, P0 value/effective time, run ID.
3. `오늘의 결론`: exact policy action and a compact executive summary.
4. `오늘의 주요 예측`: 1w/1m/1y probability, directional lean, confidence band, and exact action.
5. `전문 브리핑`: direction interpretation, timing/alignment/liquidity table, and decision-gate explanation.
6. `데이터 신뢰도와 핵심 리스크`: source availability and horizon-specific strong missing evidence.
7. `읽는 법과 한계`: research-only status, unknown semantics, timing/direction separation.
8. Audit links to full explainability and sealed Journal.

Use compact Markdown tables and short paragraphs. Keep the first reader-facing screen free of raw JSON, UUID evidence lists, engine ledgers, and internal Python representations.

## 4. Deterministic interpretation rules

### 4.1 Canonical display mappings

- Horizons: `1d/1w/1m/3m/1y` → `1일/1주/1개월/3개월/1년`.
- Actions: `WAIT/HOLD/ENTRY/SELL/WATCH/NO_ACTION` retain the canonical token and add a Korean label.
- Confidence: `<25% 매우 낮음`, `<50% 낮음`, `<70% 보통`, otherwise `높음`. This is a display band only and never changes policy.
- Missing probabilities render `산출 보류`, never `0%`.
- Missing liquidity renders `확인 불가`, never neutral.

### 4.2 Direction narrative

For numeric forecasts, compare Up and Down only:

- absolute spread below 5 percentage points: `상승·하락 경합`;
- otherwise display the leading direction and exact percentage-point spread.

Always append the stored confidence and state that the observation is not an actionable signal when the policy action is WAIT/HOLD/NO_ACTION. Do not infer economic causes beyond typed evidence.

For a withheld horizon, show its structured eligibility reasons and `strong_missing` evidence labels. No prior probability is presented as a forecast.

### 4.3 Timing, alignment, and liquidity

Render bottom/top reversal scores as timing diagnostics; explicitly state they do not set direction. Render bullish/bearish alignment separately. If buy/sell liquidity is absent, say the liquidity gate is unconfirmed and do not convert it to zero.

### 4.4 Decision gates

Translate only stored `passed_gates` and `decision.reasons` through a fixed label dictionary. Unknown identifiers remain escaped canonical text rather than being guessed. The exact stored action is authoritative.

### 4.5 Evidence quality

Count sources by stored status and `used_by_model`. Translate a fixed set of factor IDs for readability while retaining the canonical ID in parentheses. Deduplicate strong-missing fields per horizon and cap display to eight plus an explicit remainder count. This display cap does not discard evidence from the Journal or audit report.

## 5. Today's expected briefing

For run `d2d7d4b7-78c3-5927-87b4-2ebedb62614a`, the new surface must state without reinterpretation:

- Overall and all horizon actions: 관망 (`WAIT`).
- 1w: Up 35.9%, Down 42.0%, Flat 22.1%, confidence 5.1%; Down leads Up by about 6.2 percentage points.
- 1m: Up 37.2%, Down 40.4%, Flat 22.4%, confidence 4.0%; Up/Down are within the five-point mixed band.
- 1y: probability and confidence withheld because memory coverage/family quorum is insufficient.
- Liquidity: buy/sell confirmation unavailable.
- Sources: 11 registered source summaries, five fresh, six unavailable, four used by the model.
- P0: KRW 183,400 at the last eligible completed 30-minute close, explicitly not an executable quote.

## 6. Publisher and index changes

`export_record` adds `briefing.md` to its immutable outputs. `publish` ensures the header asset and changes the index to:

| Prediction timestamp | Professional briefing | Full audit | Sealed Journal |
|---|---|---|---|

The index description must reflect the current daily 07:15 KST schedule rather than the obsolete five-minute wording. Existing safe Git staging, divergence checks, captured-commit push, retry, and no-force behavior remain unchanged.

## 7. Security and integrity

- Render from `record['system']` only after `check_public`, allowlist, baseline digest, local-store boundary, and sealed-file equality checks.
- Escape dynamic strings inserted into Markdown tables or prose so field values cannot inject layout or links.
- Do not include raw observations, raw source references, credentials, holdings, Human Forecast, Shadow records, or arbitrary prewritten reports.
- Keep full internal detail in the existing explainability and exact Journal links.

## 8. Test plan

### Renderer tests

- SVG contains expected navy color, accessible title/role, and no script/external URL.
- Available probabilities, confidence bands, directional spread, P0, and KST timestamps are formatted correctly.
- Withheld horizon shows `산출 보류` and structured missing evidence rather than zero probability.
- Timing is labeled timing-only; unavailable liquidity is `확인 불가`.
- Stored gate reasons and canonical decisions are preserved.
- Dynamic Markdown control characters are escaped.

### Publication tests

- Export creates exactly Journal, full audit, and briefing per run while excluding outer private values.
- Existing different briefing is refused as an immutable collision.
- Shared SVG and index are inside `docs/predictions/` and repeated publication is idempotent.
- Index primary link targets `briefing.md` and current schedule text says daily 07:15 KST.

### Release verification

- Run publication-focused and full regression suites under the repository owner.
- Record SHA-256 of today's Journal and explainability before and after re-publication.
- Render today's briefing locally and inspect its first-screen content and SVG.
- Commit/push source changes first, then manually invoke `python -m publication` to publish the generated briefing without running prediction.
- Verify `origin/main`, public index, today link, and unchanged sealed/audit hashes.

## 9. Rollback

If briefing generation fails, keep the source commit separate from generated result publication, retain the existing Journal and explainability links, and fix only the publication projection. Never delete, rewrite, or regenerate a Prediction Journal to repair presentation.
