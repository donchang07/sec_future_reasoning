# 07:00 Daily Forecast 운영정책 전환 보고

2026-09-10. 운영정책 `daily-preopen-v1.0.0`, 운영코드 `forward-ops-v1.1.0`.

## 변경과 실행 확인

기존 16:10 예약을 중지하고 **매일 07:00 KST** 예약으로 교체했다. 다음 자동 실행은 **2026-09-11 07:00 KST**다. Python 3.11/3.12 CI 통과 후 활성화했으며, 활성화 후 예약 작업 경로 실행도 종료 코드 0이었다. 오늘 낮의 자동 호출은 시간창 밖이므로 새 예측을 추가하지 않았다. 실제 완료 시각은 수집 소요 시간만큼 달라지며 07:00으로 소급하지 않는다.

오늘만 승인된 예외 예측은 **2026-09-10 12:15:33.112563 KST**에 봉인했다. 사용자가 요청한 12:05는 요청 당시 시각이며 실행 시각으로 꾸며 쓰지 않았다.

- Run ID: `2ce0e81e-6569-53de-8b7a-fc7ecd854d7a`
- Contract: `real-world-contract-v2.0.0`; 원래 E01–E19/Weight/Prior/Calibration/Decision/ENTRY 80%/SELL 70% 유지
- Journal SHA256: `17335bcc5508f7a2675977ecd9c30054ac617c702f5fd20156f6168887ed7aa7`
- 한국 가격·수급 cutoff: **2026-09-09 15:30 KST**
- 미국 시장 cutoff: **2026-09-09 16:00 EDT = 2026-09-10 05:00 KST**
- 지식/수집 cutoff: **2026-09-10 12:15:33 KST**
- P0: **197,500원**, 9월 9일 삼성전자우 완료 일봉 종가. 현재 체결가격이 아니다.

## Horizon 결과

확률과 Confidence는 %, Bottom/Top은 보정된 확률이 아닌 0–1 알고리즘 score다. Alignment는 bullish/bearish다.

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment | Liquidity | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1주 | 44.4074 | 34.1754 | 21.4172 | 16.1764 | unavailable | unavailable | unavailable | unavailable | WAIT |
| 1개월 | 43.1804 | 34.8810 | 21.9386 | 7.4879 | 0.45 | 0.20 | 0.40 / 0.00 | unavailable | WAIT |
| 1년 | withheld | withheld | withheld | unavailable | 0.00 | 0.10 | 0.40 / 0.00 | unavailable | WAIT |

1년은 `coverage:memory`, `memory_family_quorum` 때문에 숫자를 만들지 않았다. 1주·1개월 ENTRY 실패 Gate는 `future_up`, `without_history_up`, `confidence`, `bottom_timing`, `alignment`, `liquidity`다. `meta_check`만 통과했고, 1년은 이것도 실패했다. 개별 수급을 시장 현물·선물로 대체하지 않았다.

## Feedback 전후

| Horizon | 전 Up / Down / Flat (%) | 후 Up / Down / Flat (%) | 변화 Up / Down / Flat (pp) |
|---|---|---|---|
| 1주 | 44.4074 / 34.1754 / 21.4172 | 44.4074 / 34.1754 / 21.4172 | 0 / 0 / 0 |
| 1개월 | 42.2587 / 35.7019 / 22.0395 | 43.1804 / 34.8810 / 21.9386 | +0.9218 / −0.8209 / −0.1009 |
| 1년 | insufficient_evidence | insufficient_evidence | 산출하지 않음 |

각 Horizon에 Feedback을 한 번 적용했다. 1주 primary 30m은 stale로 제외되어 기술 효과가 0이었다. 1개월은 일봉의 Bottom/Top 차이에 따라 frozen 로직의 regime +0.0375, reflexivity +0.025가 적용됐고, flow 효과는 0이다. 1년에도 기술 artifact는 기록했지만 Memory coverage 부족으로 확률은 계속 보류했다.

전체 E01–E19 실행 기록은 **114회**, success **112회**, 장기 E18 insufficient_evidence **2회**다. 산출된 전/후 4개 Probability ledger 모두 prior부터 최종 확률까지 정확히 재구성했다.

## 실제 데이터 제한

원본 응답은 그대로 저장하고 cutoff를 넘는 16개 행을 별도 admitted bundle에서 제외했다. 오늘 한국 장중 30분봉과 일봉을 사용하지 않았다. 기존 freshness 규칙상 전일 30분봉은 오늘 낮에는 stale이므로 단기 Wave와 Alignment가 unavailable이다. 원자료 자체가 없다는 의미와 구분된다.

일봉은 9월 9일, 주봉은 9월 4일, 월봉은 8월 31일까지 사용했다. 일봉 RSI 54.72, 주봉 RSI 56.04. 일봉 double-bottom 형태는 탐지됐지만 neckline·volume·divergence를 포함한 Bottom Confirmation은 충족하지 않았다.

**이번 실행이 직전 미국 세션 전체를 반영했다는 뜻은 아니다.** 동결된 Treasury/DXY/환율 일봉 계약의 provider-local end-of-day 시각이 미국 cash close보다 늦어, 이번에는 **9월 8일 provider date** 자료까지 허용됐다. 미국 9월 9일 자료를 16:00으로 임의 재표시하지 않았다. 이 제약은 결과를 보기 전 Design의 OP-F01로 기록했다. SOX·미국 개별 반도체주·유가를 새 Direction Factor로 추가하지 않았다. 더 나은 overnight coverage는 별도 Source Contract PDCA가 필요하다.

외국인·기관·프로그램 개별 수급과 DRAM Contract ASP는 계속 unavailable이다. TrendForce Spot, 관세청 수출, 삼성전자 재무자료의 기존 의미/매핑도 변경하지 않았다. Confidence를 낮춘 Strong Evidence와 positive/negative causal paths, RSI/neckline/거래량, What Would Change My Mind는 아래 전체 보고서에 있다.

## 검증과 Forward Evaluation

**245개 테스트 통과 = 기존 221 + 신규 24**. [활성화 전 CI](https://github.com/donchang07/sec_future_reasoning/actions/runs/34432581517)는 Python 3.11·3.12 모두 성공했다. 기존 4개 Live Journal의 당시 코드 Replay와 새 예외 Run의 raw→admission→Journal Replay가 모두 일치했다. 원래 두 v1 Journal과 기존 v2/Daily의 기록을 수정하지 않았다. 새 결과 확인 후 모델·운영코드 변경도 없었다.

동일 날짜의 예외 재실행은 같은 Run을 반환했다. 현재 등록 Journal 3개, 중복 날짜를 제거한 Forward Case **2/20**, 연결 대기 Outcome **12개**다. 아직 실제 성능 지표를 계산할 성숙 Outcome은 없다.

오늘 Journal의 Outcome due는 1일 9월 11일, 1주 9월 17일, 1개월 10월 10일, 1년 2027년 9월 10일 각각 **12:15:33 KST**다. 각 due 이상인 첫 실제 완료 종가를 별도 Outcome으로 연결한다. 이전 15:42/16:16 예측의 만기를 07:00으로 바꾸지 않았다. Windows 예약은 로그인된 사용자 세션·전원·네트워크가 필요하다.

## 산출물

- [Plan](../01-plan/features/daily-0700-operating-policy.plan.md), [Design](../02-design/features/daily-0700-operating-policy.design.md), [Check](../03-analysis/daily-0700-operating-policy.analysis.md)
- [봉인된 예외 Journal](../03-analysis/daily-0700-operating-policy.exception-journal.json)
- [전체 Explainability 및 Contribution Ledger](daily-0700-operating-policy.full-explainability.md)
- [검증 Evidence](../03-analysis/daily-0700-operating-policy.evidence.json), [운영 사용법](../FORWARD_OPERATIONS.md)

Act: 운영 전환은 완료했으며 OP-F01–03은 제한사항으로 유지한다. 결과에 맞춘 임계값·Weight 조정은 하지 않았다.
