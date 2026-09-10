# Frozen Forward Operations 사용법

Baseline은 `real-world-contract-v2.0.0`과 `73c30f77608813bafcecf137e413e88b3c01d7cf` 코드다. `forward_ops`는 원래 `live_v2.evaluate`를 별도 프로세스에서 실행한다. 모든 신규 수급·Event·Human Forecast는 모델 입력에서 제외된다. 이 문서의 예시는 입력 형식이며 실제 Evidence가 아니다.

## 실행과 Monitoring

저장 위치는 기본 `artifacts/local/forward-evaluation-v1`이며 Git에서 제외된다. 자료를 제출하기 전에 원자료의 단위·대상·마감일·공개 시각을 확인한다. 출처 없는 값이나 추정값을 넣지 않는다.

```powershell
.venv/Scripts/python.exe -m forward_ops bootstrap
.venv/Scripts/python.exe -m forward_ops daily
.venv/Scripts/python.exe -m forward_ops serve --port 8678
```

화면: http://127.0.0.1:8678. Forecast Horizon을 선택하면 기여 Ledger와 Gate, E09/E10/E11, source freshness를 조회한다. Shadow 진단과 Human Forecast, 평가 점수는 별도 영역이다. UI는 읽기 전용이며 입력은 아래 CLI를 사용한다.

공식 Daily는 운영정책 `daily-preopen-v1.0.0`에 따라 매일 **07:00 KST**에 시작한다. 자동 지연·재시도는 09:00 전까지만 허용하며 그 밖에는 skipped다. 사용자 로그인·전원·네트워크가 필요하다. 같은 날짜의 `daily:YYYY-MM-DD`는 정책 버전이 달라도 한 번만 봉인한다. 주말·휴일에도 전일 가용 자료로 실행하되 기존 freshness/coverage 정책 때문에 결과가 withheld일 수 있다. 한국 가격·수급은 관측된 직전 한국 종가까지, 미국·FX는 직전 NYSE core close를 넘지 않는 기존 timestamp 의미의 자료만 사용한다. 원본 raw와 별도 admitted bundle, market_cutoffs를 함께 보관한다. 이전 16:10 정책은 역사적 기록으로만 보존한다.

예외 실행은 명시적으로 허용된 날짜에만 `daily --exception-date YYYY-MM-DD --exception-reason "승인된 예외 사유"`로 실행한다. 날짜가 현재 KST 날짜와 다르면 거절된다. 결과 시각은 실제 수집 완료 시각이며 07:00으로 소급하지 않는다. `not_ready`는 종료 코드 2, 예약 작업은 30분 간격 최대 3회 재시도하되 09:00 이후에는 실행하지 않는다. [정책 설계 및 알려진 데이터 제한](02-design/features/daily-0700-operating-policy.design.md)을 참고한다.

```powershell
./scripts/install-forward-schedule.ps1
Get-ScheduledTask -TaskName SEC-Frozen-Forward-Daily
Get-ScheduledTaskInfo -TaskName SEC-Frozen-Forward-Daily
```

현재 환경은 Korea Standard Time이다. 설치기는 다른 OS timezone을 거절하며 검증·CI 통과 후 설치한다. 오류 로그는 `logs/`, 원시 응답 및 subprocess 로그는 `attempts/`에 남는다. 비정상 종료로 `active.lock`이 남으면 실행 중인 작업이 없는지 확인한 뒤 정확한 해당 lock 파일만 정리하고 재실행한다. 봉인된 결과는 삭제하거나 덮어쓰지 않는다. Outcome의 만기와 P0, Journal hash는 각 예측 당시 계약을 유지하므로 새 예약이 기존 평가 만기를 바꾸지 않는다. Replay CLI는 기록된 운영 버전에 따라 이전 worker 또는 새 admission 경로를 선택한다.

## Market Positioning Shadow 입력

입력 JSON 하나 또는 JSON 배열을 작성한다. 아래 자리표시자는 실제 값으로 교체해야 하며 그대로 제출하면 검증에서 거절된다.

```json
{
  "provenance": "human_supplied_market_close",
  "venue": "kospi_spot",
  "instrument": "KOSPI",
  "investor": "foreign",
  "measure": "net_buy_value",
  "unit": "krw_million",
  "value": "실제 순매수 금액을 숫자로 입력",
  "trade_date": "YYYY-MM-DD",
  "effective_at": "YYYY-MM-DDT15:30:00+09:00",
  "released_at": "원자료 공개 시각 ISO8601",
  "source_ref": "원자료 URL 또는 보존 파일 참조",
  "submitter": "입력자 식별용 별칭"
}
```

```powershell
.venv/Scripts/python.exe -m forward_ops position --input data/private/market-close.json
```

venue는 `kospi_spot`, `index_futures`, `stock_futures`, `program`, `usd_futures`, `stock_spot`, `sector_relative`로 나눈다. Futures는 `unit=contracts`, `measure=net_buy_contracts` 또는 `net_position_contracts`, `expiry=YYYY-MM`을 명시한다. 계약 수와 현물 KRW 금액을 더하지 않는다. 공통주 005930과 우선주 005935를 구분한다. 개별 우선주 수급도 이번 버전에서는 Shadow만 기록한다.

Sector relative flow는 `unit=ratio`, `measure=relative_flow`와 `operands`의 `sector_net_buy`, `sector_turnover`, `market_net_buy`, `market_turnover` 네 값을 모두 요구한다. turnover는 양수여야 하며 계산 값과 value가 일치해야 한다. 자동으로 Liquidity Factor에 넣지 않는다.

received_at은 서버가 기록한다. 수정 입력에는 기존 기록 해시를 `revision_of`로 남길 수 있다. 동일 시점 충돌은 제외하며, 다른 Source가 다르면 수집 시각만으로 한 Source를 우선하지 않는다. Shadow snapshot은 예측 수집 시작 전 받은 자료만 포함한다. 이후 들어온 수급은 이미 발행된 예측의 Shadow를 바꾸지 않는다.

## Event Shadow와 Event Run

`event_type`은 `FOMC`, `CPI`, `employment`, `samsung_earnings`다. 다음 필드를 실제 공개자료에서 작성한다.

| 필드 | 의미 |
|---|---|
| event_id | 공식 발표를 구분하는 고유 식별자; 중복 Event Run 금지 |
| field / unit / actual | 발표 항목과 단위, 실제 값 |
| released_at / source_ref | 공식 공개 시각과 출처 |
| consensus / consensus_at / consensus_ref | 같은 항목·단위의 사전 기대값 배열, 발표 전 확보 시각과 출처 |
| pre_move / expected_price_move | 사전 가격 변화와 별도로 확보한 기대 가격 변화, 수익률 소수 단위; 방향 추정 금지 |
| pre_start / pre_end | 발표 전에 끝난 가격 구간 |
| yield_before / yield_after | 미국 10년물 금리 %, 선택 항목 |
| yield_before_at / yield_after_at / yield_source_ref | 금리 반응의 시각과 출처 |

```powershell
.venv/Scripts/python.exe -m forward_ops event-input --input data/private/event.json
.venv/Scripts/python.exe -m forward_ops event --event-id 실제-등록한-event-id
```

기대값이 없거나 분산이 0이면 standardized surprise는 unknown이다. Event Diagnostic은 Baseline에 주입되지 않으며, Event Run의 모델은 당시 실제 시장 데이터만 원래 v2 경로로 실행한다. 급락·과매도·금리인상 자체를 ENTRY/SELL로 바꾸는 규칙은 없다.

## Human Forecast

`run_id`, `horizon`(1w/1m/1y), `human_id`, `probabilities`(up/down/flat 합계 1), `confidence`(0~1), `rationale`를 별도 JSON으로 제출한다. 서버 제출 시각을 사용하며 과거 제출로 backdate할 수 없다.

```powershell
.venv/Scripts/python.exe -m forward_ops human --input data/private/human-forecast.json
```

AI에 입력하지 않는다. 같은 사람·Run·Horizon의 첫 기한 전 기록을 독립 평가하고 후속 수정은 보존한다. due_at 이후 제출은 late로 저장하되 prospective 점수에서 제외한다. AI를 보고 작성할 수 있으므로 blinded=false다.

## Outcome / 평가 / Replay

새 Daily/Event Run을 수집하면 원시 일봉에서 이전 예측들의 due_at 이후 첫 완료 종가를 찾아 별도 Outcome으로 저장한다. 아직 도래하지 않은 Outcome은 pending이며 숫자 0으로 만들지 않는다. 1d Outcome은 보조 수익률이고 1w 예측의 정답으로 재사용하지 않는다.

```powershell
.venv/Scripts/python.exe -m forward_ops evaluate
.venv/Scripts/python.exe -m forward_ops replay --run-id 실제-run-id
.venv/Scripts/python.exe -m forward_ops outcomes --run-id 완료-일봉을-포함한-run-id
```

후자의 outcomes 명령은 지정 Run에 저장된 raw close snapshot으로 누락된 Outcome 등록을 재시도한다. 현재 cutoff 이후의 데이터를 예측 입력으로 소급해 넣지 않는다. 기존 `outcome_due`를 유지하므로 16시 이후 예측의 due 시각이 다음 날 종가보다 늦을 수 있다. 실제 측정 지연 시간을 기록한다(FE-F04).

Horizon별 Direction Accuracy, multiclass Brier(0~2), Probability reliability/ECE, Confidence calibration, False/Missed ENTRY·SELL 및 분모를 집계한다. Shadow 사후 비교는 Baseline 정오답과 해당 당시의 포지셔닝/Surprise를 연결한 기술 통계다. 인과관계·수익성·개선된 모델을 주장하지 않는다. 겹치는 Horizon과 같은 날 여러 기록은 독립 시행이 아니다. 최소 20개 사례 guard는 동일 session을 중복 계산하지 않는다.

UI/평가/Shadow에는 학습·튜닝 API가 없다. 20개 이후에도 별도 Contract PDCA 검증이 필요하다. 기존 두 v1 Journal은 계속 역사 기록으로 보존하고, 첫 v2 Journal부터 평가 대상으로 사용한다.
