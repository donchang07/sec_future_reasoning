# FE-SF08 — 미국 10년물 전파와 Baseline 오차

- Parent PDCA: forward-evaluation-and-liquidity-v1
- Finding version: shadow-us10y-transmission-v1.0.0
- Registered: 2026-09-11 KST
- Status: open / hypothesis registered; prospective diagnostic automation pending
- Model influence: false. Probability / Confidence / Decision influence: false.
- Scope: Shadow Finding과 별도 진단 기록. 신규 모델 Feature 또는 Baseline 개선 작업이 아니다.

## 검증 질문

현재 frozen Baseline이 미국 10년물 금리의 경제적 중요성을 과소평가하는가? 단순 Factor weight가 아니라 실제 graph reachability, 전파 강도, Horizon별 시차, E09 중복 제거, 최종 contribution과 이후 오차를 함께 검증한다. 과소평가를 미리 결론내리지 않는다. 금리와 주가가 동일한 성장·인플레이션 뉴스에 반응할 수도 있으므로 동행 관계를 인과효과로 단정하지 않는다.

금리의 자산가격·투자·환율 전파에 대한 일반적 근거는 [Federal Reserve의 통화정책 설명](https://www.federalreserve.gov/monetarypolicy/files/pf_complete.pdf)이다. 아래 AI CAPEX·Memory 및 한국 개별 주식 연결은 이 문서가 입증한 사실이 아니라 추가 Evidence로 검증할 연구 가설이다.

## 현재 Baseline에서 확인한 사실

[9/11 immutable Journal](../predictions/2026-09-11/ad9cf183-cd34-512e-8386-d8436b2e28e4/journal.json)의 E08 금리 경로는 `us_10y_yield → module:macro → preferred_price`다. E09의 해당 root 조정은 중복 제거 없이 -0.69447375이며, 아래는 최종 ledger의 E12 순차 갱신 기여다.

| Horizon | Up 기여(%p) | Down 기여(%p) | Flat 기여(%p) |
|---|---:|---:|---:|
| 1주 | -7.048584 | +7.602513 | -0.553929 |
| 1개월 | -5.350408 | +6.067504 | -0.717096 |
| 1년 | unavailable | unavailable | unavailable |

1년은 Forecast withheld이므로 기여를 0으로 만들지 않는다. 이 값은 독립적인 counterfactual 효과가 아니며, E14/E17/E18 이후 최종 확률에 대한 금리만의 인과효과로 재명명하지 않는다.

E01은 Level, Change, Acceleration을 이미 저장하지만 E06의 기본 방향 계산은 normalized level과 quality를 사용한다. 기본 금리 baseline=4%, scale=1%p에서 normalized level은 clip되므로 5% 이상에서는 이 기본 Level 신호가 포화될 수 있다. 이는 점검할 메커니즘이지 Weight 변경 근거가 아니다. Threshold 및 FOMC proximity는 현재 별도 자동 Shadow 시계열로 구현되어 있지 않다.

## 전파 경로 감사

각 경로에 `implemented_and_active / implemented_but_suppressed / absent_from_baseline_graph / evidence_unavailable / horizon_withheld`를 구분한다. absent 또는 unavailable은 실제 경제효과가 0이라는 뜻이 아니다. 현재 관찰된 금리 root의 세부 분기 여섯 개는 absent_from_baseline_graph로 기록한다.

| 검증할 경로 | 별도 관찰할 Evidence / 반증 가능성 |
|---|---|
| 금리 → Valuation → 우선주 | 할인율·기대이익·멀티플을 분리. 이익 개선이 할인율 상승을 상쇄할 수 있다. |
| 금리 → USD/KRW → 우선주 | 환율 반응의 시점·크기. 금리 상승만으로 원화 약세를 가정하지 않는다. |
| 금리 → Foreign Flow → 우선주 | 실제 개별 종목 수급과 시장 Positioning을 구분. KOSPI/선물로 삼성전자우 Liquidity를 대체하지 않는다. |
| 금리 → AI CAPEX → Memory Demand Expectation → 우선주 | 실제 기업 CAPEX 가이던스·자금조달·수요 기대의 시차. 금리 상승만으로 CAPEX 감축을 만들지 않는다. |
| 금리 → Memory Demand Expectation → 우선주 | Spot/Contract/HBM/Inventory/Shipment를 구분. export를 DRAM 가격으로 대체하지 않는다. |
| FOMC risk ↔ 장기금리 반응 → 위 경로 | 정책 기대·Surprise·Priced-in 여부·발표 전후 금리를 구분. 금리가 FOMC 결정을 유발했다는 역인과를 가정하지 않는다. |

각 run/horizon/generation에 root observation IDs, graph/code/contract versions, node/edge IDs, edge sign/strength/confidence/lag/duration, E08 path strength, E09 original/adjusted effect와 suppression reason, E12 before/after/delta를 참조한다. 한 금리 root의 여러 경로를 독립 Evidence처럼 합산하지 않는다. Baseline에 없는 경로에 가상의 contribution을 배정하지 않는다. Valuation·FX·Flow의 자체 root 기여도 금리에서 유래했다고 자동 귀속하지 않는다.

## 별도 Shadow Diagnostic 필드

`diagnostic_id, finding_version, recorded_at, run_id, prediction_sha256, prediction_cutoff, data_mode, recording_mode, diagnostic_version, model_influence=false`를 필수로 한다. Source별 `provider, source_ref, raw_hash, observed_at, effective_at, released_at, collected_at, source_timezone, session_date, freshness, revision/vintage, missing_reason`을 보존한다. 제공되지 않은 시각은 null로 둔다.

| 진단 | 사전 정의 |
|---|---|
| Level | nominal US Treasury 10-year par yield, percent. 실질금리·정책금리·시장 intraday yield와 구분. |
| Change | 연속하는 source 거래 세션의 `100 × (y[t] - y[t-1])` bp. 세션이 빠지면 1일 변화라고 부르지 않고 observed interval을 기록. |
| Acceleration | `change[t] - change[t-1]` bp/관측 간격. 최소 3개 동일 Source·vintage 관측과 실제 간격 필요. |
| Threshold proximity | 사용자 지정 5.00%에 대해 signed distance=`100 × (y-5)` bp, absolute distance, below/at/above, crossing을 별도 기록. 임계점 근접 자체는 매매 신호가 아니다. |
| FOMC proximity | cutoff 이전 확보된 공식 일정의 event ID, 발표 예정/실제 시각, hours_until / hours_since, 일정 vintage. 일정 또는 정확한 시각 미확보 시 unavailable. |
| Event context | 사전에 수집한 expectation, surprise, priced-in, 장기금리 반응. 없으면 unknown. 사건 이후 얻은 설명은 사후 Evidence로 별도 표시. |

금리 Level·Change·Acceleration·5% proximity는 같은 원자료의 파생 진단이다. 다섯 독립적인 긍정/부정 표로 계산하지 않는다. 5% 기준은 결과를 보고 최적화하지 않는다. 추가 threshold 및 shock cohort 기준은 첫 prospective 분석 전에 Design으로 고정하고 version을 발행한다.

이번 [별도 진단 JSON](shadow-us10y-transmission.observation-2026-09-11.json)은 이미 봉인된 run에서 추출한 사후 annotation이다. 예측 당시 생성된 Shadow record로 소급하거나 Forward/Event 사례 수에 추가하지 않는다. FOMC proximity는 당시 확보된 일정 증거를 검증하지 못했으므로 unavailable로 기록한다. 새 자동 기록기를 배포했다는 의미는 아니다.

## Forward Evaluation 검증 계획

1. 향후 Daily/Event run은 Baseline을 그대로 실행한다. Shadow는 별도 저장하고 prediction SHA와 run_id로 연결한다. journal 안에 사후 필드를 추가하지 않는다. 구현 시 parent PDCA의 Plan/Design 확정 및 isolation tests가 선행되어야 한다.
2. Outcome이 완성되면 동일 Horizon끼리 join한다. 1일 Outcome은 보조 진단이며 1주 예측의 정답으로 재사용하지 않는다. withheld, stale, missing, not-yet-due를 각각 별도 집계한다.
3. 기존 label/flat band/Brier(0..2)/Confidence bin/ENTRY·SELL 지표 정의를 유지한다. 금리 진단 구간별 n, Baseline error rate, Brier, class calibration, Confidence calibration, False/Missed ENTRY·SELL과 opportunity denominator를 보고한다.
4. 금리 충격 분석의 주 지표는 연속적인 signed change와 acceleration이다. shock/non-shock 이산 비교가 필요하면 거래 세션 연속성, 관측 창, 금리 변화 기준, FOMC 창을 미래 Outcome 관찰 전에 고정한다. 현재 단일 run의 +12bp를 보고 shock cutoff를 선택하지 않는다.
5. 금리 Level 효과와 변화 효과를 분리하고 미국 주가·USD/KRW·실적·변동성·수급 missing 및 source-timing version 차이를 함께 보고한다. 필요한 보조 자료가 없으면 confounding을 해결했다고 주장하지 않는다.
6. 중첩된 1주/1개월/1년 Forecast와 동일 FOMC의 여러 run은 독립 표본이 아니다. session/event 단위 중복 제거, 충격 episode 수, matched matured outcome 수를 별도 보고한다. 불확실성 추정 시 시계열 의존성을 고려한다.
7. 최소 20개 distinct Forward/의미 있는 Event 사례 이전에는 모델 변경 검토를 시작하지 않는다. 20개는 통계적 충분조건이 아니며, 충격 구간의 만기 도래 Outcome이 부족하면 insufficient_evidence를 유지한다. 그 이후에도 변경은 별도 Contract PDCA 승인이 필요하다.

## 불변 조건과 후속 Check

real-world-contract-v2.0.0, Ontology, Mapping, Requirement Matrix, E01–E19, Graph, Weight, Prior, Calibration, Wave/Reversal, Alignment, Liquidity, Decision, ENTRY 80%, SELL 70%를 유지한다. 금리 단독 하락/상승 규칙이나 FOMC 직후 급락 ENTRY를 추가하지 않는다.

후속 구현의 필수 검증: percent↔bp 단위, 비연속 세션, missing/revision/cutoff, FOMC 일정 vintage, 5% 경계와 교차, 같은 root 중복 방지, absent path와 0 effect 구분, withheld Horizon, Shadow on/off Baseline 동일 SHA, immutable Journal/replay, 전체 회귀 통과. 현재 작업은 Finding 문서와 기존 기록의 추출만 수행하며 실행 코드·예약·모델은 변경하지 않는다.
