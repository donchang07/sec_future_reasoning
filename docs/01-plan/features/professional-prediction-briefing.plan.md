# Professional prediction briefing — Plan

> Version: 1.0.0 | Date: 2026-09-15 | Status: Approved
> Level: Enterprise

## 1. Purpose and background

The public result currently opens with a dense, English-first audit report of more than 200,000 characters. It preserves evidence well but does not let an executive reader understand today's forecast, confidence, timing, decision, or evidence limits at a glance.

Add a separate Korean professional briefing for every eligible public Prediction Journal. The briefing becomes the primary human-readable link while the existing sealed Journal and full explainability report remain immutable audit artifacts. Re-publish today's 2026-09-15 result in the new format without rerunning prediction.

## 2. Goals

- Present a restrained institutional-research visual identity led by a navy header.
- Put today's conclusion and horizon-level probabilities before technical detail.
- Explain direction, timing, multi-timeframe alignment, liquidity, confidence, and missing evidence in professional Korean.
- Derive every statement deterministically from typed Journal fields; do not add model opinions or alter Decision Policy.
- Preserve direct links to the full explainability report and exact sealed Journal.

## 3. Scope

### In scope

- New immutable `briefing.md` beside each published `journal.json` and `explainability.md`.
- Shared navy SVG header under `docs/predictions/assets/` for reliable GitHub Markdown rendering.
- Executive conclusion, today's key forecasts, professional interpretation, evidence-quality summary, gate discipline, and audit metadata.
- Korean labels and explanations with English canonical actions/field names retained where useful.
- Update the results index so the briefing is the primary link and audit artifacts remain separately accessible.
- Backfill registered public runs and immediately publish the new 2026-09-15 briefing.

### Out of scope

- Recomputing a forecast, changing probabilities, confidence, timing scores, gates, or decisions.
- Rewriting an existing `explainability.md` or sealed `journal.json`.
- Personalized investment advice, target-price selection, or discretionary natural-language model commentary.
- Publishing raw captures, credentials, holdings, Human Forecast, or external Shadow inputs.

## 4. Functional requirements

- `PB-F01`: Export `briefing.md` immutably for each validated public run and keep existing Journal/explainability bytes unchanged.
- `PB-F02`: Display a navy, white-text, accessible header as a versioned SVG image with no remote asset dependency.
- `PB-F03`: The first screen shows KST briefing date, target instrument, reference price and time, overall action, and a 1w/1m/1y forecast table.
- `PB-F04`: Professional commentary distinguishes Future Reasoning direction from Price Wave/Reversal timing and reports Multi-Timeframe and liquidity state separately.
- `PB-F05`: Low confidence, withheld horizons, failed gates, unavailable sources, and strong missing evidence are prominent; unknown is never presented as neutral or zero.
- `PB-F06`: Narrative is deterministic and templated from typed fields. It may summarize values but must not invent causes, forecasts, recommendations, or evidence.
- `PB-F07`: The public index links primarily to `briefing.md` and separately to `explainability.md` and `journal.json`.
- `PB-F08`: Today's run `d2d7d4b7-78c3-5927-87b4-2ebedb62614a` is published again through the existing safe Git transaction without rerunning prediction.

## 5. Non-functional requirements

- GitHub Markdown compatible, readable on desktop and mobile, with compact tables and no JavaScript.
- Navy header remains visually stable without relying on inline CSS that GitHub may sanitize.
- Existing public/private allowlists, hash checks, immutable-collision behavior, scoped Git commits, and no-force policy remain release gates.
- Repeated publication is idempotent, including the new briefing and header asset.

## 6. Success criteria

- Tests cover header color/accessibility, probability and confidence formatting, withheld evidence, gate explanations, audit links, immutable export, index routing, and idempotency.
- Publication-focused tests and full regression suite pass.
- Today's briefing clearly reports WAIT for 1w/1m/1y, the available 1w/1m probability values, very low confidence, missing liquidity, and withheld 1y evidence.
- Today's sealed Journal and existing explainability SHA-256 values are identical before and after publication.
- The new briefing and index are pushed to `origin/main`; `.codex/config.toml` remains untouched.

## 7. Risks and mitigations

| Risk | Effect | Mitigation |
|---|---|---|
| Polished prose overstates weak evidence | Reader mistakes a weak signal for conviction | Lead with official Decision Policy result and confidence; label directional lean as non-actionable. |
| Timing score is read as direction probability | Reversal diagnostics distort the forecast | Put timing in a separate section and state that it does not determine direction. |
| GitHub strips visual styling | Navy header disappears | Use a repository-owned SVG referenced as an image instead of sanitized inline CSS. |
| Renderer change mutates prior output | Audit history is rewritten | Create a new immutable briefing artifact; never replace existing Journal or explainability bytes. |
| Briefing leaks private data | Public boundary is violated | Render only after the existing public validation and from the validated system Journal. |

## 8. Delivery order

1. Publish Plan and PDCA status.
2. Complete and publish Design before source changes.
3. Add tests before renderer and publisher changes.
4. Render and inspect today's briefing locally; run publication and full regression suites.
5. Publish implementation, then run the publisher once to re-send today's result.
6. Verify immutable hashes and GitHub state; publish Check and Report.

## 9. References

- `docs/samsung_future_reasoning_prd_v1.1.html`
- `docs/02-design/features/prediction-result-publication.design.md`
- `docs/RESULT_PUBLICATION.md`
- `docs/predictions/2026-09-15/d2d7d4b7-78c3-5927-87b4-2ebedb62614a/explainability.md`
