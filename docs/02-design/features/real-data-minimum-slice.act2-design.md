# real-data-minimum-slice — Act iteration 2 design

Date: 2026-09-09. This continues the existing feature and its Plan/Design. No new feature is created.

## Frozen boundary and acceptance

Keep the first live journal byte-for-byte, the original model profile, graph, all three core engine files, priors, calibration and ENTRY 80% / SELL 70%. New collection produces a new cutoff and run ID. Completion remains conditional on all nine original criteria.

Source discovery found two semantic blockers, not just missing HTTP adapters. E11 requires production/capacity and consolidated revenue = units sold × unit price, but consolidated Samsung financial statements do not disclose one company-wide physical sales unit. Its cash equation describes free cash flow, not the statement's net change in cash. Do not manufacture units, price or free cash flow solely to make these identities pass. The critical `dram_contract_asp` is an index; a specific DRAM spot quotation in USD/chip cannot replace it. Do not relax its critical flag or change its baseline/scale.

The Act adapter therefore stores typed financial facts, independently reconstructed statement identities, narrowly scoped spot evidence and export nowcast revisions alongside a fresh execution of the unchanged model. Unsupported mappings are explicitly `unmapped`, not silently included in the model. Accounting evidence will be connected to the journal's E11 input assessment, but unavailable original identities remain unavailable. If these limitations persist, report the feature incomplete rather than substitute a new forecast algorithm.

## Sources and scope

| Source | Provider / authority | Time and unit | Revision / freshness | Missing / mapping policy |
|---|---|---|---|---|
| 2026 H1 consolidated balance sheet, cash flow, income statement PDF | Samsung Electronics IR / official original | Period ended 2026-06-30; KRW million; Asia/Seoul; exact release time unknown, known-at is collection | Revisable, quarterly; stale after 150 days from period end | Extract named statement rows with column validation; no company-wide units or capacity invented |
| DRAM spot public table | TrendForce / original price publisher | Table's explicit GMT+8 update; USD/chip and SKU; Asia/Taipei | Revisable; stale after 4 days | Strict scoped table adapter; no contract/HBM equivalence; unavailable on schema drift |
| Aug 1–10, Aug 1–20, July monthly export HWPX | Korea Customs Service / official original | Period end, dated release; USD million and same-period YoY where available; Asia/Seoul | Nowcast revisions; 45-day freshness measured from release | Parse original XML tables; retain each raw revision, select latest eligible release per month; never add partial-period totals |
| Foreign / institutional / program flow | KRX / official | Source acquisition diagnostic | No eligible values without authorized data response | Maintain unavailable; portal availability is not data availability |

Samsung originals: [financial statements index](https://www.samsung.com/global/ir/financial-information/audited-financial-statements/). TrendForce: [DRAM spot](https://www.trendforce.com/price/dram/dram_spot). Customs: [August 20 release](https://www.customs.go.kr/kcs/na/ntt/selectNttInfo.do?bbsId=1362&mi=2891&nttSn=10173983&nttSnUrl=88748d91848cefc847351b9e9a2b4e1c). KRX: [Open API](https://openapi.krx.co.kr/contents/OPP/MAIN/main/index.cmd).

The default remains machine-readable data. HWPX is ZIP/XML; PDFs are official statements with table extraction. TrendForce's public HTML table is an explicit, isolated exception required by the requested source, with raw retention, strict schema checks and no login/paywall bypass.

## Evidence contracts and execution

Add an independent Act journal envelope without changing the first live journal schema. Raw documents retain URL, provider, content type, original bytes (base64), SHA256, request/collection timestamps and acquisition status. Every evidence record has data_mode, source hash, observed/effective/released/collected timestamps where known, scope, unit, availability and mapping disposition.

The semiconductor export demand factor is a typed source-level factor pending model mapping. Group revisions by calendar month and choose one latest eligible vintage; preserve coverage (10, 20, full month). Do not treat a larger cumulative period as demand growth or use three releases as three independent causal paths. Explicit YoY is a separate reported field, not inferred full-month demand.

Before a new forward run, finish all extra source collection, then collect market feeds and freeze cutoff. Run E01–E19 and one technical feedback using the frozen profile. Preserve supplementary accounting/spot/export evidence and original E11 assessment in the same immutable envelope. No supplementary unmapped factor contributes to direction probability. Report this limitation clearly.

Replay parses the stored bytes and recomputes the whole envelope offline at the same code version. Existing first-journal replay must use its recorded code version because source_identity hashes all Python sources. Integrity verification of the first journal continues on current code. Never change a recorded version merely to make replay compare equal.

## Validation and reporting

Tests cover raw tampering, cutoff/release chronology, stale source, strict financial columns, independently checked accounting identities, spot scope, missing/changed spot schema, export same-month revision deduplication, revision conflicts, future revisions and replay. Preserve the existing 109 tests (including all 89 fixture tests).

Report both journal IDs/hashes, source status and mapping status, all engine executions including non-applicable/insufficient counts, probabilities and confidence or explicit absence, wave/alignment/liquidity, gate failures, replay and CI. Separate independently validated financial identities from the unchanged E11 identities. Never call successful source ingestion successful full engine execution.
