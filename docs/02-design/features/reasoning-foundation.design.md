# reasoning-foundation — Design

> 2026-09-09 · v1.0.0 · Enterprise · 구현 계약 baseline

## 1. 기준과 구조

[Plan](../../01-plan/features/reasoning-foundation.plan.md), [통합 Design](sec-future-reasoning-v1-1.design.md), [Engine 상세](sec-future-reasoning-v1-1/engines-and-model.md), [Factor 정의](sec-future-reasoning-v1-1/factor-registry.md)를 따른다.

`reasoning/schemas/contracts.py`: 공통 ID/Horizon/VersionBundle/Observation/Forecast/Journal. `artifacts.py`: 19개 discriminated payload 및 envelope/EngineResult. `reasoning/registry.py`: Factor/Module 모델과 정합성 검사. `reasoning/validation.py`: offline source catalog/schema 검사. `reasoning/__main__.py`: CLI. `ontology/*.json`, `tests/golden/catalog.json`, `packages/schemas/*.json`: versioned 산출물. 제품 API/DB/추론 실행은 포함하지 않는다.

## 2. 타입과 불변조건

Pydantic 2 모델에 extra=forbid, frozen=True, allow_inf_nan=False, 숫자 strict field를 적용한다. 중첩 컬렉션은 tuple로 고정한다. model_construct/model_copy(update=...)는 검증을 우회하므로 외부 입력 경로에서 사용하지 않는다. 수신은 model_validate_json, 내부 생성은 검증된 constructor만 쓴다. 시간은 aware datetime, probability는 finite strict float [0,1], ID는 비어 있지 않은 slug/UUID다. [Pydantic 모델 문서](https://docs.pydantic.dev/latest/concepts/models/).

F01: `Payload`는 kind literal로 E01–E19를 판별하는 union이다. 배열 결과는 payload의 items tuple로 감싼다. `Artifact`는 schema_version=1.0.0, UUID IDs, engine_id/version, cutoff, created_at, dependency IDs, evidence IDs, payload를 보유한다. engine_id와 payload.kind가 다르면 실패한다. `EngineResult` success는 artifact/confidence 필수, artifact confidence가 있는 경우 일치, applicable:false는 reason 필수다. retry는 retry_engine 필수, failed/insufficient/conflict는 warning 필수이며 output_artifact=null이다. E19에는 next_engine=null이 허용된다. envelope hash는 별도 canonical serializer가 계산하며 스스로를 해시하지 않는다.

F02: `ProbabilityVector` up/down/flat 합계 1e-9 이내. `Contribution`은 before/after/delta_pp tuple 3개와 engine/edge/version refs; delta=100×(after−before). `Forecast`는 prior→ledger→final 연결을 검증하고 target_at>data_cutoff, price_low≤price_high, confidence 범위 검증. `without_history_probabilities`를 독립 필드로 저장한다. 특정 policy threshold는 계약에 포함하지 않는다.

F03: `Observation`은 source ID/revision/unit/value와 observed/published/available_at을 가진다. observed≤published≤available을 요구하는 초기 계약이며 장래 사건 일정은 Observation 대신 Event 타입을 사용한다. cutoff 선택기는 available_at≤cutoff, published_at≤cutoff만 선택하고 같은 series/time의 최신 revision을 반환한다. cutoff에서 둘 이상 상충하는 source를 자동 평균내지 않는다. VersionBundle은 19 engine versions 전부, ontology/graph/model/prompt/calibration/policy/source/calendar/code를 요구한다.

F04: `JournalSnapshot`은 전체 Forecast/VersionBundle/observation refs/typed artifacts의 immutable tree다. canonical JSON은 sort_keys, compact separators, UTC timestamps, allow_nan=False로 직렬화한다. SHA256 hash는 envelope `{snapshot,sha256}`에서 snapshot만 대상으로 검증한다. 이 기능은 로컬 변조 감지이며 DB 불변성의 대체가 아니다. owner가 snapshot과 hash를 모두 바꾸는 공격을 인증한다고 주장하지 않는다.

## 3. Registry와 Golden

F05: 49개 Factor는 상세 문서와 ID/Module/값 정의/cadence/SLA/source class/provenance를 일치시킨다. `transform`, comparison_period, warmup, source_status, critical_for_horizons를 구조화한다. release schedule/series/provider 미확정은 null과 unresolved_fields로 표시하며 connected 금지. 경제적 sign은 graph/regime-dependent로 명시하고 임의 방향을 추가하지 않는다. required Horizon은 1d/1w의 6 Factor, 1m은 +memory/eps revision, 3m/1y는 +AI/supply/earnings/valuation의 명시된 ID 집합이다. references 없는 derived input은 auxiliary로 구분한다.

F06: HTML source의 T01–T70/MT01–MT10을 JSON에 그대로 보존한다. 각 entry는 case_id, source_columns, execution_status=unresolved, assumptions=[]이며 카탈로그 검사 성공을 Golden 실행 pass로 보지 않는다. CLI `release-check`는 하나라도 unresolved/failed/skipped이면 exit 1. 이 단계에서는 80개 전체가 unresolved인 것이 정확한 결과다.

F07: Python 타입에서 JSON Schema를 생성해 버전 관리한다. `python -m reasoning export-schemas`와 `python -m reasoning validate`로 생성과 drift를 검사한다. 모델의 교차 필드 validator는 JSON Schema로 완전히 표현되지 않으므로 Python 의미 검증이 최종 권위다. TS 타입 생성은 웹 기능 단계에서 같은 schema를 소비한다. [Pydantic JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/).

## 4. 선행 테스트·실행 환경

pytest: 잘못된 probability/NaN/boolean/unknown field, ledger 불연속, naive/future timestamp, revision cutoff, engine kind mismatch, success without evidence, invalid retry, nested mutation, hash tampering, 49 registry 중복/누락/문서 차이, 80 원문 사례 drift, schema drift를 검사한다. T66/T67/T70은 foundation 단위 수준에서만 검증하며 end-to-end Golden 완료로 표시하지 않는다.

Python>=3.11, Pydantic 2 및 pytest는 정확한 버전과 설치 의존성을 requirements.lock에 고정한다. 로컬 .venv를 사용한다. CI는 Python 3.11/3.12, pytest, schema/catalog 검증을 수행하고 dependency cache와 permissions:contents:read를 사용한다. paid/external service 호출은 없다. .env/.venv/private data는 gitignore한다. 가격·인과·정책 파라미터를 이 기능에서 계산하거나 변경하지 않는다.

## 5. 완료 기준

F01–F07에 구현/테스트 경로를 연결한 분석과 보고서를 작성한다. 전체 제품의 Do는 유지한다. 다음은 foundation을 소비하는 `reasoning-vertical-slice`의 별도 Plan/Design이다.
