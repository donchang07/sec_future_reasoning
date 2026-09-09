# reasoning-vertical-slice — Plan

> 2026-09-09 · v1.0 · 사용자 지시로 fixture 우선 / 핵심 실행 테스트 15개 우선

## 목적

Foundation 계약을 재사용하여 E01–E19→Wave→Alignment→Liquidity→technical feedback→E01–E19 재계산 1회→Decision→통합 Journal을 실행한다. 1w/1m/1y 결과와 모든 중간 artifact를 조회할 수 있게 한다. 기존 80개 카탈로그 전체 통과는 이번 완료 기준이 아니다.

## 범위와 수용 기준

| ID | 수용 기준 |
|---|---|
| VS01 | CK-01–04 선행 회귀 테스트 후 수정, Foundation 계약 유지 및 검증 강화 |
| VS02 | versioned fixture 한 세트와 OHLCV 네 timeframe, 외부 접속 없이 결정론적 실행 |
| VS03 | 19 Engine 모두 자신의 수치 계산/규칙 기반 구조화 추론 수행, pass-through 금지 |
| VS04 | 1w/1m/1y 각각 확률·confidence·양/음 causal path와 ledger |
| VS05 | OHLCV로 RSI divergence·double pivot·neckline·SMA·volume·reversal 계산 |
| VS06 | 방향·timing·상위정렬·유동성·confidence를 모두 확인하는 독립 Decision |
| VS07 | 기술 Evidence가 Regime/Flow/Reflexivity에 반영되어 확률 1회 재계산 |
| VS08 | 한 JSON Journal에 run/cutoff/versions/3 Horizon/모든 artifact/Decision/설명, hash 검증 및 overwrite 차단 |
| VS09 | 핵심 15개 executable 사례, 별도의 계약/재현/ledger/피드백 불변조건 테스트 |

## 실행 순서

Design 문서→GitHub 게시→네 결함 회귀 테스트→수정→fixture 및 15개 oracle 선행→Engine/technical/orchestrator/Journal 구현→로컬·원격 CI→실제 CLI fixture 실행→분석·보고 및 게시.

공식 공급자, DB 서비스, 웹 UI와 실전 예측 정확도는 다음 범위다. fixture의 실험 prior/scale/graph/model은 명시적으로 version 관리하며 기대 결과나 case_id를 Engine 코드에서 참조하지 않는다. 정량 oracle는 방향/상대 변화/경계 및 불변조건 중심으로 설정한다.
