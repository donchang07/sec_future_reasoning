# Check: reasoning-vertical-slice

2026-09-09 · [Design](../02-design/features/reasoning-vertical-slice.design.md) · 구현 commit `1f38e7fad801b4bc7e1d65b09becf7eba2ec1de4`

사용자가 요청한 최소 실행 범위의 31개 검사항목(기존 결함 4 + 엔진 19 + 통합 8)을 충족했다. 해당 범위 match rate는 31/31=100%다. 전체 PRD나 원래 Golden 80개 완료율을 뜻하지 않는다. 기존 전체 PRD Check의 28.125%는 이전 commit에 대한 역사적 수치이며 이번에 전체 32개 항목을 재채점하지 않았다.

## 기존 결함 재검증

| ID | 발견 문제 | 수정 및 검사 | 판정 |
|---|---|---|---|
| CK-01 | 임의 문자열 metadata 80개로 release true | `CaseEvidence` UUID/hash/VersionBundle 검증, 파일/hash/run/version 검사, 원래 oracle 미완성 시 fail-closed | 해소 |
| CK-02 | non-applicable/no-driver MetaCheck publishable | applicable+driver 필수, EngineResult evidence 조건과 결합; 3개 경계 조합 | 해소 |
| CK-03 | 동일 source/time revision을 UUID로 임의 선택 | 최신 publication/availability 동률 중 값/단위 충돌은 명시적 오류; 정순/역순 모두 검사 | 해소 |
| CK-04 | EPS30d/DRAM MoM 비교 기간 소실 | 명시적 49개 transform/window, ontology-design-v2, CPI/growth/capacity/FCF 독립 oracle | 해소 |

7개 회귀 테스트를 선행 작성하여 6 fail/1 pass를 재현한 다음 수정했다. CK-01의 범위는 허위 release 통과 방지다. 원래 80개의 완전한 성공 oracle은 후속 작업이며 현재 release gate는 의도적으로 false다.

## E01–E19 검사: 19/19

각 engine은 기존 Foundation의 서로 다른 typed payload를 반환한다. [실행 문서](../VERTICAL_SLICE.md)의 19행에 구현 계산과 사용 입력을 기록했다. `tests/test_slice_invariants.py::test_each_engine_computes_structured_output`은 19개 결과의 계산 속성을 확인한다. 기본 fixture의 3 Horizon×2 generation×19개 전부 success이며 각 payload가 계산 경로에 사용된다. E13도 현재 fixture에서 similarity/regime gate를 통과하여 비영(非零) relevance를 계산한다.

E01 history 통계, E03 consensus dispersion, E04 residual, E06 Module state, E08 edge 곱, E09 중복 제거, E11 회계 identity, E12 Horizon 효과, E13 표본 감점, E15 분포, E17 simulation count/quantile, E18 확률 ledger, E19 발행 gate를 확인했다. placeholder/pass-through engine, case ID 분기, 엔진 내부 expected-result 값은 없다.

## 통합 검사: 8/8

| 항목 | 관찰한 증거 | 판정 |
|---|---|---|
| 재현 가능한 fixture | 20 Factor/80 observations, 4×160 OHLCV, raw event/consensus/accounting/history/DAG | 통과 |
| 3 Horizon 독립 결과 | 1w/1m/1y 확률·confidence·positive/negative paths 모두 존재; divergence 테스트 | 통과 |
| Wave/Alignment/Liquidity | RSI divergence, double bottom/top, neckline, MA, volume; primary+higher context와 flow | 통과 |
| 독립 Decision | 기술 단독 금지, confidence/liquidity/no-history gates, ENTRY79/80·SELL69/70 | 통과 |
| feedback 1회 | generation={0,1}; E01 불변, E06 Regime/Flow 및 E10 변경, final probability 변경 | 통과 |
| 하나의 Journal | 114개 execution, 모든 중간 Artifact, 입력 fixture, 버전, 3 Horizon, hash seal, exclusive create | 통과 |
| 설명/원장 복원 | 각 before/after/delta 체인 재검증; source/graph/model/calibration version 포함 | 통과 |
| 핵심 15 executable case | 15개 요구 사례 및 추가 불변조건 통과, 전체 pytest 89개 통과 | 통과 |

## 실제 실행 결과

| Horizon | 상승 | 하락 | 횡보 | Confidence | Bottom timing | Bullish alignment | Buy liquidity | 결정 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1주 | 79.01% | 9.20% | 11.78% | 98.19% | .90 | 1.00 | 1.00 | WAIT |
| 1개월 | 75.47% | 11.50% | 13.04% | 96.54% | .90 | 1.00 | 1.00 | WAIT |
| 1년 | 69.08% | 15.60% | 15.32% | 94.15% | .90 | 1.00 | 1.00 | WAIT |

합성 입력의 연구 결과다. confidence는 증거 품질/충돌에 대한 모델 내부 값이며 검증된 적중률이 아니다. 기술 조건이 좋아도 Future Probability가 .80 미만이므로 모두 WAIT다. 유리한 DRAM/HBM·AI 수요·금리/환율 경로와 불리한 CXMT 증설·PER 경로가 함께 저장되어 있다. 정확한 초기/최종 확률, path ID, hash는 [기계 판독 증거](reasoning-vertical-slice.check-evidence.json)에 있다.

로컬 `artifacts/local/prediction-journal.json`을 저장 후 다시 읽어 hash/contract/ledger/decision을 검증했고, 저장된 입력으로 전체 replay하여 Journal 일치를 확인했다. 실행 code commit의 [GitHub CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34315461362)도 Python 3.11/3.12에서 tests/fixture/replay를 실행하며 Journal을 artifact로 제공한다.

## 구현 시 명시한 범위와 보완

- Journal에 전체 typed fixture를 추가 저장하여 bar/event/consensus까지 독립 replay가 가능하게 했다.
- 가격 범위는 시나리오별 q10 최소~q90 최대의 보수적 envelope다. 전체 mixture의 정확한 quantile을 주장하지 않는다.
- 가설 반증 조건 방향, 역방향 pre-move, consensus 결측 감점을 추가 경계 테스트로 확인·수정했다.
- 동일 source의 모호한 revision은 fixture 자체 실행을 명시적 오류로 거절한다. 서로 다른 source의 충돌은 품질·confidence를 낮춰 전달한다.
- 부족한 critical factor는 E18 `insufficient_evidence`, 발행 불가 E19, WAIT/HOLD로 이어진다. 숫자 0이나 neutral로 채우지 않는다.
- 전체 49개 데이터 연결, 실데이터 adapter, 운영 calibration, DB/API/UI, 원래 80개 전체 oracle은 이번 최소 실행 범위 밖이다. product release는 닫혀 있다.

판정: 요청한 fixture vertical slice의 Check 통과. Foundation 결함 4개 닫음. 전체 제품은 후속 구현을 계속한다.
