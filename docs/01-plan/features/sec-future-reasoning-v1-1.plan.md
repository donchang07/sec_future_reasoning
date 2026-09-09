# SEC Future Reasoning v1.1 — Plan

> 작성일: 2026-09-09 | Plan 버전: 1.1.0 | 상태: Complete (계획 작성 완료, 구현 미착수)
> bkit Feature: `sec-future-reasoning-v1-1` | Level: Enterprise
> 다음 단계: Design — 구현 전에 기능별 계약·알고리즘·테스트를 확정한다.

## 1. 목적과 기준 문서

삼성전자우를 첫 참조 도메인으로, 가격의 원인이 되는 경제·산업·기업·수급 체계를 관측하고 미래를 확률과 근거로 설명하는 시스템을 구축한다. 방향 예측과 매매 의사결정을 분리하며, 데이터가 부족할 때 숫자를 만들어내지 않는다.

- 최우선 제품 기준: [Canonical PRD v1.1](../../samsung_preferred_future_reasoning_prd_v1.1.html), 원격 커밋 `5b6d234`의 README가 지정한 기준이다.
- 상세 보완 명세: [삼성전자우 상세 PRD v1.1](../../samsung_future_reasoning_prd_v1.1.html). 본 문서의 섹션 번호와 T/MT 사례는 이 상세본을 참조한다. 충돌 시 canonical을 우선한다.
- 상세본 원본 SHA-256: `42558703612C86BBDC2FABB519B7A5B5A92FD0A61743B21744AF9FE210FA9FEF`.
- 사용자가 지칭한 `sec_future_reasoning_prd_v1.1`에 해당하는 실제 파일은 위 HTML이다.
- 프로젝트 규칙: [AGENTS.md](../../../AGENTS.md). v0.9 문서는 참고 이력이며 v1.1을 대체하지 않는다.
- 현재 저장소에는 PRD, bkit 설정 및 설치 스크립트가 있다. 제품 API·UI·추론 엔진·DB migration·제품 테스트는 아직 없다.
- 원문에는 섹션 번호 중복과 건너뜀이 있다. 요구사항 추적은 번호와 제목을 함께 사용한다.

## 2. 목표와 완료 정의

### 2.1 제품 목표

1. 9개 World Model Module을 Ontology·Factor·Evidence·Causal Graph로 연결한다.
2. 19개 Engine이 typed artifact를 교환하며 실행·분기·검증·재시도를 수행한다.
3. Horizon별 Up/Down/Flat, Price Range, Confidence, 긍정·부정 Driver, What Would Change My Mind를 반환한다.
4. Forecast와 contribution ledger를 같은 버전·cutoff로 재현한다.
5. Future Reasoning, Reversal, Timeframe, Liquidity가 확인된 경우에만 Position별 ENTRY/SELL을 허용한다.
6. System Map에서 Factor·Evidence·Explanation·Scenario까지 탐색할 수 있게 한다.
7. Journal → Actual Outcome → Review → Learned Experience의 검증 루프를 구축한다.

### 2.2 완료 수준을 구분한다

| 수준 | 완료 증거 |
|---|---|
| 로컬 개발 기반 | 재현 가능한 fixture, 계약 검증, DB/graph migration, API·UI 실행 방법, 의미 있는 테스트 |
| 통합 MVP | 실제 adapter와 저장소를 통한 end-to-end 실행, PRD 기능 수용 기준, 80개 원문 사례의 추적 및 테스트 결과 |
| 운영 준비 | 실제 공급자 연결, staging 검증, 환경별 secrets, 배포·복구·관측 절차, forward 평가 수집 |
| 예측 성능 검증 | 미래 데이터로 수집한 forward 결과와 calibration 평가; 코드 테스트 통과와 별도로 보고 |

Fixture 또는 mock의 성공을 실데이터 연결이나 검증된 예측 성능으로 보고하지 않는다. 부분 엔진 구현을 19개 Engine 완료로 계산하지 않는다.

## 3. 범위와 요구사항 추적

| ID | 요구사항 | PRD 근거 | 주요 산출물 / 검증 |
|---|---|---|---|
| FR-01 | 9 Module, Ontology, Factor/Source Registry | §2, §3, §15 | YAML·JSON Schema, ID/단위/갱신주기/출처/결측정책 검증 |
| FR-02 | Neo4j 인과경로와 버전 | §3, §21 | constraints/seed, sign·strength·confidence·lag·regime·유효기간, 경로 테스트 |
| FR-03 | Supabase 시간·운영 저장소 | §4, §21 | migrations, observation/state/artifact/forecast/journal/review 저장과 접근 제어 |
| FR-04 | 수집·검증·영향 Module 재계산 | §4.3, §6.2, §9.1 | 우선 5개 시계열 adapter, freshness/conflict/idempotency/cutoff 테스트 |
| FR-05 | 19 Engine 및 Orchestrator | 통합부 「19개 Engine 상세」, §21 | E01–E19 각각의 계약, 실행기, 저장·재시도·실패 추적 |
| FR-06 | 확률·시뮬레이션·설명 | §1, §5, §7.4, E15–E19 | prior→delta→normalize→calibration 재구성, 가격구간·반증 조건 |
| FR-07 | Reversal·Timeframe·Liquidity | §22.1–22.5 | 30분/일/주/월 관측, bottom/top 상태, 정렬과 유동성 근거 |
| FR-08 | Forecast와 독립된 Decision Policy | §22.6–22.9 | Horizon별 Position, ENTRY/WAIT/HOLD/SELL, gate별 사유 |
| FR-09 | 기술 Evidence 피드백 | §22.8 | Regime/Capital Flow/Reflexivity 재실행 후 Forecast·Decision 재계산 |
| FR-10 | API | §6.1 | forecast, system-map, module, factor, scenario, explain, review endpoint |
| FR-11 | 5개 화면 | §7 | System Map, Module Detail, Factor Detail, Why Probability, Scenario Lab |
| FR-12 | 불변 Journal·Outcome·Review·Experience | §4, §9, E13/E19 | 불변 snapshot, outcome/review 별도 저장, 유사사례 영향 제한 |
| FR-13 | 환경·CI/CD·보안 | §8 | Next.js/Vercel, Python API, PR 검사, staging/production 분리 |
| FR-14 | Golden·회귀·Forward 검증 | §20, §22.10 | T01–T70, MT01–MT10, 변경 원인 버전 식별, forward 보고 |

### 범위 제외

- 증권사 주문 실행, 자동매매, 자금 이체. 본 버전은 설명과 의사결정 지원까지다.
- 삼성전자우 외 도메인의 제품화. 공통 계약은 확장 가능하게 설계한다.
- 초기부터 완전한 Bayesian Network 또는 OWL/RDF 도입. PRD의 설명 가능한 log-odds 접근과 YAML/JSON Schema를 따른다.
- Forward 데이터가 없는 상태에서 목표 수익률·정확도·실전 calibration 성능을 보장하는 일.

## 4. 구현 전에 해결할 PRD 간극

아래는 PRD 원문 수정이 아니라 구현 추적용 해석과 미확정 항목이다. 임의 상수로 조용히 채우지 않는다.

| ID | 관찰 | 처리 기준 / 종료 조건 |
|---|---|---|
| GAP-01 | 초기 Output은 1D/1W/1M/3M, 후기 Temporal/Decision은 1Y를 포함 | Forecast 계약은 `1d/1w/1m/3m/1y`를 수용한다. 단기=1d/1w, 중기=1m, 장기=1y. 3m은 별도 Forecast로 유지하고 Decision용 파동 매핑을 Design에서 명시한다. |
| GAP-02 | §22.7 SELL에는 alignment/liquidity 수치가 없지만 AGENTS는 네 계층의 일치를 요구 | SELL에서도 정렬·유동성 확인을 필수로 한다. 수치와 상위 추세 충돌 처리 규칙은 Design의 버전 있는 정책으로 명시하고 경계 테스트를 먼저 만든다. 미확정 상태에서 SELL을 허용하지 않는다. |
| GAP-03 | 49 Factor Registry를 선언하지만 전체 49개 명세가 제공되지 않음 | 원문에 식별된 Factor와 추가 제안 Factor를 구분한다. Design에서 49개 후보의 ID·단위·출처·cadence·Module·근거를 작성하고 원문 명시/제안 상태를 남긴다. 수량만 맞추는 placeholder 금지. |
| GAP-04 | T01–T70 중 ENTRY/SELL 사례와 MT 사례에 timing/liquidity/confidence 입력 일부 누락 | 원문 expectation을 보존한다. Forecast 검증과 최종 Decision 검증을 분리하고, 누락 조건은 별도 fixture 가정으로 명시한다. 원문 수치에 맞추기 위한 사례 ID별 출력 하드코딩 금지. |
| GAP-05 | WATCH/NO ACTION과 공식 네 Action 혼용 | Action은 ENTRY/WAIT/HOLD/SELL로 유지하고 WATCH/NO ACTION은 경고 또는 사유로 표현한다. 미보유는 WAIT, 보유는 HOLD를 기본 안전 상태로 설계한다. |
| GAP-06 | Edge에 Evidence가 직접 연결되는 예시 | Neo4j 관계 자체를 관계 endpoint로 사용할 수 없으므로 인과 edge를 참조하는 식별 가능한 node 모델 등으로 Design에서 구체화한다. 근거와 graph version 연결을 보존한다. |
| GAP-07 | prior, likelihood 변환, flat 경계, price range, calibration, history cap, TTL의 수치 미정 | 모델·정책 설정을 분리하고 초기 실험 가정을 명시한다. train/calibration/forward cutoff 분리, 민감도 및 cap 테스트를 먼저 정의한다. |
| GAP-08 | 공급자, 계정, API 배포 환경 미지정 | 로컬 fixture와 실제 adapter를 분리한다. 공급자별 데이터 권한·시각·단위를 확인한 뒤 연결하고, 연결 미확인은 운영 완료를 막는 항목으로 기록한다. |
| GAP-09 | 테스트 예제 마지막 `assert confidence`가 불완전 | 개별 Golden의 명시 범위 및 계약 불변조건으로 검증한다. 빠진 assertion을 통과로 취급하지 않는다. |

## 5. 아키텍처 계획과 불변조건

### 5.1 구성

- Web: PRD의 Next.js, Python API: FastAPI, orchestration: LangGraph/Python state를 설계 대상으로 한다. 구체 버전은 Design에서 호환성을 확인하고 고정한다.
- Neo4j는 인과관계와 graph version, Supabase/Postgres는 시간·관측·실행 artifact·Forecast·Journal·Review를 담당한다.
- LLM은 event/situation/hypothesis/challenger/scenario/meta의 구조화 추출·진단에 사용한다. Quant/Rule/Graph/Simulation 기능을 LLM 자유형 서술로 대체하지 않는다.
- 9 Module은 도메인 상태의 구분이고 19 Engine은 처리 단계다. 서로 일대일이라고 가정하지 않는다.
- §21.4의 `apps/web`, `apps/reasoning_api`, `reasoning`, `ontology`, `graph`, `db/supabase/migrations`, `ingestion`, `tests`를 기본 구조로 삼는다.

### 5.2 데이터와 실행 불변조건

1. EngineResult는 success/insufficient_evidence/conflict/retry/failed, typed output, confidence, evidence refs, warning, next/retry engine, trace ID를 갖는다.
2. E16 실패는 E15로, E19 실패는 원인 Engine으로 복귀한다. 횟수 제한과 종료 상태를 정하고 실패 Forecast를 발행하지 않는다.
3. 데이터는 observed time과 시스템이 알게 된 시각을 구분한다. cutoff 이후 정보 및 이후 확정된 outcome을 과거 Run에 주입하지 않는다.
4. Run은 data cutoff, ontology/graph/model/prompt/calibration version을 고정한다. Engine·policy version, random seed 및 실제 artifact도 재현에 필요한 범위로 저장한다.
5. Probability 합계는 내부 허용오차 내 1, UI는 100%다. Confidence는 별도 값이며 Unknown을 neutral로 바꾸지 않는다.
6. Graph 중복·상쇄·lag·regime과 historical influence cap은 설명 ledger 및 테스트로 검증한다.
7. E18 Forecast는 Decision threshold에 의존하지 않는다. E19 통과 및 기술 Evidence 반영 완료 후 Decision을 계산한다.
8. Journal은 append-only이며 review/outcome을 원본에 덮어쓰지 않는다. DB 권한과 변경 차단도 검증한다.
9. Technical feedback에는 원천 Evidence ID·버전과 재실행 범위를 기록한다. 같은 Evidence를 중복 가산하거나 무한 재실행하지 않는다.
10. 비밀은 환경 변수로만 주입한다. 브라우저에는 service-role/Neo4j/LLM secret을 노출하지 않는다.

## 6. 기능별 PDCA 실행 순서

### 첫 구현 목표: End-to-End Vertical Slice

2026-09-09 원격 README의 지침을 반영한다. 첫 구현은 전체 기능 완성이 아니라 하나의 실제 입력이 E01–E19와 기술 신호 피드백을 거쳐 Horizon별 forecast/timing/decision/explanation/journal을 생성하는 수직 단면이다. P1 foundation 이후 `reasoning-vertical-slice`의 기능별 Plan/Design을 작성하고 P2/P4/P5/P6에서 필요한 최소 경로를 먼저 구현한다. 하나의 입력은 검증 가능한 하나의 수집 배치를 의미하며, 추론에 필요한 역사·consensus·graph·OHLCV가 자동으로 충분해진다고 가정하지 않는다. 부족 시 종단까지 insufficient_evidence와 WAIT/HOLD 사유를 보존한다. fixture 경로 통과와 실제 입력 통과를 별도 보고한다. 이후 아래 P2–P8의 나머지 범위를 확장한다.

각 작업 묶음은 아래 feature slug로 `docs/01-plan/features/{slug}.plan.md`와 `docs/02-design/features/{slug}.design.md`를 먼저 작성한다. 본 문서는 제품 전체 계획이며 각 기능의 상세 Design을 대신하지 않는다. 개별 구현 후 `docs/03-analysis`에서 gap을 분석하고 완료 증거를 `docs/04-report`에 남긴다.

| 순서 / Feature | 의존성 | 구현 범위 | 완료 증거 |
|---|---|---|---|
| P1 `reasoning-foundation` | 본 Plan와 통합 Design | 공통 타입, 버전, 9 Module/Factor Registry, 19 Engine contract, 테스트 틀 | schema 양/음성 사례, 레지스트리 무결성, 원문 사례 추적 목록 |
| P2 `evidence-storage-ingestion` | P1 | Supabase migration, Neo4j graph, 5 시계열 수집, 검증, scheduler | 저장소 통합 테스트, 중복 수집·결측·충돌·cutoff·migration 검증 |
| P3 `world-model-explorer` | P2 | System Map, Module/Factor read API와 UI | 9 Module 표시, Evidence/시계열/인과 이웃 탐색, 빈 데이터 상태 |
| P4 `reasoning-engine-pipeline` | P1/P2 | E01–E19, 우선 Macro/Memory에서 시작해 전체 Module 확장, 분기·retry | Engine별 의미 테스트, causal/temporal/constraint/scenario 테스트, 실패 차단 |
| P5 `forecast-explanation-journal` | P4 | Horizon 확률·가격구간, ledger, 설명 UI, immutable journal | T66–T70, 재실행/재구성, calibrator provenance, DB 불변성 |
| P6 `wave-alignment-decision` | P4/P5 및 OHLCV/flow | reversal, timeframe, liquidity, position별 policy, feedback | T58–T65, MT01–MT10와 추가 결측·gate 경계·중복 feedback 테스트 |
| P7 `scenario-review-learning` | P5/P6 | 5 Factor override, scenario UI, actual/review, capped experience | 기준 Run 오염 없음, 모순 scenario 거절, history trap 및 outcome 누출 방지 |
| P8 `release-forward-validation` | P1–P7 | CI/CD, 환경분리, 관측·복구, staging 통합, forward 수집 | 전체 gate, 배포 증거, secrets 검증, 운영 문서, 잔여 gap 보고 |

각 단계의 구현 완료 시점은 의존성 및 검증 통과 기준으로 정한다. 계정·실데이터 확보와 무관하게 진행할 수 있는 계약, 로컬 저장소, fixture, UI 작업부터 수행한다. 외부 연결 없이는 완료할 수 없는 항목은 명시적으로 남긴다.

## 7. 수용 기준

| ID | 완료 조건 | 검증 방법 |
|---|---|---|
| SC-01 | 9 Module/주요 Edge가 한 화면에 표시되고 상세로 이동 | UI 통합 확인, PRD 화면 필드 점검 |
| SC-02 | Factor 최신값·단위·시각·시계열·출처·freshness·근거·인과 이웃·기여 조회 | API/저장소/UI 연결 검사, 결측·stale 상태 검증 |
| SC-03 | 지원 Horizon에서 합계 100%, 독립 Confidence, price range, 양/음 Driver와 반증 조건 | 계약, T66, 실패시 insufficient_evidence 검증 |
| SC-04 | 저장된 prior와 모든 delta/calibration으로 최종 확률 재구성 | T67, ledger 합계 및 버전별 회귀 |
| SC-05 | 19 Engine 각각 구현과 검증 증거 및 trace가 존재 | engine별 계약·의미·실패 테스트; stub는 미완료 |
| SC-06 | 최소 US10Y/USDKRW/DRAM ASP/AI CAPEX/CXMT capacity override 가능 | 같은 cutoff 기준 재계산, 영향 경로 표시, baseline 보존 |
| SC-07 | 각 Forecast Journal에 cutoff·버전·artifact·contribution 연결 | T70, update/delete 거절, outcome/review 후 원본 동일 |
| SC-08 | ENTRY/SELL은 필수 네 계층 및 Position 정책 충족 | 각각의 gate 아래/동일/위 경계, 누락/상충 시 action 차단 |
| SC-09 | 기술 Evidence가 관련 Engine을 갱신한 뒤 최종 Decision 생성 | MT09, 중복 이벤트·재시도·오래된 artifact 차단 |
| SC-10 | 실제 outcome 및 Human/AI review 구분 저장, 경험 영향 제한 | T38/T39, 시간 누출 방지, evidence 및 reliability 추적 |
| SC-11 | PR preview/staging/production 분리와 server-only secret 유지 | CI 실행·환경 설정·실배포 확인; 설정 파일만으로 완료 처리 금지 |
| SC-12 | Golden 80개와 추가 계약/정책 회귀가 추적 가능하며 release gate 통과 | 원문 ID별 실행 결과·가정·실패 원인; skipped/xfail을 pass로 계산하지 않음 |

## 8. 테스트와 품질 계획

- **테스트 선행:** 인과 규칙, horizon weight, threshold, Engine contract 변경 전 기대 동작과 실패 사례를 작성한다.
- **Golden 분류:** T01–T32 도메인/시장, T33–T40 evidence/history, T41–T49 constraint/path/lag, T50–T57 반전/confidence/bias, T58–T65 정책, T66–T70 불변조건/버전. MT01–MT10은 결합 판단·피드백·다중 Position이다.
- **독립 기대값:** 사례 입력과 기대 범위를 먼저 고정하고 출력에 맞춰 테스트를 수정하지 않는다. 동일 fixture를 calibration 학습과 독립 성능 검증에 중복 사용하지 않는다.
- **미정 입력:** qualitative 입력의 수치화·baseline·source·cutoff·timing 보완을 테스트 명세에 기록한다. 준비되지 않은 사례는 unresolved로 보고한다.
- **통합:** Supabase와 Neo4j 실제 테스트 인스턴스에서 저장/조회/제약/권한을 검사한다. adapter mock은 별도 단위 검증이다.
- **회귀:** data/ontology/graph/engine/model/prompt/calibration/policy 변경에 따른 차이를 engine·edge·설정 단위로 출력한다.
- **Forward:** Horizon별 outcome 성숙 시 평가한다. Brier score, log loss, calibration 및 구간 coverage 등을 기록하되 성능 목표는 baseline과 표본을 보고 정한다. 1Y 미성숙 표본을 완료 평가로 표시하지 않는다.
- **Gap 분석:** 각 주요 기능 구현 후 요구사항→Design→코드→테스트 연결을 점검한다. bkit match rate 90%는 보고 전 최소 기준이며, 누락된 핵심 gate나 실패 Golden을 면제하지 않는다.

## 9. 위험과 대응

| 위험 | 영향 | 대응 |
|---|---|---|
| 데이터 공급/라이선스/지연 | 근거 부족, 운영 연결 지연 | Source Registry와 freshness 정책, fixture 명시, insufficient_evidence |
| 49 Factor 명세 부재 | 잘못된 ID/단위/해석 | 원문 식별분과 제안분 구분, provenance 포함 Design |
| 목표 확률에 대한 과적합 | 설명은 되지만 일반화 실패 | ID별 하드코딩 금지, holdout/forward 분리, history cap |
| 재시도·feedback 반복 | 중복 반영, 비용 증가 | 실행 예산, deduplication, retry 범위·terminal status |
| LLM 비결정성/구조화 실패 | 계약 위반, 재현 어려움 | schema 검증, artifact snapshot, 제한적 재시도, 버전 고정 |
| 서비스 간 부분 저장 실패 | Forecast/Journal 불일치 | idempotent Run, publish 조건, 복구 절차를 Design에서 정의 |
| 불변 snapshot과 사후 평가 혼합 | 과거 예측 조작 | append-only journal, 별도 outcome/review, DB 수준 검증 |
| Horizon·정책 원문 충돌 | 성급한 ENTRY/SELL | GAP별 결정 기록, 누락 gate 확인 전 action 금지 |
| 외부 환경 미확보 | 운영 완료 검증 불가 | 로컬 구현 진행, 실제 연결·배포 상태 별도 추적 |

## 10. 일정과 다음 실행

| 단계 | 상태 | 종료 조건 |
|---|---|---|
| 전체 Plan | 완료 | v1.1 기준 범위·의존성·gap·수용 기준 정의 |
| 전체 Design | 다음 | 아키텍처, schema, 저장 원자성, API, 알고리즘, policy 및 테스트 상세 |
| P1–P8 기능별 Plan/Design/Do | 대기 | 각 기능 문서 선행 후 구현·검증 |
| Check/Act | 대기 | gap 분석 후 결함 수정 및 회귀 |
| Report | 대기 | 실제 완료·미완료·외부 의존·forward 성숙도 보고 |

다음 명령은 `$pdca design sec-future-reasoning-v1-1`이다. 통합 Design 이후 P1 `reasoning-foundation`부터 기능별 PDCA를 진행한다. 별도 구현 재승인을 전제로 하지 않으며, 이 Plan 완료는 제품 구현 완료를 의미하지 않는다.
