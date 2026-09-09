# real-world-contract-refinement 완료 보고서

2026-09-09 · **완료조건 10/10 충족** · Plan → Design → Do → Check → Act 완료.

현실 데이터에 맞는 별도 계약 `real-world-contract-v2.0.0`을 발행했다. **새 live prediction은 생성하지 않았다.** 기존 두 Journal의 당시 판단과 `real-data-minimum-slice`의 7/9 기록도 변경하지 않았다.

## 발행 산출물

- [버전 태그](https://github.com/donchang07/sec_future_reasoning/tree/real-world-contract-v2.0.0): `b9dc4a542113044d4d7ecdec4c70ec0fca03897b`.
- [기계 판독 계약 manifest](../../config/contracts/real-world-contract-v2.0.0.json): 코드 해시, 동결 모델 해시, 48개 Factor의 Horizon별 요구조건, coverage 기준, Memory taxonomy.
- [설계·경제적 근거](../02-design/features/real-world-contract-refinement.design.md), [최종 gap analysis](../03-analysis/real-world-contract-refinement.analysis.md).
- [23개 사실 개별 분류](../03-analysis/real-world-contract-refinement.mapping-audit.md), [전체 매핑 JSON](../03-analysis/real-world-contract-refinement.mapping-audit.json).

## Horizon별 요구조건과 Probability / Confidence

48개 활성 Factor 각각에 1주·1개월·1년의 Hard Required / Strong Evidence / Supporting Evidence / Optional / Unavailable Allowed를 지정했다. 이 등급은 기존 인과 Weight를 바꾸지 않는다.

Coverage는 단순 관측 개수가 아니라 경제적 정보 묶음별 최대 mapping confidence를 사용한다. 예를 들어 Macro는 금리·환율, Earnings는 수익성·현금 창출, Memory는 가격·수요·재고/출하 균형으로 나눈다. 동일 SKU·파생 지표를 추가해 관측 개수만 늘려도 coverage가 증가하지 않는다.

| Horizon | Macro 최소 | Memory 최소 | Earnings 최소 | Price/Regime 최소 | 추가 조건 |
|---|---:|---:|---:|---:|---|
| 1주 | 0.40 | 없음 | 없음 | 0.60 | 종목 가격 Hard Required; 기술 데이터만으로 통과 불가 |
| 1개월 | 0.40 | 0.25 | 0.40 | 0.60 | Memory와 Earnings 근거 필요 |
| 1년 | 0.40 | 0.50 | 0.80 | 0.40 | 서로 다른 Memory family 2개 이상, 자산·부채·자본 Hard Required; Spot 제외 |

DRAM Contract ASP는 1주 Supporting, 1개월·1년 Strong이다. 하나의 계약가격이 모든 Horizon의 필수 조건은 아니지만, 1년에는 다른 충분한 Memory·Earnings 근거가 없으면 계속 보류한다. 근거는 PRD의 시간축 차이와 가격·수요·현금 흐름의 구분이며, 현재 두 WAIT 결과를 맞추어 정한 기준이 아니다. 위 숫자는 사전 고정한 연구용 eligibility 정책이며 통계적으로 검증된 정확도 기준은 아니다.

Hard Required 결측 또는 Module coverage 미달은 probability withheld다. 적격일 때만 Future Reasoning이 공급한 후보 확률을 그대로 유지하며, Confidence에 `필수 Module coverage의 최솟값 × 0.9^(Strong 결측 Module 수)`를 적용한다. 결측을 이유로 Flat 확률에 임의로 섞지 않는다. 이전 후보를 새 계약 이름으로 다시 발행하는 기능은 없다.

## 의미 분리와 Memory State

DRAM Contract ASP, DRAM Spot Price, HBM Demand, HBM Price, Memory Inventory, Memory Bit Shipment, Semiconductor Export Momentum의 7개 family를 분리했다. 각각의 수치·단위·scope·root·mapping version을 보존한다. 비교 가능한 과거 값이 없는 Spot 한 점은 방향 unknown이다. 재고 변화는 가격/수요와 반대 방향으로 해석하며, 수출과 DRAM이 상충하면 positive/negative family와 conflict를 모두 출력한다. 이는 Memory State이며 직접 주가 확률은 아니다.

SourceObservation은 field/unit/scope/보고기간/horizon/regime/cutoff를 검증한 뒤 FactorEvidence가 된다. 각 Mapping에는 요청된 9개 필드가 모두 포함된다. 동일 원자료여도 Mapping Version이 바뀌면 Evidence ID가 달라진다. 실제 데이터에 미등록 Mapping Version을 임의로 적용할 수 없다.

## 수출 Nowcast

10일 v1 → 20일 v2 → 월간 잠정 v3 → 월간 확정 final을 구분했다. 같은 월의 최고 eligible stage에서 최신 revision 하나를 선택한다. 뒤늦게 수집된 v1이 final을 덮어쓰지 못한다. YoY·조업일수 조정 YoY·가속/감속을 별도 파생 항목으로 기록하되 같은 월/root를 공유한다.

조업일수가 없으면 조정치를 만들지 않는다. 가속도는 전월의 같은 기간 또는 양쪽 모두 전체 월일 때만 계산한다. 이전 월 자료는 현재 coverage에 stale이어도 cutoff 이전에 알려진 적격 비교자료라면 가속도의 provenance에만 사용할 수 있다. 추가적인 독립 positive vote가 되지 않는다.

## E11 v2

| 영역 | 구현 | 데이터 없을 때 |
|---|---|---|
| Company Financial Constraint | 자산=부채+자본, 현금흐름 구성 합계, 현금 rollforward; OCF·정확한 cash CAPEX·FCF·Cash/Debt | 항등식별 non_applicable 및 missing fields |
| Memory Business Constraint | 같은 Segment·기간·통화·수량단위의 Revenue=Volume×ASP | non_applicable; 연결매출을 강제 투입하지 않음 |
| Industry Supply Constraint | 생산≤능력, Yield 범위, 물리적 Bit Supply 한계, 신규 증설 수치 | non_applicable |

Company 파생 FCF는 PPE 현금 CAPEX와 무형자산 현금 CAPEX가 모두 있을 때만 계산한다. 계산한 FCF를 독립적으로 검증한 값처럼 사용하지 않으며, 같은 정의의 공식 FCF가 별도로 있을 때만 identity check가 가능하다. 결산일뿐 아니라 `2026-H1` 같은 보고기간도 같아야 한다. 서로 다른 공급자의 상충 값과 분기/반기 혼합을 막는 추가 회귀 테스트를 Act에서 먼저 실패시킨 뒤 수정했다.

## 기존 23개 사실 재분류

**직접 매핑 19개 / 파생 근거 매핑 4개 / 의미 검증 후에도 미매핑 0개.** 기존 Journal 안의 23개 `unmapped` 표시는 그대로다. 별도 감사 산출물에서 새 계약을 검토한 결과이며, 23개 모두를 방향 신호로 바꾼 것이 아니다.

- 직접: 재무 사실 12개와 Spot SKU 값 7개.
- 파생: 음수 PPE 취득 현금흐름을 양수 cash CAPEX로 변환한 1개, 보고된 YoY를 사용하는 수출 vintage 3개.
- 재무매출/영업이익은 같은 기간임을 확인해 margin을 파생할 수 있다. 회계 원자료 여러 행을 독립 positive evidence로 세지 않는다.
- Spot 7개는 비교 시점이 없으므로 방향 unknown. 전체 CAPEX/FCF는 무형자산 CAPEX 미확보, Cash/Debt는 부채 미확보로 계속 unavailable이다.
- 실제 회계 사실의 Company 대사 3개는 통과했고, Memory Business와 Industry Supply는 non_applicable였다.

## 검증 및 불변성

**170 tests passed = 기존 129 + 신규 41.** 요청한 15개 Golden 시나리오 모두 포함한다. Contract missing + Spot, 상반된 수출/DRAM, Horizon 충분성 차이, Hard withholding, Strong penalty, 원자료 미매핑 무영향, 단위 불일치, 같은 월 revision, Mapping Version 변경, 세 E11 영역을 검증했다. 추가로 공급자 충돌, 보고기간 혼합, 시점/모드, 조업일수, 파생 provenance, 후보 확률 불변, 기존 Liquidity Gate, 버전 manifest를 검증했다.

[최종 코드 CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34319281921)와 [태그 대상 CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34319310462)는 Python 3.11·3.12 모두 통과했다. 원래 fixture 실행·Replay와 schema/catalog 검증도 통과했다. 전체 제품 80개 Golden catalog의 미구현 release gate는 계속 닫혀 있다.

| 보존 항목 | 검증 |
|---|---|
| 첫 Journal `427e887c-48e2-5b7f-af46-e64e621d6be8` | 파일 SHA256 `3589081df5c7dd6c1bb9f83718d8acbe199e5de86dc4db40fdf5b362ab7fbb58` 동일; `7c36073` Replay 일치 |
| 두 번째 Journal `706bf699-1d02-5671-b1c0-005dc870714f` | 파일 SHA256 `c88e2cc2aa6bffbd2360616013f964e207b6d36a1f42af2ecbd9f3473a406d5e` 동일; `1eb1885` Replay 일치 |
| 기존 알고리즘·profile | 변경 없음; Weight/Prior/Calibration/ENTRY 80%/SELL 70% 유지 |
| Decision Engine | 변경 없음; Future Reasoning·Timing·Alignment·Liquidity·Confidence·Challenger 구조 유지 |

## 사용 경계와 후속 실행

공개 API는 `reasoning.refinement`의 `map_observations`, `assess_contract`, `evaluate_e11`, `publish_candidate`다. `publish_candidate`는 Future Reasoning 후보와 동일 Horizon/cutoff/mode/계약 버전의 평가만 받는다. 후보 확률을 생성하는 함수가 아니며, 거래 Decision을 반환하지 않는다.

```powershell
python -m reasoning.refinement.audit --verify-manifest config/contracts/real-world-contract-v2.0.0.json
python -m pytest -q
```

별도 감사 CLI는 기존 Journal을 읽어 새 분류 JSON을 exclusive-create로 저장한다. 네트워크 수집과 예측 실행 명령은 없다. 기존 live CLI는 v1 그대로이며 **후속 live 단계에서 v2 계약을 명시적으로 선택하고, Module State·E11·eligibility를 E01–E19 실행 경계에 연결해야 한다.** 이후 새 cutoff와 run_id로 실행하며 기존 Journal은 다시 쓰지 않는다. 이는 이번 계약 완료와 별개의 실제 실행 검증이다.
