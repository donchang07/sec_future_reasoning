# live-forward-v2 — 완료 보고

real-world-contract-v2.0.0을 사용하는 첫 삼성전자우 live_forward Journal을 생성·봉인했다. **1주와 1개월은 Forecast 생성, 1년은 insufficient_evidence, 최종 판단은 모두 WAIT**다. 예측을 본 뒤 코드·계약·Weight·Prior·Calibration·Threshold를 바꾸지 않았다.

- Prediction / cutoff: **2026-09-09 15:42:34.193123 KST** (06:42:34.193123 UTC).
- Run ID: `e51235a7-9c47-575b-b152-dab8cee04c17`.
- Contract `real-world-contract-v2.0.0`, Semantic Mapping `semantic-mapping-v1.0.0`, Requirement Matrix `economic-bucket-quorum-v1`.
- 실행 코드 `73c30f77608813bafcecf137e413e88b3c01d7cf`; [실행 전 lock](../03-analysis/live-forward-v2.pre-run-lock.json)을 수집 전에 GitHub에 게시했다.
- Journal SHA256: `40c54c137865fdbb9f24c2750455a2ffa974b16ff2c51059ddc12f2f2f958002`.
- **P0 = 197,500원**, 2026-09-09 15:00 KST에 끝난 실제 30분봉 종가. 현재 체결 가능 호가가 아니다.

## 최종 결과

확률·Confidence는 %, Reversal은 0~1 점수다. Reversal 점수를 보정된 확률로 해석하지 않는다. Alignment는 bullish/bearish 순서다.

| Horizon | Up | Down | Flat | Confidence | Bottom Reversal | Top Reversal | Alignment | Liquidity | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1주 | 40.8039% | 37.1848% | 22.0113% | 11.9883% | 0.00 | 0.10 | 0.40 / 0.00 | unavailable | WAIT |
| 1개월 | 41.1889% | 36.4456% | 22.3655% | 5.6435% | 0.45 | 0.20 | 0.40 / 0.00 | unavailable | WAIT |
| 1년 | withheld | withheld | withheld | withheld | 0.00 | 0.10 | 0.40 / 0.00 | unavailable | WAIT |

1년 Memory coverage는 **0.2667 < 0.50**, 인정되는 독립 Memory family도 수출 하나뿐이다. Spot은 계약상 1년 Evidence에서 제외된다. 따라서 숫자를 만들지 않았다. 재무 항등식 실패 때문이 아니다.

## Feedback 전후

Up / Down / Flat 순서. 변화량은 percentage point다.

| Horizon | Feedback 전 | Feedback 후 | Δ Up / Down / Flat |
|---|---|---|---|
| 1주 | 41.3002 / 36.7398 / 21.9599% | 40.8039 / 37.1848 / 22.0113% | −0.4964 / +0.4450 / +0.0514 pp |
| 1개월 | 40.2916 / 37.2812 / 22.4271% | 41.1889 / 36.4456 / 22.3655% | +0.8973 / −0.8356 / −0.0617 pp |
| 1년 | insufficient_evidence | insufficient_evidence | 계산하지 않음 |

각 Horizon에 technical batch 한 개만 만들고 1회 반영했다. 단기는 Regime −0.015, Reflexivity −0.010, 중기는 +0.0375, +0.025, 장기는 −0.015, −0.010이다. 수급 부재로 Capital Flow feedback은 0이며 실제 Flow 기여가 추가되지 않았다. 이후 E01–E19를 다시 호출했다.

## 왜 이 확률인가

1주 Up은 Prior 40%에서 아래 Ledger를 따라 **40.8038723637%**가 된다. 실제 Journal에는 모든 단계의 Up/Down/Flat before/after, edge/root 참조가 포함된다.

| 단계 | Up 변화 pp |
|---|---:|
| RSI 경로 | +0.370161 |
| Trend Alignment 경로 | +2.732963 |
| 삼성전자 보통주 경로 | +2.415333 |
| 삼성전자우 가격 경로 | +2.432001 |
| 미국 10년물 경로 | −6.025332 |
| USD/KRW 경로 | +0.207540 |
| Actor/Reflexivity | +0.320643 |
| Scenario simulation | +0.650343 |
| Challenger | −1.270333 |
| Historical adjustment | 0.000000 |
| Calibration | −1.029448 |

1주 Positive Driver 5개는 Trend Alignment, 삼성전자 보통주, 삼성전자우, RSI, USD/KRW 경로다. 1개월·1년의 순서는 보통주, 우선주, Trend Alignment, RSI, USD/KRW다. Negative causal driver는 미국 10년물 하나만 존재하므로 5개를 억지로 채우지 않았다. 1년 경로는 중간 reasoning artifact이며 발행된 확률의 근거로 오인하면 안 된다.

**이 방향은 기존 baseline 대비 수준 정규화를 따른다.** 최근 가격이 하락했어도 고정 baseline보다 높은 수준이면 positive가 될 수 있다. Semantic change의 부호와 엔진 정규화를 각각 기록했고, 이를 보고 baseline이나 Weight를 수정하지 않았다.

E09에서 동일 root의 중복 경로를 제거하고 E12에 전달한다. E10 상호작용, E17 시나리오, E14 Challenger, E13 Historical, E18 Calibration이 Ledger에 이어진다. 새 confidence penalty를 probability에 추가로 섞지 않았다.

1주 Confidence에는 외국인·기관 Strong Evidence 결측으로 multiplier 0.9가 적용됐다. 1개월은 Contract ASP, HBM demand/price, EPS/revision, 외국인·기관 결측과 Memory coverage를 반영한 multiplier **0.42525**가 적용됐다. 그 전에도 기존 E06/E14가 적은 방향 Evidence와 상충 경로를 반영해 Confidence를 낮춘다.

## 실제 Source와 의미 구분

삼성전자우 30분봉/일봉, 삼성전자 일봉, KOSPI, USD/KRW, DXY, 미국 Treasury 10년물의 7개 시장 피드가 fresh였다. 삼성전자 IR 연결 재무상태표·현금흐름표·손익계산서, TrendForce DRAM Spot, 관세청 10일·20일·월간의 7개 자료도 확보했다. 모든 원본과 수집 시각은 raw bundle에 보존했다.

- 재무 Evidence로 E11 Company 검증이 통과했다. Memory business와 Industry supply는 non_applicable이며 실패나 통과로 꾸미지 않았다.
- Spot 7개 SKU는 실제 가격 값으로 매핑됐지만 비교할 이전 값이 없으므로 directional signal은 null이다. Contract ASP나 HBM Price로 대체하지 않았다.
- 8월 10일→20일은 같은 월의 nowcast revision으로 처리했다. 7월 확정과 8월 최신 nowcast는 별도 월 root다. 수출 강세 signal은 있지만 frozen Graph에 경로가 없어 방향 contribution은 없다.
- KOSPI/DXY는 수집됐으나 발행된 Mapping에 유효 규칙이 없어 unmapped로 남았다.
- **여전히 unavailable:** DRAM Contract ASP, 외국인·기관·프로그램 수급. HBM demand/price, memory inventory/bit shipment, EPS/revision, 전체 cash CAPEX/FCF, debt ratio, memory segment 및 산업 공급 검증용 자료도 확보되지 않았다.

원래 documentary adapter의 `available_unmapped` 문자열은 v1 기준 상태다. 새 v2의 실제 매핑 상태는 Journal의 MappingBatch/Dispositions를 따른다. 원본 문자열은 바꾸지 않았다.

## Wave/Reversal과 Gate

| Horizon | Primary + context | RSI | Fast/Medium/Slow 대비 | Double Bottom / Top | Neckline 확정 | Volume ratio |
|---|---|---:|---|---|---|---:|
| 1주 | 30분 + 일 | 48.3866 | 아래 / 위 / 위 | 없음 / 없음 | 양쪽 미확정 | 0.8941 |
| 1개월 | 일 + 주 | 55.2699 | 위 / 위 / 위 | 있음 / 있음 | 양쪽 미확정 | 0.8888 |
| 1년 | 주 + 월 | 56.0352 | 위 / 위 / 위 | 없음 / 없음 | 양쪽 미확정 | 0.5331 |

세 Horizon 모두 RSI divergence, 최종 Bottom/Top confirmation은 false다. Volume ratio는 직전 20봉 평균 대비이며 모두 1 미만이다. 일봉은 MA reclaim feature가 true지만 neckline/volume 확인 부족으로 bottom 확정이 아니다. Fast/Medium/Slow는 원래 20/60/120 SMA다.

30분봉 마지막은 9월 9일 15:00, 일봉은 9월 8일, 주봉은 9월 4일, 월봉은 8월 31일이다. 수집 cutoff 당시 지연 공개 여유까지 적용해 마지막 30분봉·당일 일봉은 제외했고 진행 중인 주·월도 완성봉으로 넣지 않았다.

1주·1개월 통과 Gate는 meta_check뿐이다. **future_up, without_history_up, confidence, bottom_timing, alignment, liquidity**가 실패했다. 1년은 Forecast 부재로 meta_check도 실패했다. ENTRY 80%, SELL 70% 및 다른 Gate는 그대로다. 실제 보유 정보가 없어 held=false로 기록했으므로 대기 상태는 WAIT다.

What Would Change My Mind: 1주는 실제 수급·확정 Bottom·Alignment와 충분한 Future/Confidence, 1개월은 여기에 Contract/HBM/Earnings Evidence 보강, 1년은 최소 Memory coverage와 2개 이상 family 확보가 필요하다. E07의 Factor별 반증 조건도 전체 보고서와 Journal에 있다. 조건이 달라져도 **새 run을 생성**하며 이 Journal을 다시 계산해 덮어쓰지 않는다.

## 보존과 검증

E01–E19 × 3 Horizon × 2 generation = **114회**. 112 success(24 non_applicable payload 포함), 장기 E18 2회는 계약에 따른 insufficient_evidence다. 기존 두 Journal은 그대로이며 기존 코드 Replay도 유지했다.

동일 raw/code/contract/runtime Replay가 전체 Journal hash까지 일치했다. 실행 전·후 로컬 테스트 **187/187**(기존 170 + 새 17), [CI Python 3.11/3.12](https://github.com/donchang07/sec_future_reasoning/actions/runs/34320231170)도 통과했다. 시스템 전체의 미구현 Golden release gate는 계속 닫혀 있다.

Outcome은 2026-09-10, 09-16, 10-09, 2027-09-09 각각 15:42:34.193123 KST 이후 첫 완료 종가를 별도 파일로 연결하는 구조다. 예측 시점의 Journal은 수정하지 않는다. 아직 Outcome은 없다.

- [봉인 Journal](../03-analysis/live-forward-v2.sealed-journal.json)
- [전체 Explainability / Ledger / Source freshness](live-forward-v2.full-explainability.md)
- [Check 및 다음 PDCA Finding](../03-analysis/live-forward-v2.analysis.md)
- 원시 응답: `artifacts/local/live-v2/939ddfa9-af80-5651-a700-6972d9e23ef3/raw-bundle.json` (원본 로컬 보존).

Act에서는 코드 수정 대신 LV2-F01~F05를 후속 과제로 등록하고, 봉인·재현·회귀 검증을 확인했다. 이 Feature의 완료는 첫 Forward Evidence 저장 완료이며 예측 정확도 검증 완료를 뜻하지 않는다.
