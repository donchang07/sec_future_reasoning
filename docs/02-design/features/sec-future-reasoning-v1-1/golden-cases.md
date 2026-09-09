# Golden 80개 원문 사례와 구현 추적

> Design 1.0.0 · 2026-09-09 · 원문을 자동 추출했으며 테스트 실행 결과가 아니다.

[통합 Design](../sec-future-reasoning-v1-1.design.md) · [상세 PRD 원문](../../../samsung_future_reasoning_prd_v1.1.html)

## 1. 원문 보존과 판정 규칙

아래 기대값은 원문 그대로다. P1 테스트 fixture는 source_expected와 design_expected를 분리한다. 수치화를 위해 필요한 consensus/graph/version/baseline/cutoff/Position/technical evidence를 inputs와 assumptions에 추가한다. T01–T57의 정성 기대는 baseline 대비 관계와 원문 수치 범위를 각각 검증한다. 입력이 불완전한 사례는 unresolved로 남기고 pass로 계산하지 않는다.

T58–T65는 Forecast를 주입하는 독립 policy test로 시작한다. T59/T62 및 MT02–MT04/MT06의 누락 timing/alignment/liquidity/confidence는 모두 충족하는 fixture 가정을 명시하며, 누락 상태 자체는 별도 WAIT/HOLD 사례로 검증한다. T64/MT10은 Horizon별 Position을 별도 설정한다. MT05는 상위 강한 상승과 full SELL의 충돌로 Design에서 HOLD+경고를 선택했음을 별도 design_expected에 기록한다. 원문 기대값을 수정하지 않는다.

T66–T70은 합계/ledger/버전/불변성 oracle이며, MT09는 실제 feedback 후 generation 갱신과 재계산 trace를 검증한다. WATCH/NO ACTION은 경고·사유로 매핑하고 Action은 네 가지로 유지한다. 필수 Golden 실패 또는 unresolved는 release를 차단한다.

## 2. T01–T70

| ID | Scenario | Inputs | Horizon | Expected | Signal |
|---|---|---|---|---|---|
| T01 | Benign macro + memory boom | 10Y4.4; KRW1330; DRAM+12; AI strong; foreign buy | 1M | UP 80-90 | ENTRY |
| T02 | Hawkish FOMC | 10Y5.05; KRW1390; hawkish; foreign sell | 1W | DOWN 70-82 | SELL |
| T03 | Dovish hike priced-in | 25bp expected; 10Y→4.6; memory strong | 1W | UP 55-70 | WAIT/HOLD |
| T04 | Hot CPI surprise | CPI +0.4pp; 10Y+18bp; KRW weak | 1W | DOWN 65-78 | WATCH/SELL |
| T05 | Strong jobs benign inflation | jobs strong; CPI benign | 1W | mixed 45-60 UP | WAIT |
| T06 | Oil shock | WTI +15%; yields↑ | 1W | DOWN 55-70 | WATCH |
| T07 | FX shock | DXY↑; KRW1420; foreign sell | 1W | DOWN 70+ | SELL |
| T08 | Foreign buy divergence | market weak; Samsung foreign heavy buy | 1W | UP > baseline | WAIT/ENTRY |
| T09 | Foreign sell divergence | price↑; foreign heavy sell | 1W | turning risk↑ | WATCH SELL |
| T10 | DRAM contract +20 | inventory low; HBM strong | 1M | UP 75-88 | ENTRY boundary |
| T11 | DRAM spot rollover | spot -12%; contract flat | 1M | UP falls | HOLD/WATCH |
| T12 | Inventory spike | inventory high; ASP weak | 1M | DOWN 65-78 | SELL boundary |
| T13 | HBM surge | AI CAPEX strong; HBM orders↑ | 3M | UP 75-88 | ENTRY boundary |
| T14 | HBM disappointment | AI CAPEX strong; HBM orders↓ | 3M | UP below baseline | WAIT |
| T15 | AI capex acceleration | CAPEX +40%; ROI stable | 1Y | UP 75-90 | ENTRY boundary |
| T16 | AI debt stress | CAPEX +40%; ROI weak; yields↑ | 1Y | UP 45-60 | WAIT |
| T17 | Weak monetization | usage↑; revenue/margin weak | 1Y | UP reduced | WAIT |
| T18 | CXMT early ramp | capacity +35%; early ramp | 1Y | DOWN 55-70 | WATCH |
| T19 | CXMT delayed | capacity plan; ramp +2Y | 1W | minimal effect | HOLD/WAIT |
| T20 | Samsung capex surge | current shortage; capex↑ | 1W vs1Y | short UP > long UP | different |
| T21 | Supply discipline | SKH/Micron capex controlled | 1Y | UP higher | HOLD/ENTRY |
| T22 | Yield improvement | effective supply↑ faster | 1Y | UP lower | WAIT |
| T23 | EPS revision +20 | rates stable | 1M | UP 80+ | ENTRY |
| T24 | EPS strong + rate 5.2 | EPS+20; 10Y5.2 | 1M | UP 45-60 | WAIT |
| T25 | FCF deterioration | earnings↑; FCF↓ | 1Y | confidence/UP reduced | WAIT |
| T26 | Shareholder return surprise | cash return↑ | 1M | Preferred UP boost | ENTRY boundary |
| T27 | Extreme pref discount | discount wide; common stable | 1M | relative UP | ENTRY if overall |
| T28 | Pref discount closes | discount normalizes | 1M | support fades | HOLD |
| T29 | Breakout + volume + flow | 20/60 positive; vol z high; foreign buy | 1W | UP 70-85 | ENTRY boundary |
| T30 | Overbought no flow | RSI high; volume fades; foreign sell | 1W | DOWN risk↑ | WATCH SELL |
| T31 | Reflexive squeeze | heavy buy; momentum high | 1W | UP 75-85 | ENTRY boundary |
| T32 | Forced deleveraging | vol spike; sell; rates↑ | 1W | DOWN 80+ | SELL |
| T33 | Missing memory data | DRAM/HBM unknown | 1M | Confidence <55 | NO ACTION |
| T34 | Conflicting sources | DRAM sources conflict | 1M | confidence reduced | WAIT |
| T35 | Stale data | memory data stale 60d | 1M | confidence reduced | WAIT |
| T36 | Priced-in hawkish | hawkish event 90% expected | 1W | downside < raw model | HOLD/WAIT |
| T37 | Unexpected dovish | dovish surprise; 10Y↓; KRW↑ | 1W | UP rises sharply | ENTRY boundary |
| T38 | Historical bullish trap | current neutral; past analogs bullish | 1W | history capped | NO threshold jump |
| T39 | Historical bearish trap | current positive; past analogs bearish | 1M | history capped | No forced SELL |
| T40 | Regime structural break | old rate relation stops working | 1M | confidence↓; regime-change flag | WAIT |
| T41 | Impossible revenue scenario | demand↓ price↓ volume↓ revenue↑ | 1Y | scenario rejected | N/A |
| T42 | Impossible capacity ramp | fab output +50% next week | 1W | scenario rejected | N/A |
| T43 | Accounting cash violation | FCF negative but cash rises without financing | 1Y | scenario rejected | N/A |
| T44 | Actor response Fed | inflation↑ but Fed assumed dovish no reason | 1M | scenario challenge/reject | N/A |
| T45 | Actor response CXMT | price high; CXMT capacity constrained | 1Y | supply response capped | HOLD |
| T46 | Path double count | HBM and DRAM constraint same causal source | 1M | duplicate contribution removed | No inflation |
| T47 | Opposing paths | AI boom boosts EPS and yields | 1M | mid probability 45-65 | WAIT |
| T48 | Lag test | new fab announced today | 1D | near-zero supply effect | HOLD/WAIT |
| T49 | Lag maturation | fab ramp reaches production | 1Y | supply effect material | WATCH |
| T50 | Turning point early warning | price↑; flow↓; ASP momentum↓; rates↑ | 1W | transition risk high | WATCH SELL |
| T51 | False turning point | price↑; flow briefly↓; EPS/ASP accelerate | 1W | warning suppressed | HOLD |
| T52 | Confidence high alignment | official sources agree | 1M | confidence >75 | policy eligible |
| T53 | Confidence low rumor | rumor-only supply shock | 1M | confidence <50 | NO ACTION |
| T54 | User bullish bias | user bullish; evidence neutral | 1W | no upward adjustment from user belief | WAIT |
| T55 | AI anchoring bias | prior forecast bullish; new data bearish | 1W | forecast updates bearish | SELL boundary |
| T56 | Challenger wins | main bull but counter evidence stronger | 1W | main hypothesis replaced | depends |
| T57 | Challenger weak | counter lacks evidence | 1M | main retained | depends |
| T58 | Entry threshold 79 | UP79; conf85; no challenge | 1M | UP79 | WAIT |
| T59 | Entry threshold 80 | UP80; conf75; no challenge | 1M | UP80 | ENTRY |
| T60 | Entry low confidence | UP85; conf55 | 1M | UP85 conf55 | NO ACTION |
| T61 | Sell threshold 69 | DOWN69; conf80; held | 1W | DOWN69 | HOLD |
| T62 | Sell threshold 70 | DOWN70; conf70; held | 1W | DOWN70 | SELL |
| T63 | Sell low confidence | DOWN80; conf50 | 1W | DOWN80 conf50 | HOLD/WATCH |
| T64 | Short sell, long entry | FOMC risk high; long AI/memory strong | 1W/1Y | short DOWN>70; long UP>80 | SELL short / ENTRY long |
| T65 | Short entry, long risk | flow squeeze; CXMT long risk | 1W/1Y | short UP>80; long UP<60 | ENTRY short / WAIT long |
| T66 | Probability sum | arbitrary valid inputs | all | UP+DOWN+FLAT=100 | N/A |
| T67 | Contribution reconstruction | known contribution set | 1M | final equals stored deltas/calibration | N/A |
| T68 | Graph version regression | same data; graph version changed | 1M | diff explained by edge/version | N/A |
| T69 | Model version regression | same graph; calibrator changed | 1M | diff localized to calibration | N/A |
| T70 | Prediction Journal immutability | past forecast outcome known | all | original snapshot unchanged | N/A |

## 3. MT01–MT10

| ID | 상황 | Expected |
|---|---|---|
| MT01 | 30분봉 Bottom Reversal 강함, 일봉 하락, Future Upside 55% | WAIT — 기술적 반등만으로 Entry 금지 |
| MT02 | 30분봉 Bottom Reversal 82%, 일봉 정렬 76%, Future Upside 84%, Confidence 80% | 단기 ENTRY |
| MT03 | 일봉 Bottom Reversal 85%, 주봉 정렬 80%, Future Upside 83% | 중기 ENTRY |
| MT04 | 주봉 Bottom Reversal 82%, 월봉 정렬 78%, Future Upside 86% | 장기 ENTRY |
| MT05 | 30분봉 Top Reversal 80%, Future Downside 75%, 일봉 상승 강함 | 단기 SELL 또는 축소, 중장기 유지 가능 |
| MT06 | 일봉 Top Reversal 72%, Future Downside 74%, 주봉도 하락 전환 | 중기 SELL |
| MT07 | Future Upside 88%, Bottom Reversal 40% | WAIT — 방향은 좋으나 타이밍 미확인 |
| MT08 | Bottom Reversal 90%, Future Upside 52% | WAIT — 기술적 반등일 가능성 |
| MT09 | Bottom Reversal 이후 외국인/기관 수급 전환 | Liquidity Score와 Future Reasoning 재계산 |
| MT10 | 단기 SELL, 중기 HOLD, 장기 ENTRY 조건 | Horizon별 Position 독립 관리 |

## 4. 실행 결과 스키마

각 결과는 case_id, source_expected, design_expected, assumptions, fixture_hash, run_id, cutoff, versions, status, actual, tolerance, changed_engine_ids, changed_edge_ids, changed_calibration, reason을 포함한다. status는 passed/failed/unresolved/skipped다. 단계 미구현을 skipped로 표시할 수 있으나 release 통과로 집계하지 않는다.

현재 상태: 카탈로그 80개 추출 완료. fixture 수치화·실행 테스트는 구현 단계에서 수행하며 실행 통과 건수는 아직 없다.
