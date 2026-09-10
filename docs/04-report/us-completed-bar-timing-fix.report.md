# 미국 Completed-Bar / Data Availability 점검 및 수정

2026-09-10. Data Timing Bug Fix `source-timing-v1.0.1`, 운영정책 `daily-preopen-v1.0.1`.

## 확인된 원인과 수정

기존 코드는 미국 자료의 날짜를 모두 provider-local **23:59:59**로 변환했다. 따라서 9월 9일 Treasury 행이 Source에 있어도 미국 cutoff인 16:00 ET보다 뒤로 취급되어 제외됐다. Treasury의 관측 기준은 **약 15:30 ET**이며, 이는 실제 게시 시각과 구분해야 한다. 새 adapter는 실제 수집된 공식 행의 날짜와 이 관측 기준을 사용하되 `time_precision=date`, `released_at=null`, 실제 `collected_at`을 유지한다. [Treasury 공식 설명](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics)

Nasdaq 주식 정규장은 16:00 ET 종료이며 공식 조기 폐장일은 13:00이다. 새 가용성 진단은 거래 캘린더·Source regular-session metadata·해당 세션의 유효 OHLCV·20분 지연 여유를 함께 확인한다. 장후 `regularMarketPrice`나 진행 중 일봉을 완료 종가로 사용하지 않는다. [Nasdaq 거래시간·휴장일](https://www.nasdaq.com/market-activity/stock-market-holiday-schedule)

이 수정은 데이터 준비 계층에만 적용했다. `reasoning/`, `config/`, E01–E19, Causal Graph, Weight, Prior, Calibration, ENTRY 80%, SELL 70%는 변경하지 않았다.

## 실제 Source 점검 결과

**실제 수집 완료: 2026-09-10 12:26:25 KST. 대상 세션: 미국 2026-09-09.** 아래는 이 캡처 시점의 판정이다.

| 자료 | 실제 확인 | 판정 및 적용 범위 |
|---|---|---|
| Nasdaq Composite | 9/9 regular-session OHLCV 존재 | 완료 정규장 bar 가용, 별도 진단만 |
| SOX | 9/9 regular-session OHLCV 존재 | 완료 정규장 bar 가용, 별도 진단만 |
| NVDA / AMD / MU / AVGO / TSM ADR | 5종 모두 9/9 OHLCV 존재 | 완료 정규장 bar 가용, 별도 진단만 |
| 미국 10년물 Treasury par yield | 공식 XML 9/9 행 존재, 4.83% | 약 15:30 ET 관측 자료 가용; 다음 Run부터 기존 us_10y_yield Factor의 시각 처리만 수정 |
| DXY `DX-Y.NYB` | Source 응답/값은 존재 | **unavailable**: cash index 일봉을 16:00 종가나 ICE DX 선물 settlement로 볼 근거 미검증 |
| 유가 `CL=F` | Source 응답/값은 존재 | **unavailable**: 연속선물 일봉이 특정 만기 계약의 공식 settlement임을 확인하지 못함 |
| USD/KRW `KRW=X` | Source 응답은 존재 | **unavailable**: London 일봉 구간이 미국 cash-session cutoff와 맞지 않음 |

DXY cash index와 ICE DX 선물은 다른 자료다. WTI daily settlement도 일반 연속선물 OHLCV와 구분해야 한다. 값이 보인다는 이유로 종가·settlement 의미를 바꾸지 않았다. [ICE DX 명세](https://www.ice.com/api/productguide/spec/194/pdf), [CME settlement 설명](https://www.cmegroup.com/market-data/daily-settlements.html)

Yahoo의 완료 정규장 판정은 **수정 불가능한 거래소 최종값 인증이 아니다**. Source의 final flag는 없으므로 `provider_final=null`, `revisable=true`다. 수집 당시 원본을 보존해 이후 수정 여부를 추적할 수 있다.

## 07:00에 쓸 수 있는가

정규장 16:00 ET는 서머타임 기간 05:00 KST, 겨울에는 06:00 KST다. Treasury 약 15:30 ET 관측은 각각 04:30/05:30 KST다. 따라서 **07:00 실제 수집 시 해당 날짜의 행이 이미 제공된다면** 완료 정규장 자료와 Treasury 관측을 사용할 시간 조건은 충족한다. Source 지연·누락·상충이 있으면 unavailable이며, 과거 행을 최신값으로 간주하지 않는다.

**오늘 12:26 캡처는 오늘 07:00 가용성을 증명하지 못한다.** 모든 Source에 `availability_at_0700=unknown_not_captured_by_0700`를 기록했다. 정확한 공개 시각도 만들지 않았다. 다음 실제 예약 Run에서 그때의 raw 응답과 수집 시각, 가용/누락 사유를 보관한다. Prediction cutoff는 명목상 07:00이 아닌 그 Run의 실제 수집 완료 시각이다.

## 운영과 보존

- Python 3.11/3.12 CI 성공 후 bug-fix 정책을 07:00 예약에 적용했다. 다음 실행은 **2026-09-11 07:00 KST**다.
- [Version tag source-timing-v1.0.1](https://github.com/donchang07/sec_future_reasoning/tree/source-timing-v1.0.1), 코드 `64ff66ba355919eea49b95bbb1c59327f4018fe8`.
- 기존 다섯 Prediction Journal과 당시 판단을 변경하지 않았다. 9/10 12:15 예측도 그대로다.
- 이번 점검에서는 **새 Prediction을 생성하지 않았다**. 오늘 공식 Daily는 여전히 1개, 등록 Forward Journal은 3개다.
- Nasdaq/SOX/새 반도체주/유가는 `availability_diagnostic`에만 저장된다. 신규 Factor나 Causal Edge를 추가하지 않았다.
- Treasury의 target-date 행이 없거나 cutoff 이후 관측이면 기존 E01부터 missing이 전달된다. FX/DXY도 미검증 일봉을 이전 날짜로 조용히 대체하지 않는다.

## 검증

**266개 테스트 통과: 기존 245 + 신규 21.** [CI 34433429184](https://github.com/donchang07/sec_future_reasoning/actions/runs/34433429184)에서 Python 3.11·3.12 모두 성공했다. 늦은 수집의 look-ahead 방지, target-date 결측, 미래 행 제외, 상충 revision, 조기 폐장·DST, 장후 quote 제외, OHLCV 검증, 미검증 DXY/FX/WTI 차단, E01 결측 전달, 비미국 데이터 준비 불변, frozen model hash를 확인했다.

기존 v1 두 개, 원본 v2, 16:10 Daily, 첫 preopen 예외 Journal 등 **5개 Replay 모두 일치**했다. 기존 preopen은 당시 운영 commit `6479777`과 원래 admission으로 재현한다. 새 timing 계약으로 과거 예측을 다시 쓰지 않는다.

가용성 Audit `41437225-f7bf-425e-8b8f-485592d496a3`도 동일 raw에서 Replay가 일치했다. SHA256: `b8ca2b4f77a74657098e50d8f970498002b46b7ef956407706785602e2c878b3`.

[Plan](../01-plan/features/us-completed-bar-timing-fix.plan.md) · [Design](../02-design/features/us-completed-bar-timing-fix.design.md) · [Check](../03-analysis/us-completed-bar-timing-fix.analysis.md) · [봉인된 Source별 가용성 Audit](../03-analysis/us-completed-bar-timing-fix.availability-audit.json)
