# Act: real-data-minimum-slice — external evidence required

2026-09-09 · [Check](../03-analysis/real-data-minimum-slice.analysis.md) · **Feature is not complete**

Plan → Design → Do → Check까지 수행하고 각 산출물을 GitHub에 게시했다. Act에서 확인한 남은 간극은 API/원자료 접근과 실제 필수 근거 부족이다. 사용자 금지사항을 지키면서 이 간극을 engine weight/threshold/critical flag 변경이나 synthetic 값으로 해소할 수 없다. 9개 완료조건 중 7개 충족 상태를 유지한다.

## 보존한 첫 forward evidence

- 한국시간 2026-09-09 14:51:04.715969, mode live_forward.
- run_id: `427e887c-48e2-5b7f-af46-e64e621d6be8`.
- Journal SHA256: `b74c172436e164e3989885d4a031970e66a5ae92ccb7a738ae31ddc3652e03cf`.
- 로컬: `artifacts/local/live/b3c93b04-4a31-5f23-b3b9-bb2d176a50b0/prediction-journal.json`.
- [사람이 읽는 첫 Explainability Report](real-data-minimum-slice.first-live-explainability.md).
- 같은 raw/cutoff/version으로 전체 replay 일치. 새 원자료가 확보되면 **새 시각의 별도 forward run**을 만든다. 이 Journal을 수정하거나 과거 Prediction을 재생성하지 않는다.

## 남은 source 의존성

| ID | 필요한 실제 근거 | 현재 상태 | 다음 입력/작업 |
|---|---|---|---|
| RD-A01 | DRAM contract price 또는 의미·단위가 검증된 memory price series | unavailable, E18 critical gate | 이용 가능한 provider/series/라이선스, machine-readable API 접근이 필요. proxy는 별도 source/semantic 설계를 먼저 검증 |
| RD-A02 | preferred 또는 명시된 시장 범위의 foreign/institution/program net flow | KIS/KRX 권한 미확보, liquidity unknown | 공식 read-only API 접근. 종목/시장·수량/금액 단위·집계 시점을 구분 |
| RD-A03 | production/capacity/revenue/cash identity 실제 사실 | unavailable, E11 non-applicable | 검증 가능한 공시/원자료 및 해당 accounting contract에 맞는 실제 값. 추정값 보충 금지 |
| RD-A04 | 안정적인 공식 주가 feed와 독립 검증 | Yahoo JSON fallback 사용 | KIS/KRX 접근 가능 시 adapter 우선순위/교차검증 추가. 첫 raw는 유지 |

환경변수 이름 수준의 검사에서 KIS/ECOS/FRED/KRX credential은 확인되지 않았다. 키 자체를 대화나 GitHub 문서에 붙일 필요는 없다. 다음 작업을 시작하려면 사용 가능한 공급자·series 및 안전하게 설정된 credential의 변수 이름을 확인해야 한다. 새 계정 생성·유료 구독·주문 실행은 수행하지 않았다.

## 이번 Act에서 지킨 처리 원칙

1. Data unavailable → 원본 상태와 E01 coverage 35%를 보존하고 기존 E06/E14 penalty를 유지했다.
2. DRAM critical을 optional로 낮추지 않았다. 최종 확률/확률 변화량은 null이다.
3. 회계·event·historical evidence를 fixture에서 가져오지 않았다. 수치가 없는 engine을 정상 근거로 통과했다고 보고하지 않았다.
4. Bottom/Top 기존 score를 calibrated probability로 표시하지 않았다.
5. 기존 89개 및 신규 20개 테스트, [CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34316550373), legacy Journal hash 검증을 통과했다.
6. 자동으로 source 권한을 얻을 수 없으므로 현재 Feature의 status를 `act / blocked_external_data`로 기록하고 완료 보고로 닫지 않는다.

## Outcome 계획

1일: 2026-09-10 14:51:04.715969 KST, 1주: 2026-09-16 같은 시각, 1개월: 2026-10-09 같은 시각이다. 휴장 시 첫 유효 관측을 append-only Outcome으로 연결할 수 있다. 실제 future value는 아직 없고 schedule만 존재한다. 수집된 원본/시각을 검증한 별도 Outcome 객체가 원래 run_id와 hash를 참조해야 한다.

현재 결과: 세 Horizon 모두 **WAIT / insufficient_evidence**. 이것은 모델 개선을 위해 보존할 첫 실데이터 실행 증거이며, 사용자가 요구한 숫자 Forecast 완료를 대체하지 않는다.
