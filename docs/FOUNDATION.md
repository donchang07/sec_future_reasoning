# Reasoning Foundation 실행 안내

> P1 · Python 3.11 이상 · 외부 서비스 연결 없이 실행 가능

## 설치와 검증

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.lock
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m reasoning validate
.\.venv\Scripts\python.exe -m reasoning release-check
```

Linux/macOS에서는 `.venv/bin/python`을 사용한다. `validate`는 19개 payload 타입, 49 Factor/9 Module, 원문 Golden 80개 및 생성 schema 일치를 확인한다. `release-check`는 현재 `release_ready=false`와 exit 1을 반환한다. Golden 기대값 카탈로그는 실제 엔진 실행 결과가 아니므로 제품 release를 차단하는 것이 정상이다.

## 구현된 범위

- `reasoning/schemas/contracts.py`: 확률 vector·기여도 ledger·cutoff·19 Engine version bundle·불변 Journal/hash.
- `reasoning/schemas/artifacts.py`: E01–E19의 구체 typed payload, discriminator, EngineResult 상태 계약.
- `ontology/registry.json`: 49 Factor 정의, required Horizon, unit/cadence/SLA/provenance. 공급자 상태는 미연결이다.
- `tests/golden/catalog.json`: 원문 80개 사례와 unresolved 상태. 원문 hash는 UTF-8/LF 정규화 기준이다.
- `packages/schemas`: Python 모델에서 생성한 6개 JSON Schema. 교차 필드 제약은 Python 의미 검증도 필요하다.
- `.github/workflows/test.yml`: Python 3.11/3.12 계약 및 schema 검증.

JSON 입력은 `model_validate_json`으로 검증한다. 검증을 우회하는 `model_construct`, `model_copy(update=...)`를 ingestion/API 경계에 사용하지 않는다. frozen 모델과 tuple은 메모리상의 불변성을 제공하고 sealed snapshot hash는 변조를 감지한다. DB의 append-only 권한/transaction은 이후 저장소 기능에서 구현한다.

## 변경 절차

Engine 계약 변경은 테스트를 먼저 작성하고 schema version 영향을 확인한다. JSON Schema를 갱신하려면 `python -m reasoning export-schemas`를 실행한다. Factor/Golden 원문 추적 자료는 `python scripts/build_foundation_data.py`로 재생성한다. 실제 시장 관측을 이 스크립트가 만들어내지는 않는다.

## 다음 범위

실제 E01–E19 처리 알고리즘, Neo4j/Supabase, 실데이터 adapter, Wave/Decision 계산, API/UI는 아직 구현하지 않았다. 다음 `reasoning-vertical-slice`는 이 계약을 사용해 실제 입력→추론→피드백→결과·Journal의 종단 경로를 구현한다. 현재 단위 테스트 통과는 실전 예측 정확도 검증을 뜻하지 않는다.
