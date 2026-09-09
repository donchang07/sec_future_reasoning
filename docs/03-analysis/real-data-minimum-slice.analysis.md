# Check: real-data-minimum-slice

2026-09-09 · 구현 commit `7c36073d74afc16ae21c44717ae12da2d90fa377`

**부분 달성, 완료 아님.** 사용자 완료조건 9개 중 7개 충족, 2개 blocked(77.78%)다. 실제 데이터를 수집하여 첫 live_forward Journal을 저장하고 같은 raw snapshot replay에 성공했다. 그러나 DRAM critical 입력과 회계 근거가 없어서 모든 19개 엔진이 정상 수치 결과를 내거나 Horizon별 최종 확률을 생성하지 못했다. 이 조건을 optional로 낮추거나 합성값으로 채우지 않았다.

## 실제 실행 증거

- Prediction timestamp / cutoff: `2026-09-09T05:51:04.715969+00:00` = 한국시간 14:51:04.715969.
- Mode: `live_forward`; run_id `427e887c-48e2-5b7f-af46-e64e621d6be8`.
- Journal SHA256: `b74c172436e164e3989885d4a031970e66a5ae92ccb7a738ae31ddc3652e03cf`.
- 저장 디렉터리: `artifacts/local/live/b3c93b04-4a31-5f23-b3b9-bb2d176a50b0/`.
- raw-snapshot / prediction-journal / explainability / outcome-schedule을 저장했다. 기존 파일을 덮어쓰지 않았다.
- [CI Python 3.11/3.12 성공](https://github.com/donchang07/sec_future_reasoning/actions/runs/34316550373). 로컬 109 passed = 기존 89 + 신규 20.
- 기존 fixture Journal `43c01ba0…`도 원래 hash 그대로 검증했다. engine/technical/decision 파일 hash는 변경되지 않았다.

## 완료조건 판정

| # | 조건 | 실제 결과 | 판정 |
|---|---|---|---|
| 1 | 실제 Source 최소 6개 | 6 instrument/series, 7 HTTP feeds, 2 providers. KOSPI/DXY는 context이고 기존 모델에 임의 edge 추가하지 않음 | 충족(독립 Provider 6개는 아님) |
| 2 | 실제 preferred 30m/daily/weekly Wave | 263 / 4,931 / 1,042 bars; monthly context 239개; 모두 available | 충족 |
| 3 | 실제 데이터 E01–E19 정상 통과 | 114회 호출, success 108(이 중 non-applicable 30), E18 insufficient_evidence 6; E11 회계 근거 없음 | blocked |
| 4 | technical feedback 후 재추론 1회 | generation 0/1, 각 19 engine invocation. E12 효과와 E14 evidence confidence 변경 확인 | 충족 |
| 5 | Horizon 확률과 Decision | 세 기간 WAIT; probability/forecast confidence 모두 null, prior를 final로 복사하지 않음 | blocked |
| 6 | Explainability report | source 상태, missing, driver/path, technical feature, gate, E09/E12/E13/E19, 반증 조건 보고 | 충족(숫자 확률 원장은 생성 불가) |
| 7 | 첫 live_forward immutable Journal | hash seal + exclusive create, mode 일관성 | 충족 |
| 8 | 같은 raw snapshot replay 일치 | 네트워크 없이 원본 raw와 cutoff 재실행, 전체 Journal equality 통과 | 충족 |
| 9 | fixture regression 유지 | 기존 89개 모두 통과, 총 109개 및 CI 통과 | 충족 |

## Source와 투입 범위

| Source | 채택된 rows | 상태 | 실제 모델 사용 |
|---|---:|---|---|
| 삼성전자우 30분 | 263 | fresh | Wave |
| 삼성전자우 일봉 | 4,931 | fresh | 가격 및 RSI/trend/volume 파생, weekly/monthly aggregation |
| 삼성전자 일봉 | 4,933 | fresh | 보통주 가격 |
| Treasury 10Y | 172 | fresh | US10Y |
| USD/KRW | 218 | fresh | 환율 |
| KOSPI | 243 | fresh | raw/context 보존; frozen graph에는 투입하지 않음 |
| DXY | 251 | fresh | raw/context 보존; frozen graph에는 투입하지 않음 |
| 외국인·기관·프로그램·DRAM | 0 | unavailable | 값 생성 안 함 |

현재 모델의 expected 20개 중 실제 4개 원천 Factor+3개 OHLCV 파생 Factor가 존재하여 E01 coverage는 35%다. expected metadata를 지워 coverage를 부풀리지 않았다. 회계/event/consensus/history도 합성값으로 채우지 않았다. 단일 소스별 수집이므로 현재 run에 독립 source 교차 검증은 없다. 공식 Treasury 외 Yahoo fallback의 한계는 Source Architecture에 명시되어 있다.

## Horizon 결과와 feedback

| 기간 | Final 확률 | E14 증거 confidence (전→후) | Bottom/Top score | Bullish alignment | Liquidity | 결정 |
|---|---|---|---|---:|---|---|
| 1주 | insufficient_evidence | .277630→.276095 | .00 / .20 | .40 | unknown | WAIT |
| 1개월 | insufficient_evidence | .272855→.273694 | .45 / .20 | .40 | unknown | WAIT |
| 1년 | insufficient_evidence | .280859→.280449 | .00 / .10 | .40 | unknown | WAIT |

E14 confidence는 진단값이며 없는 Forecast confidence를 대체하지 않는다. Bottom/Top은 기존 uncalibrated score이며 검증된 reversal probability가 아니다. 세 기간 모두 Bottom/Top confirmed=false다. ENTRY의 probability, no-history probability, confidence, timing, alignment, liquidity, meta-check gate가 모두 실패했다. 통과한 ENTRY gate는 없다. SELL도 보유하지 않은 현재 상태와 불충분한 근거 때문에 제안되지 않는다.

E12 합산 효과는 1주 .063646→.059699, 1개월 .034818→.036097, 1년 .033067→.032567로 바뀌었다. 이는 timing evidence의 Regime/Actor 해석 반영 결과이며 **확률 변화량이 아니다**. 흐름 자료가 없으므로 Capital Flow feedback은 unknown을 수치로 보충하지 않는다. 확률 전후 delta는 null로 남는다.

## 추가 경계 검사

unavailable, stale, conflict, timezone, cutoff, revision, look-ahead, 30m missing, intraday-vs-close, immutable storage, same-raw replay를 검사했다. 완성되지 않은 첫 aggregation bucket, provider release time 불명, mode 혼합, Treasury XML, 기존 엔진 hash, 전체 114 offline invocation, 조기 Outcome 연결도 검사했다. 테스트용 응답은 synthetic_fixture이며 live 결과와 섞지 않았다.

## 남은 간극과 Act

- 실제 DRAM 또는 의미·단위·원천이 검증된 Memory 가격 series와 수급 API 권한이 필요하다. 광범위 반도체 PPI/ETF를 DRAM으로 위장하지 않는다.
- E11 production/capacity/revenue/cash identity에 필요한 실제 회계 근거가 추가로 필요하다. 정상 회계값을 복사하지 않았다.
- 최초 live 출력은 고정된 실험 baseline/scale에서 일부 가격 신호가 포화될 수 있다. 이 실행을 보고 scale/weight를 조정하지 않았다. 후속 모델 변경은 별도 Plan/Design과 forward 비교 대상이다.
- Outcome은 immutable 연결 구조와 pending schedule까지다. 실제 1일/1주/1개월 가격은 아직 도래하지 않아 수집하지 않았다. API caller가 넣은 price의 출처 검증 자동화는 후속 작업이다.
- Source priority/authority는 명세와 현재 primary 선택에 반영되어 있으나 여러 provider의 자동 failover·독립 교차검증 운영은 아직 없다.
- 새 코드는 `python -m reasoning.live collect|verify|replay`로 제공한다. 기존 fixture CLI와 분리했다.

Act에서는 원자료 접근 의존성을 명시하고 원래 모델·첫 Journal을 보존한다. Feature를 complete 또는 100%로 표시하지 않는다.
