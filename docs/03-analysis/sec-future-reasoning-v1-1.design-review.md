# v1.1 Design 검토 기록

> 2026-09-09 · 대상: Design 1.0.0 · 검토 방식: 문서·계약 일관성 확인
> 코드 구현 gap analysis가 아니며 구현 match rate를 산출하지 않는다.

## 기준

[Canonical PRD](../samsung_preferred_future_reasoning_prd_v1.1.html), [보완 상세본](../samsung_future_reasoning_prd_v1.1.html), [Plan 1.1](../01-plan/features/sec-future-reasoning-v1-1.plan.md), [통합 Design](../02-design/features/sec-future-reasoning-v1-1.design.md).

## 검토 결과

| 점검 | 결과 |
|---|---|
| 상세본과 canonical 우선순위 | canonical 우선, 상세본의 API/화면/사례 보존 |
| 첫 구현 목표 | README의 End-to-End Vertical Slice를 Plan/Design에 반영 |
| 19 Engine | E01–E19 19개 계약, 입력·처리·저장·다음 단계·실패 동작 정의 |
| Factor Registry | 49개 ID 중복 없음, 9 Module, source 연결 미완료와 E/D/P provenance 명시 |
| Golden | T01–T70 + MT01–MT10 총 80행을 상세 HTML과 문자열 비교하여 일치 확인 |
| Horizon 가중치 | 5개 열 각각 합계 1을 계산해 확인 |
| 문서 링크 | 설계 4개 문서의 내부 파일 링크 누락 0개 |
| Forecast/Decision 분리 | Forecast는 threshold를 읽지 않고 history 없는 shadow도 보존 |
| Reversal/정렬/유동성 | confirmed 상태, 방향별 gate, unknown 차단, 미보정 score 표시 정의 |
| 기술 feedback | root 근거 dedup, 고정 cutoff, downstream generation 무효화, 1회 batch 반영 |
| Journal | 단일 Postgres 발행 transaction, append-only, DB trigger/role, 버전 고정 |
| 보안 | 게시 대상의 대표 token/private-key 패턴 검사에서 매치 없음; 설정 파일은 커밋 범위에서 제외 |
| 요구사항 | FR-01–FR-14와 SC-01–SC-12의 Design 위치 연결 |

## 해석과 남은 구현 검증

- 3m의 주봉/월봉 매핑, SELL 정렬 .70·유동성 .60, history 제외 확률 gate는 설계 가정으로 기록했다.
- MT05는 상위 강한 상승 중 full SELL 대신 HOLD+경고를 택했다. 원문 expected는 보존하며 구현 oracle에서 차이를 드러낸다.
- 초기 log-odds weight, simulation fusion, confidence, flat band, history cap, timing feature 점수는 실험 설정이다. Golden 범위나 실제 정확도 충족이 검증된 값은 아니다.
- Forecast source/분포/가격 변환 계수 부족은 insufficient_evidence를 반환한다. 모든 Engine을 호출했다는 이유만으로 성공 처리하지 않는다.
- P1/P2 기능 설계에서 registry를 machine-readable schema와 source series 매핑으로 옮긴다. 공급자 접근권·API/worker hosting·실제 calibration 학습과 forward 결과는 구현/운영 검증 과제다.
- 제품 코드는 작성하지 않았고 제품 테스트를 실행하지 않았다. 본 검토에서 Golden 테스트 통과 건수를 주장하지 않는다.

## 판단

통합 Design 산출물 작성 및 정합성 점검을 완료했다. 다음은 `reasoning-foundation`의 기능별 Plan/Design과 구현이며, 이후 `reasoning-vertical-slice`로 실제 입력 경로를 연결한다. 각 단계의 성공 여부는 실행 증거로 다시 검증한다.
