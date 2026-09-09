# SEC Future Reasoning v1.1 — Check 결과

> 2026-09-09 · Check 1 · 대상 commit: `629af3d45054dd70d592d7118bac4912573b92af`
> 판정: **Act 필요 / 제품 release 불가**
> 설계 항목 일치율: **9/32 = 28.125%** (부분 구현은 분자에서 제외)

## 1. 점검 범위와 기준

[Canonical PRD](../samsung_preferred_future_reasoning_prd_v1.1.html), [통합 Design](../02-design/features/sec-future-reasoning-v1-1.design.md), [P1 Design](../02-design/features/reasoning-foundation.design.md)을 현재 소스와 대조했다. foundation은 이전에 완료 보고되었으나 이번 경계 검증에서 결함이 추가로 확인되어 재개한다.

32개 검사항목은 통합 Design의 코드·저장소·실행·화면·검증 책임을 분해한 이번 Check의 분모다. 일치 9, 부분 4, 미구현 19다. 이 값은 공수 기반 진척률이나 예측 정확도가 아니다. 코드가 존재하고 해당 책임의 검증 증거가 있는 항목만 일치로 계산한다. 데이터 계약은 Engine 알고리즘 구현으로 계산하지 않는다.

## 2. 재현된 결함

### CK-01 · 높음 · 잘못된 실행 메타데이터가 release 검사를 통과

- 위치: [validation.py](../../reasoning/validation.py#L160), `release_ready`.
- 재현: 80개 정상 case_id를 넣고 execution_status=passed, run_id=`not-a-uuid`, fixture_hash=`not-a-hash`, versions=`not-a-version-bundle`로 구성하면 `True`를 반환한다.
- 원인: 필드의 존재·truthiness만 확인하고 실행 결과 schema, UUID/hash 형식, VersionBundle을 검증하지 않는다.
- 영향: `release-check --results`가 검증 가능한 실행 결과가 없는 입력을 release-ready로 표시할 수 있다. 현재 기본 unresolved 카탈로그는 계속 차단되고 실제 배포 경로는 아직 없다.
- Act 수용 조건: malformed 결과/비정상 versions/누락 실행 증거/중복 ID를 거절하는 선행 테스트; typed 결과 스키마와 fixture/run/버전 provenance 대조. 사람이 쓴 `passed` 문자열을 계산 검증의 대체로 삼지 않는다.

### CK-02 · 높음 · 근거 없는 non-applicable Meta 결과의 발행 가능 표시

- 위치: [artifacts.py](../../reasoning/schemas/artifacts.py#L392), `MetaCheck.publish_checks`, `EngineResult.valid_status`.
- 재현: E19 payload에 applicable=false, reason=`no inputs`, publishable=true, 빈 failed_checks/offending_engines/driver_refs를 지정한다. evidence 없이 success/confidence=1.0인 EngineResult가 생성되며 publishable=true가 유지된다.
- 원인: non-applicable의 evidence 예외와 publishable 교차 조건이 연결되어 있지 않다.
- 영향: 후속 Orchestrator가 이 필드를 신뢰하면 E19의 부족 근거 차단을 우회할 수 있다. 현재 실제 publisher가 구현된 상태는 아니다.
- Act 수용 조건: non-applicable 또는 필수 근거 미확인 Meta는 publishable=true 불가. 성공과 발행 가능을 분리하고 정상·부족·실패 조합 회귀 테스트를 먼저 작성한다.

### CK-03 · 중간 · 동일 시각의 상충 revision을 UUID로 선택

- 위치: [contracts.py](../../reasoning/schemas/contracts.py#L80), `select_as_of`.
- 재현: factor/source/observed/published/available이 같은 두 관측의 값이 4.2/4.8, revision이 r1/r2일 때 UUID(int=2)인 r1을 선택한다. UUID 대소 관계를 바꾸면 선택도 달라진다.
- 원인: timestamp 동률에서 observation UUID를 정렬 기준으로 사용하며 revision의 공급자 순서 또는 conflict 상태를 확인하지 않는다.
- 영향: source 간 충돌은 유지하지만 같은 source의 동시 수신 정정 충돌을 숨긴다. r1/r2 문자열 자체가 보편적인 revision 순서를 보장하는 것도 아니므로 문자열 정렬만으로 수정해서는 안 된다.
- Act 수용 조건: 공급자 revision 순서가 명시된 경우에만 최신값 선택; 순서 불명·값 상충은 conflict 또는 명시 오류. 입력 순서·UUID를 변경해도 결과 의미가 보존되는 테스트.

### CK-04 · 중간 · Factor의 비교기간을 일반값으로 덮음

- 위치: [validation.py](../../reasoning/validation.py#L87), `build_registry`.
- 재현: `samsung_eps_revision`의 value_definition에는 `30d revision`이 있지만 comparison_period는 `previous_observation`이다. `dram_contract_asp`의 MoM도 같은 일반값이 된다.
- 원인: yoy 이외의 모든 Factor에 previous_observation을 일괄 적용한다. schema/문서 drift 테스트도 같은 생성 함수를 기준으로 삼아 이 의미 차이를 잡지 못한다.
- 영향: 이후 Signal Engine이 비교기간을 기계적으로 해석하면 일간 EPS revision과 30일 revision 등을 혼동한다. 현재 Signal 알고리즘은 미구현이다.
- Act 수용 조건: Factor ID별 명시적인 transform/window/단위를 정의하고 30d·MoM·YoY·level별 독립 oracle을 테스트한다. 미정 값은 unknown 메타데이터로 남긴다.

위 네 건은 코드 수정 없이 로컬에서 재현했다. [기계 판독 증거](sec-future-reasoning-v1-1.check-evidence.json)에 입력 요약과 실제 결과를 보존했다.

## 3. 설계 대비 전체 매핑

| ID | 설계 항목 / 관련 FR | 판정 | 코드 또는 미구현 증거 |
|---|---|---|---|
| D01 | 49 Factor 의미·기간 / FR-01 | partial | registry 존재, CK-04 |
| D02 | 9 Module ID·참조 / FR-01 | match | MODULE_IDS, Registry.identities, registry 검사 |
| D03 | 19 typed payload 형태 / FR-05 | match | PAYLOAD_TYPES, 19 branch roundtrip |
| D04 | EngineResult/Meta 성공·근거 / FR-05 | partial | CK-02 |
| D05 | VersionBundle 고정 / FR-03/12 | match | 19 engine 버전 및 모델·graph·policy 필수 |
| D06 | cutoff·revision 선택 / FR-04 | partial | 미래값 제외 통과, CK-03 |
| D07 | Probability/ledger 값 계약 / FR-06 | match | 합계·finite·연결·delta·target 테스트 |
| D08 | 로컬 Journal 불변/hash / FR-12 | match | frozen tree, SHA256, 변조·중복 테스트 |
| D09 | JSON Schema 생성 / FR-01/05 | match | 6 schema 재생성 일치 |
| D10 | foundation CI / FR-13 | match | Python 3.11/3.12 원격 성공 |
| D11 | Golden 원문 추적 카탈로그 / FR-14 | match | T01–T70/MT01–MT10 일치, unresolved 보존 |
| D12 | 실행 결과 기반 release gate / FR-14 | partial | 기본 차단 정상, CK-01 |
| D13 | 로컬 설치·검증 방법 / FR-13 | match | FOUNDATION.md, lockfile, 실행 확인 |
| D14 | Entity/relationship/regime ontology 확장 / FR-01 | missing | ontology에는 registry.json만 존재 |
| D15 | Neo4j constraints/seed/repository / FR-02 | missing | graph 구현 없음 |
| D16 | Supabase schema/migration/access / FR-03 | missing | db 구현 없음 |
| D17 | 원자적 Forecast·Journal 저장 / FR-03/12 | missing | 저장 transaction/outbox 없음 |
| D18 | 실제 5 series ingestion/scheduler / FR-04 | missing | ingestion 구현 없음 |
| D19 | 운영 freshness/conflict/quarantine / FR-04 | missing | 메타데이터만 있고 실행기 없음 |
| D20 | Orchestrator/retry/checkpoint / FR-05 | missing | workflow 실행기 없음 |
| D21 | E01–E19 실제 처리 / FR-05 | missing | schemas만 존재, engines/service 없음 |
| D22 | 확률·simulation·calibration 계산 / FR-06 | missing | 값 계약만 존재 |
| D23 | Historical cap/Challenger 실행 / FR-06/12 | missing | typed payload만 존재 |
| D24 | Wave/Reversal feature 실행 / FR-07 | missing | OHLCV/timing 계산 없음 |
| D25 | Timeframe/Liquidity 계산 / FR-07 | missing | 계산 구현 없음 |
| D26 | Position별 Decision gate / FR-08 | missing | decision 구현 없음 |
| D27 | technical feedback 재계산 / FR-09 | missing | generation/dedup orchestration 없음 |
| D28 | API/BFF/auth/rate limit / FR-10/13 | missing | apps/API 구현 없음 |
| D29 | 5개 화면 / FR-11 | missing | apps/web 구현 없음 |
| D30 | Scenario/Outcome/Review/Experience 운영 / FR-10/12 | missing | 저장·조회·실행 없음 |
| D31 | 제품 Golden/회귀/forward 실행 / FR-14 | missing | 제품 Golden 80개 unresolved |
| D32 | staging/production·운영 관측 / FR-13 | missing | foundation 검사 workflow만 존재 |

## 4. 실행 검증

| 검사 | 관측 결과 |
|---|---|
| pytest 전체 | 50 passed, 0 failed |
| `python -m reasoning validate` | engines=19, factors=49, modules=9, golden_cases=80 |
| `python -m pip check` | No broken requirements found |
| 기본 `release-check` | release_ready=false, cases=80, exit 1 (정상 차단) |
| 최신 commit 원격 CI | [34313863832](https://github.com/donchang07/sec_future_reasoning/actions/runs/34313863832), success |
| 추가 경계 probe | CK-01–CK-04 모두 현재 코드에서 재현 |

테스트 50개 통과는 그 테스트가 다루지 않는 위 결함을 부정하지 않는다. 새 probe를 테스트 파일로 반영하고 수정하는 일은 Act에서 수행한다. 제품 코드·테스트 파일은 이번 Check에서 변경하지 않았다.

## 5. 이전 foundation 완료 판정 정정

이전 7/7=100%는 기존 테스트 범위의 초기 판정이다. 이번 재점검에서 F01(CK-02), F03(CK-03), F05(CK-04), F06(CK-01)을 partial로 재분류한다. F02/F04/F07은 match다. 같은 7개 기준의 엄격한 재검토 일치율은 **3/7=42.857%**다. 부분 항목을 전혀 구현하지 않았다는 뜻은 아니다.

기존 보고서는 이력으로 보존하되 재검토 안내를 추가한다. foundation 완료 상태를 재개하고 Act 대상으로 둔다. 전체 Do를 완료로 소급 기록하지 않는다. 이번 Check는 미완성 구현의 중간 검토이며 완료 판정이 아니다.

## 6. 다음 Act 순서와 종료 조건

1. CK-02·CK-01 회귀 테스트 선행 → 상태/발행 계약과 실행 결과 검증 강화.
2. CK-03·CK-04 회귀 테스트 선행 → revision 충돌 규칙과 Factor 기간 명세 수정.
3. schema/ontology 버전 영향 기록 → 생성 자료 갱신 → 로컬·원격 CI 및 네 probe 재실행.
4. foundation 재분석 후 `reasoning-vertical-slice` 기능 Plan/Design을 작성하고 실제 실행 경로 구현.
5. 제품 Golden 80개를 실행 가능한 fixture/oracle로 전환하고 미구현 D14–D32를 순차 충족.

이번 Check는 완료했고 다음 단계는 Act다. 90% 기준 미달과 핵심 기능 미구현·결함 때문에 release 또는 최종 완료 Report로 이동하지 않는다.
