# reasoning-foundation — Plan

> 2026-09-09 · v1.0.0 · Enterprise · P1

## 목표와 범위

[Canonical PRD](../../samsung_preferred_future_reasoning_prd_v1.1.html)와 [통합 Design](../../02-design/features/sec-future-reasoning-v1-1.design.md)의 첫 구현 기반을 만든다. 19 Engine 실행 로직과 외부 저장소를 만들기 전에 계약·버전·근거·결측 처리를 실행 가능한 검증으로 고정한다.

범위는 Python 패키지, 19개 typed payload와 EngineResult, observation/cutoff 계약, Forecast/ledger 무결성, versioned journal snapshot 직렬화, 9 Module/49 Factor JSON registry, Golden 80개 기계 판독 카탈로그, JSON Schema 생성/검사 CLI, 선행 테스트 및 CI다. 실제 Engine 실행·실데이터 ingestion·Neo4j/Supabase·UI·Decision 계산은 이후 기능이다. 이 범위를 전체 Do 완료로 보고하지 않는다.

## 성공 기준

| ID | 조건 |
|---|---|
| F01 | 19 Engine ID와 payload type 일치, success/실패/unknown 계약 검증 |
| F02 | 확률 합계·finite·ledger 연결·기여도 재구성·target 시각 검증 |
| F03 | data cutoff/버전 고정, publication/availability 미래 데이터 거절 |
| F04 | immutable typed snapshot, 결정론적 hash, 변조 감지 |
| F05 | 49 unique Factor/9 Module, source 미연결 상태·provenance·required Horizon 보존 |
| F06 | T01–T70/MT01–MT10 보존, 미실행을 pass로 처리하지 않는 release 검사 |
| F07 | JSON Schema 재생성 일치 및 정상/비정상 사례 테스트, CI 구성 |

## 실행 순서와 위험

Plan→Design→테스트 작성 및 실패 확인→계약/registry/CLI→전체 테스트→gap analysis/report. 문서는 완성 시 GitHub에 올린다. 값 검증만으로 실제 예측 성능을 검증했다고 주장하지 않는다. frozen 객체 내부의 mutable list 문제는 tuple 및 frozen 중첩 모델로 막는다. Python 3.11이 현재 설치되어 있으므로 foundation은 3.11 이상을 지원하고 CI는 3.11/3.12로 검사한다. 통합 Design의 3.12 목표는 운영 기준이며 local 3.11 지원을 허용하는 호환 범위 확장이다.
