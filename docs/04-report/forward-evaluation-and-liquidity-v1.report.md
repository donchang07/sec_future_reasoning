# forward-evaluation-and-liquidity-v1 — 운영 시작 보고

2026-09-09. Frozen Baseline의 Daily Forward Evaluation과 별도 Shadow Layer를 구현했다. Plan → Design → Do → Check를 수행했고, Act에서는 모델을 수정하지 않고 남은 검증·관측 항목을 기록했다. **Baseline 개선이나 Liquidity 대체 입력은 하지 않았다.**

## 현재 운영 상태

- Monitoring: **http://127.0.0.1:8678** — 로컬에서 실행 중. 세 Horizon과 Ledger, Gate, 실제 E09/E10/E11, Shadow 및 독립 평가를 조회한다.
- 예약 작업: `SEC-Frozen-Forward-Daily`, 매일 **16:10 KST**, 주말은 실행기에서 skip. 휴장·종가 미확보는 명시적으로 not_ready를 기록하고 30분 간격 최대 3회 재시도한다.
- 다음 예약: **2026-09-10 16:10 KST**. 설치 후 시험 실행 종료 코드 **0**. 사용자 로그인·전원·네트워크가 필요하다.
- 같은 날 재실행은 `already_sealed`로 처리했다. 이미 생성한 예측을 덮어쓰거나 다시 계산해 대체하지 않는다.

## 첫 Daily Close Prediction

Run ID `e5b62fea-3b19-5fc2-8a7a-b1e1788408f2`.
Cutoff **2026-09-09 16:16:28.273912 KST**.
P0 **197,500원**, 당일 15:30에 끝난 실제 30분봉 종가.
Journal SHA256 `ef6753118329b0e3c80de55cabe6720fc13f2bd98667ec84b8516a15a279a2c5`.

| Horizon | Up | Down | Flat | Confidence | Bottom | Top | Alignment bull/bear | Liquidity | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1주 | 44.4074% | 34.1754% | 21.4172% | 16.1764% | 0.10 | 0.10 | 0.40 / 0.00 | unavailable | WAIT |
| 1개월 | 43.1804% | 34.8810% | 21.9386% | 7.4879% | 0.45 | 0.20 | 0.40 / 0.00 | unavailable | WAIT |
| 1년 | withheld | withheld | withheld | withheld | 0.00 | 0.10 | 0.40 / 0.00 | unavailable | WAIT |

Bottom/Top은 반전 점수다. 이번에는 당일 완료 일봉과 15:30 완료 30분봉이 확보됐다. 총 30분봉 265, 일봉 4,932, 주봉 1,042, 월봉 239개이며 진행 중인 주·월은 포함하지 않았다.

Feedback 전/후 Up·Down·Flat:

| Horizon | 전 | 후 |
|---|---|---|
| 1주 | 44.4074 / 34.1754 / 21.4172% | 동일 |
| 1개월 | 42.2587 / 35.7019 / 22.0395% | 43.1804 / 34.8810 / 21.9386% |
| 1년 | insufficient_evidence | insufficient_evidence |

한 번의 기존 Technical feedback만 적용했다. 신규 Shadow 입력은 0개이고 모델 영향은 false다. 원래 ENTRY 80%, SELL 70%, Confidence/Timing/Alignment/Liquidity Gate를 그대로 적용했다. 장기는 기존 Memory coverage/family 기준으로 보류했다. 실제 보유 입력이 없는 frozen Baseline의 held=false도 유지했다. 따라서 현재 SELL/HOLD 평가 분모는 0이며 SELL 성능이 검증됐다고 말할 수 없다.

## 수급과 Event Shadow

KOSPI 외국인·기관 현물, 외국인 지수선물, 주식선물, 프로그램, 달러선물, 개별주 수급을 별도 구조화된 Market Positioning으로 저장할 수 있다. 현물 금액과 선물 계약 수를 합산하지 않으며, 만기·투자자·관측일·단위·수정·출처·수신 시각을 구분한다.

사람이 입력한 자료의 provenance는 `human_supplied_market_close`다. 공식 API 관측으로 위장하지 않는다. 삼성전자우 개별 수급도 이번 버전에서는 Shadow에만 저장한다. KRX의 원래 수급 Source가 여전히 unavailable이므로 기존 Liquidity Gate를 채우지 않았다.

FOMC/CPI/고용/삼성전자 실적 Event는 Expectation, standardized Surprise, 사전 가격 반영, 미국 10년물 반응과 Challenger Scenario를 독립 진단한다. 같은 시각의 실제 시장 snapshot으로 Event Run을 할 수 있지만 이벤트 값을 AI 방향 확률에 주입하지 않는다. 실제 공개 Event 입력이 없어 이번 세션에서 가짜 Event Run을 만들지 않았다.

실제 E09/E10 Artifact와 Shadow Interaction/Actor Diagnostic은 별개다. 최소 20개 이후에도 자동 연결하지 않으며 별도 Contract PDCA가 필요하다.

## Forward / Human / Shadow 평가

기존 첫 v2와 새 Daily의 **2개 Journal**을 등록했다. 동일 거래일이므로 20개 기준에서는 **독립 session 1개 / 20**으로 계산한다. 1일·1주·1개월·1년 Outcome **8개가 pending**, 완료 Outcome은 **0개**다. 아직 Accuracy/Brier 등의 실제 누적 성능 숫자는 없다.

- Direction Accuracy, multiclass Brier(0~2), Probability reliability/ECE, Confidence calibration을 Horizon별로 집계한다.
- False/Missed ENTRY·SELL은 사전 정의한 방향 기회 기준과 분모를 함께 보여준다. 실제 체결·비용·경로별 손절을 반영한 P&L로 주장하지 않는다.
- 1일 Outcome을 1주 Forecast의 정답으로 재사용하지 않는다. withheld는 평가에서 제외하고 0점으로 바꾸지 않는다.
- Human Forecast는 별도 저장한다. 기한 후 제출은 late로 보존하고 prospective 점수에서 제외한다. AI를 본 뒤 작성할 수 있으므로 blinded=false다.
- Outcome 후 당시 Shadow의 투자자·상품·단위·부호, Event Surprise와 Baseline 정오답/Brier/수익률을 연결해 비교한다. 표본 연관성 분석이며 인과관계나 확률 보정으로 사용하지 않는다.
- 원래 Journal의 정확한 due_at은 바꾸지 않았다. 종가가 due_at보다 먼저라면 다음 완료 종가로 측정될 수 있으며 지연 시간을 기록한다.

## 검증 / 남은 항목

**221개 테스트 통과 = 기존 187 + 신규 34**. [Python 3.11/3.12 CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34322896431) 통과. 신규 Raw Replay와 기존 세 Live Journal의 기록 당시 코드 Replay가 모두 일치했다. 새 Daily와 첫 v2의 VersionBundle도 동일함을 검증했다.

Check는 **14/15 확인, 1개 부분 확인(93.33%)**이다. Monitoring API와 브라우저 없이 실행한 DOM 테스트에서 초기 화면·세 Horizon·Ledger·보류 Horizon 전환을 확인했다. 연결된 브라우저가 없어서 실제 화면의 시각 검증은 하지 못했다(FE-F07). 이 제한을 통과로 처리하지 않았다.

Act에서는 FE-F01~07을 보존했다. 모델·Weight·Calibration·Threshold는 수정하지 않았다. 앞으로 실제 입력과 Outcome을 축적하고, Event 식별자는 실제 공식 발표별 canonical ID로 관리해야 한다. 아직 20개 조건이나 예측 정확도 검증이 완료된 것은 아니다.

## 산출물

- [사용법 / 수동 입력 / Event / Human / Replay](../FORWARD_OPERATIONS.md)
- [Plan](../01-plan/features/forward-evaluation-and-liquidity-v1.plan.md)
- [Design](../02-design/features/forward-evaluation-and-liquidity-v1.design.md)
- [Check / Findings](../03-analysis/forward-evaluation-and-liquidity-v1.analysis.md)
- [첫 Daily 봉인 Journal](../03-analysis/forward-evaluation-and-liquidity-v1.first-daily-journal.json)
- [첫 Daily 전체 Explainability / Ledger](forward-evaluation-and-liquidity-v1.first-daily-explainability.md)

원시 응답·운영 요청·수신 기록·미래 Outcome/Human 입력은 `artifacts/local/forward-evaluation-v1`에 별도 보존한다. 이후 수신한 개인의 판단이나 수동 자료를 자동으로 GitHub에 게시하지 않는다.
