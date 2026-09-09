# real-data-minimum-slice Act 2 결과

2026-09-09. 같은 Feature의 Act를 계속했다. **완료조건은 여전히 7/9이며 completed가 아니다.** 공식 원자료 연결과 두 번째 immutable Journal 생성은 완료했지만, 기존 계약을 그대로 유지하면서 E11 전체 항등식과 E18 최종 확률을 생성하는 문제는 해결되지 않았다.

## 실제 연결과 모델 투입의 구분

신규 공급자 3곳에서 원자료 7개를 수집했다. 삼성전자 PDF 3개, TrendForce DRAM Spot 공개 표 1개, 관세청 HWPX 3개다. 총 23개 수치 사실을 추출했다. KRX 안내문 수집은 수급 Source 확보로 계산하지 않았다.

| 신규 Source | 확보한 범위 | 상태 / 제한 |
|---|---|---|
| 삼성전자 공식 2026년 반기 연결재무제표 | 재무상태표·현금흐름표·손익계산서, KRW million | 13개 사실과 독립 대사 3개 확보. 기존 E11 입력으로 완전 변환할 수 없어 unmapped |
| TrendForce DRAM Spot | DDR3/4/5의 공개 SKU 7개 session average, 2026-09-09 11:00 GMT+8 | Spot만 기록. 전체 DRAM·HBM·계약가격 index로 대체하지 않음 |
| 관세청 8월 1~10일 | 반도체 수출 9,952 USD million, YoY 155.4% | 8월 11일 09:00 KST 발표; 이후 같은 월 20일 vintage로 대체 |
| 관세청 8월 1~20일 | 26,032 USD million, YoY 198.8% | 8월 21일 09:00 KST 발표; 8월 최신 확보 vintage로 선택 |
| 관세청 7월 월간 | 41,172 USD million, YoY 176.3% | 8월 18일 09:00 KST 발표; 수리일 기준 표 사용, 선적일 기준 값과 구분 |

원자료: [삼성전자 IR](https://www.samsung.com/global/ir/financial-information/audited-financial-statements/), [TrendForce Spot](https://www.trendforce.com/price/dram/dram_spot), [관세청 8월 10일](https://www.customs.go.kr/kcs/na/ntt/selectNttInfo.do?bbsId=1362&mi=2891&nttSn=10172763&nttSnUrl=baccec5a7b47a665ac4d22878c83804b), [8월 20일](https://www.customs.go.kr/kcs/na/ntt/selectNttInfo.do?bbsId=1362&mi=2891&nttSn=10173983&nttSnUrl=88748d91848cefc847351b9e9a2b4e1c), [7월 월간](https://www.customs.go.kr/kcs/na/ntt/selectNttInfo.do?bbsId=1362&mi=2891&nttSn=10173584&nttSnUrl=4fee7b9502f263377346349001e33a66).

`semiconductor_export_demand`를 source-level typed factor로 추가했다. 같은 월 발표는 최신 eligible release 하나만 선택하며, 누적기간이 늘어났다는 이유로 성장률을 추정하지 않는다. 현재 선택된 vintage는 7월 월간과 8월 1~20일이다. 기존 graph에는 이 Factor의 edge가 없으므로 인과 기여는 0이 아니라 **미연결**이다. 임의 weight/edge를 추가하지 않았다. 이번 실행에서 신규 원자료가 E01의 입력 coverage를 늘리지는 못했다.

## E11과 확률을 막는 원인

삼성전자 자료에서 `자산 = 부채 + 자본`, `현금 증감 = 영업 + 투자 + 재무 + 환율 효과`, `기말 현금 − 기초 현금 = 현금 증감`의 대사 3개는 residual 0으로 통과했다. 이 검증은 기존 E11의 생산능력·매출·free cash flow 항등식과 다르다.

기존 E11은 `production <= capacity`, `revenue = units_sold * unit_price`, `cash_flow = operating_cash - capex`를 모두 요구한다. 연결재무제표의 회사 전체 매출에는 단일 판매단위·단가가 없다. 현금흐름표의 현금 증감을 free cash flow라고 바꾸거나, 매출에서 단가를 역산해 항등식을 자명하게 통과시키지 않았다. 따라서 실제 회계 Evidence를 Journal의 E11 입력 평가에 연결했지만 E11 정상 계산을 완료했다고 보고하지 않는다.

E18의 직접 차단 요인은 `dram_contract_asp`: critical=true, unit=index이다. DRAM Spot의 USD/chip와 다른 입력이다. 기존 설계가 critical flag 변경을 금지하므로 Spot을 연결했어도 이 필수 입력은 계속 unavailable이다. 두 가지 문제는 단순 Source 추가만으로 해소되지 않는다. 원래 입력의 기준기간·범위를 식별할 수 있는 실제 계약가격 index와 E11에 맞는 독립 수량/단가 자료가 필요하다. 이를 구할 수 없다면 추후 명시적인 계약 설계 변경이 필요하며, 이번에는 변경하지 않았다.

## 두 번째 실행

- Prediction timestamp / cutoff: **2026-09-09 15:08:43.703255 KST**.
- run_id: `706bf699-1d02-5671-b1c0-005dc870714f`.
- immutable SHA256: `ffe85d54f1e805c898bfc31d941b66c680b2950cbe515716c5942be9e2a15cae`.
- 위치: `artifacts/local/live/38930375-01dd-5110-b4b6-9b4362bbcd5a/`.
- 시장 raw snapshot, 공식 문서 raw bytes, 출처·시각·해시, 파싱 사실, 회계 대사, 원래 114개 Engine execution, 설명서, Outcome 일정 보존.
- 기존 시장 feed 7개가 fresh. 삼성전자우 30분봉 263개, 일봉 4,931개로 주봉·월봉을 집계했다.

E01–E19를 3 Horizon × feedback 전후로 **114회 호출**했다. status success 108회 중 30회는 E02/E03/E04/E11/E13의 non-applicable이며, E18 6회는 insufficient_evidence다. 따라서 **19개 전체 정상 계산은 미충족**이다. Technical Feedback 및 재추론은 Horizon마다 한 번 실행됐다.

| Horizon | Up / Down / Flat 전 → 후 | 최종 Forecast Confidence | E14 진단 Confidence 전 → 후 | Decision |
|---|---|---|---|---|
| 1주 | null → null | null | 27.7630% → 27.6095% | WAIT |
| 1개월 | null → null | null | 27.2855% → 27.3694% | WAIT |
| 1년 | null → null | null | 28.0859% → 28.0449% | WAIT |

E14 수치는 최종 예측 Confidence가 아니다. 확률 및 확률 변화량은 생성되지 않았으며 0%로 표시하지 않는다. 원인은 critical input 부족이다. Feedback의 Regime/Flow/Reflexivity 효과와 upstream causal path는 설명서에서 조회할 수 있다.

| Horizon / primary + context | Bottom / Top score | Reversal 확인 | Bullish / Bearish Alignment | Buy / Sell Liquidity |
|---|---|---|---|---|
| 1주 / 30분 + 일봉 | 0.00 / 0.20 | 둘 다 false | 0.40 / 0.00 | null / null |
| 1개월 / 일봉 + 주봉 | 0.45 / 0.20 | 둘 다 false | 0.40 / 0.00 | null / null |
| 1년 / 주봉 + 월봉 | 0.00 / 0.10 | 둘 다 false | 0.40 / 0.00 | null / null |

Reversal은 기존 알고리즘의 점수이며 검증된 확률이 아니다. 중기 double-bottom 후보와 MA 조건이 있어도 neckline/거래량 등이 확인되지 않았다. 개별 RSI divergence, double pattern, neckline, MA, volume, ATR 결과는 [전체 설명서](real-data-minimum-slice.second-live-explainability.md)에 포함했다.

모든 Horizon의 실제 실패 ENTRY Gate는 `future_up`, `without_history_up`, `confidence`, `bottom_timing`, `alignment`, `liquidity`, `meta_check`이며 통과 Gate는 없다. 포지션 미보유 입력으로 WAIT가 나왔다. ENTRY 80%·SELL 70%는 그대로다. 수급이 없다는 사실과 확률 생성 실패를 혼동하지 않는다. 수급은 optional factor이지만 Liquidity Confirmation이 비어 거래를 차단한다. 이번 확률 실패는 별도의 critical 계약가격 문제다.

## 여전히 unavailable / unmapped

KRX 외국인·기관·프로그램 수급은 unavailable이다. [공식 이용절차](https://openapi.krx.co.kr/contents/OPP/INFO/OPPINFO003.jsp)에서 인증키 및 개별 서비스 승인이 필요함을 확인했으며, 승인된 데이터 응답을 확보하지 못했다. 안내 페이지 HTTP 200을 수급 연결 성공으로 세지 않았다.

원래 모델의 missing factor 13개: `hyperscaler_capex`, `gpu_demand_growth`, `dram_contract_asp`, `hbm_demand`, `cxmt_memory_capacity`, `samsung_eps`, `samsung_eps_revision`, `foreign_net_buy`, `institution_net_buy`, `program_net_buy`, `semiconductor_relative_flow`, `samsung_forward_per`, `equity_discount_rate`. 회계 원자료는 이제 확보되었지만 원래 `Accounting` 객체는 unavailable이다. 신규 Spot/수출/재무 사실은 source available, model unmapped로 구분한다.

What Would Change My Mind: 원래 index 정의에 맞는 계약가격 관측과 독립적인 E11 자료가 확보되면 새 run에서 재실행한다. Forecast가 생성된 이후에도 reversal 확인, alignment, 실제 liquidity gate가 별도로 통과해야 한다. 성숙한 historical evidence와 누락 Factor 확보는 confidence 평가에 필요하다. 어떤 경우에도 과거 Journal을 수정하거나 지금 시장에 맞게 threshold를 조절하지 않는다.

## 첫 번째와 두 번째 Journal의 차이

| 항목 | 첫 Journal | 두 번째 Journal |
|---|---|---|
| run_id | `427e887c-48e2-5b7f-af46-e64e621d6be8` | `706bf699-1d02-5671-b1c0-005dc870714f` |
| cutoff KST | 14:51:04.715969 | 15:08:43.703255 |
| 공식 추가 문서 / typed facts | 0 / 0 | 7 / 23 |
| 실제 모델 Factor coverage | 7/20 | 7/20 |
| E11 원래 항등식 | unavailable | unavailable + 실제 재무 대사 3개 별도 보존 |
| 수치 확률 / Decision | 없음 / WAIT | 없음 / WAIT |
| 알고리즘·profile·threshold | 동결 | 동일 |

두 실행의 E14 진단 수치와 Wave/Alignment 결과도 동일했다. 수집 시각·provenance ID·Journal 구조·전체 source hash는 달라졌지만 모델을 새 데이터에 맞춰 조절한 차이가 아니다. 신규 문서가 아직 unmapped이므로 확률을 바꾸었다고 해석할 수 없다.

첫 Journal hash `b74c172436e164e3989885d4a031970e66a5ae92ccb7a738ae31ddc3652e03cf` 유지. 첫 Journal은 기록된 commit `7c36073`에서, 두 번째는 `1eb1885`에서 raw Replay 완전 일치했다. 기록된 code identity가 다르므로 첫 것을 새 코드로 다시 계산한 결과로 덮어쓰지 않았다. 현 코드에서도 첫 Journal integrity 검증은 통과한다.

## 테스트 / CI / 최종 판정

로컬 **129 passed**: 원래 fixture 89개 + 기존 data-boundary 20개 + 신규 adapter 20개. [CI 34317775848](https://github.com/donchang07/sec_future_reasoning/actions/runs/34317775848)은 Python 3.11·3.12 모두 성공했다. schema/catalog validate, fixture 생성 및 replay도 성공했다. 아직 구현되지 않은 전체 제품 Golden release gate는 의도대로 닫혀 있으며, 80개 제품 Golden 전체를 통과했다고 주장하지 않는다.

| 기존 완료조건 | 결과 |
|---|---|
| 시장 Source 최소 6개 | 충족 |
| 실제 30분·일·주봉 Wave | 충족 |
| E01–E19 전체 정상 실행 | **미충족** |
| Technical Feedback 후 재추론 1회 | 충족 |
| Horizon별 수치 확률과 Decision | **미충족: WAIT만 생성** |
| 사람이 읽는 설명서 | 충족 |
| immutable live_forward Journal | 충족 |
| 동일 raw Replay | 충족 |
| 기존 fixture 회귀 테스트 | 충족 |

최종 상태: `act / blocked_contract_mapping`, **7/9**. 같은 Feature를 유지한다. 상세 기계 판정은 [Act evidence](../03-analysis/real-data-minimum-slice.act2-evidence.json), 구현 전 결정은 [Act 설계](../02-design/features/real-data-minimum-slice.act2-design.md)를 참조한다.
