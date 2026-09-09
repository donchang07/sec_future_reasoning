# SEC Future Reasoning — Codex Project Rules

## Mission
Build an explainable future-reasoning system whose first reference domain is Samsung Electronics preferred shares.

## Development method
Use bkit-codex PDCA. Design is mandatory before implementation. Treat the current PRD as the product source of truth, and create feature-level Plan and Design documents before code changes.

## Core architecture rules
1. The 19 Future Reasoning Engines determine direction probabilities and confidence.
2. Price Wave/Reversal determines timing, not direction.
3. Multi-Timeframe Alignment uses 30-minute/daily/weekly/monthly scales according to short/medium/long horizon.
4. Final ENTRY/SELL requires agreement between Future Reasoning, reversal timing, timeframe alignment, and liquidity confirmation.
5. Technical signals feed back into Market Regime, Capital Flow, and Reflexivity evidence before the final decision is recomputed.
6. Engines exchange typed structured artifacts; do not pass unconstrained free-form model text between engines.
7. Unknown is not neutral. Missing or conflicting evidence must lower confidence or return insufficient_evidence.
8. Forecast logic and Decision Policy must remain separate and independently testable.
9. Prediction Journal snapshots are immutable and versioned by data cutoff, ontology, graph, model, prompt, and calibration version.
10. Historical analogies are evidence only; cap their influence and prevent overfitting.

## Testing rules
Golden test cases are release gates. Add tests before changing causal rules, horizon weights, entry/sell thresholds, or engine contracts. Regression differences must identify the engine, graph edge, model, or calibration version that caused the change.

## Repository workflow
Use docs/01-plan, docs/02-design, docs/03-analysis, and docs/04-report for PDCA artifacts. Keep implementation aligned with the PRD and run gap analysis after significant changes.

### Document publishing and autonomy
Publish newly created or updated project documents to the configured GitHub origin as each document is completed, including PDCA status updates. Check the staged scope and exclude secrets and unrelated local changes. Complete the current PDCA phase without routine confirmation questions; resolve reversible design choices using the PRD and record assumptions. User authorization covers document commits and pushes. Required tool and environment approval controls still apply.

## Security
Never commit API keys, Supabase service-role keys, Neo4j passwords, brokerage credentials, or private data. Use environment variables and example files with placeholders only.
