# 49 Factor Registry 설계

> Version: ontology-design-v1 · 2026-09-09 · [통합 Design](../sec-future-reasoning-v1-1.design.md)

## 1. 정의와 출처 상태

Canonical은 49 Factor를 요구하지만 목록 전체를 제공하지 않는다. 아래는 상세 PRD의 명시 개념을 우선해 구성한 49개 설계 후보이며, 원문 공식 49개 목록을 복구했다고 주장하지 않는다.

`E`는 상세 PRD에 Factor 개념이 직접 등장함, `D`는 명시 개념으로부터 파생한 수치 정의, `P`는 구현을 위해 추가한 제안이다. E도 정확한 series/unit/vendor 선택까지 원문이 지정했다는 뜻은 아니다. 모든 row는 구현 전에 source_id, series_id, timezone, release schedule, access status를 등록한다. 현재 공급자 연결 상태는 모두 `not_connected`다.

source group은 공급자 확정이 아니라 adapter 대상이다. `OFF`=공식 발표·중앙은행·통계기관, `MKT`=허가된 시장데이터, `FIL`=기업 공시/IR, `IND`=허가된 산업 데이터, `DER`=관측에서 계산. 상세 공급자 endpoint·권한은 P2에서 확인하고 version에 고정한다.

| # | factor_id | Module | 값/단위·초기 transform | Cadence / SLA | Source | 근거 |
|---|---|---|---|---|---|---|
| 01 | us_2y_yield | macro | 연 수익률 % / diff pp | daily / 2 trading days | OFF/MKT | E: §2 US2Y |
| 02 | us_10y_yield | macro | 연 수익률 % / diff pp | daily / 2 trading days | OFF/MKT | E: §2, Scenario |
| 03 | fed_policy_rate | macro | 목표범위 상단 % / diff pp | event / next meeting | OFF | E: Fed |
| 04 | us_cpi_yoy | macro | 전년비 % / diff pp | monthly / 45d | OFF | E: CPI |
| 05 | us_payroll_change | macro | 월간 순증 천명 / diff | monthly / 45d | OFF | D: Employment |
| 06 | dxy | macro | index points / log_return | daily / 2 trading days | MKT | E: DXY |
| 07 | usdkrw | macro | KRW per USD / log_return | daily / 2 trading days | OFF/MKT | E: USDKRW |
| 08 | wti_oil | macro | USD/barrel / log_return | daily / 2 trading days | MKT | E: Oil/T06 |
| 09 | hyperscaler_capex | ai_demand | 고정 기업군 분기합계 USD million / yoy | quarterly / 120d | FIL | E: CAPEX |
| 10 | gpu_demand_growth | ai_demand | 고정 표본 출하 YoY % / level | quarterly / 120d | IND/FIL | D: GPU demand |
| 11 | ai_revenue_growth | ai_demand | 고정 기업군 AI revenue YoY % / level | quarterly / 120d | FIL | E: AI revenue |
| 12 | ai_usage_growth | ai_demand | 정의된 사용량 지수 YoY % / level | monthly / 45d | FIL/IND | D: usage |
| 13 | ai_capex_roi_proxy | ai_demand | incremental AI gross profit / lagged CAPEX 비율 | quarterly / 120d | DER/FIL | P: T16 ROI 정량화 제안 |
| 14 | dram_contract_asp | memory | 고정 DRAM basket 지수 / pct_change MoM | monthly / 45d | IND | E: DRAM ASP |
| 15 | dram_spot_price | memory | 고정 DRAM SKU USD/unit / pct_change | daily / 5 trading days | IND | E: T11 spot |
| 16 | hbm_demand | memory | HBM 수요 지수 / yoy | monthly / 45d | IND/FIL | E: HBM Demand |
| 17 | memory_inventory_days | memory | 표본기업 재고 days / diff | quarterly / 120d | FIL/IND | D: Inventory |
| 18 | memory_bit_growth | memory | 공급 bit YoY % / level | quarterly / 120d | FIL/IND | E: bit growth |
| 19 | hbm_order_growth | memory | 확인된 주문 bit YoY % / level | quarterly/event / 120d | FIL/IND | D: T13/T14 orders |
| 20 | samsung_memory_capacity | supply | DRAM-equivalent wafer/month / pct_change | monthly / 45d | FIL/IND | E: Samsung capacity |
| 21 | skhynix_memory_capacity | supply | 같은 기준 wafer/month / pct_change | monthly / 45d | FIL/IND | E: SKH capacity |
| 22 | micron_memory_capacity | supply | 같은 기준 wafer/month / pct_change | monthly / 45d | FIL/IND | E: Micron capacity |
| 23 | cxmt_memory_capacity | supply | 같은 기준 wafer/month / pct_change | monthly / 45d | FIL/IND | E: CXMT capacity |
| 24 | fab_ramp_lead_months | supply | 다음 증설의 생산까지 months / level | event / 90d | FIL/IND | D: fab schedule/T19 |
| 25 | samsung_revenue | earnings | 연결 분기 KRW billion / yoy | quarterly / 120d | FIL | E: revenue |
| 26 | samsung_operating_margin | earnings | 연결 영업이익률 % / diff pp | quarterly / 120d | FIL | E: margin |
| 27 | samsung_eps | earnings | 보통주 귀속 EPS KRW/share / yoy | quarterly / 120d | FIL | E: EPS |
| 28 | samsung_fcf | earnings | operating CF−CAPEX KRW billion / diff | quarterly / 120d | FIL/DER | E: FCF |
| 29 | samsung_eps_revision | earnings | 고정 consensus FY EPS 30d revision % | daily / 5 trading days | IND/MKT | E: revisions |
| 30 | samsung_capex | earnings | 분기 KRW billion / yoy | quarterly / 120d | FIL | E: T20 CAPEX |
| 31 | foreign_net_buy | capital_flow | 삼성 우선주 순매수 KRW million / level | daily / 1 trading day | MKT | E: foreign flow |
| 32 | institution_net_buy | capital_flow | 삼성 우선주 순매수 KRW million / level | daily / 1 trading day | MKT | E: institution flow |
| 33 | program_net_buy | capital_flow | 삼성 우선주 순매수 KRW million / level | daily / 1 trading day | MKT | E: program flow |
| 34 | semiconductor_relative_flow | capital_flow | sector net buy / turnover−market ratio | daily / 1 trading day | MKT/DER | D: sector relative flow |
| 35 | foreign_ownership_change | capital_flow | 삼성 우선주 지분율 변화 pp / diff | daily / 2 trading days | MKT | P: 누적 자금 검증 보조 |
| 36 | samsung_forward_per | valuation | common price / forward EPS 배 | daily / 2 trading days | MKT/DER | E: PER |
| 37 | samsung_pbr | valuation | common price / latest known BPS 배 | daily / 2 trading days | MKT/FIL/DER | E: PBR |
| 38 | equity_risk_premium | valuation | 정의된 implied ERP % / diff pp | monthly / 45d | IND/DER | E: ERP |
| 39 | equity_discount_rate | valuation | risk-free + beta×ERP % / diff pp | daily / 2 trading days | DER | D: discount rate |
| 40 | samsung_common_price | preferred | unadjusted KRW/share / log_return | 30m/daily / 1 bar | MKT | E: Samsung common |
| 41 | samsung_preferred_price | preferred | unadjusted KRW/share / log_return | 30m/daily / 1 bar | MKT | E: Samsung preferred |
| 42 | preferred_discount | preferred | 1−preferred/common 비율 / diff | daily / 1 trading day | DER | E: common/preferred spread |
| 43 | preferred_dividend_yield | preferred | trailing known cash dividends/price 비율 | daily/event / 2 trading days | FIL/MKT/DER | E: dividend |
| 44 | preferred_turnover_ratio | preferred | traded shares/free-float shares 비율 | daily / 1 trading day | MKT/DER | D: liquidity |
| 45 | preferred_rsi_14 | market_regime | Wilder RSI14 0..100 / level | 30m/daily / 1 bar | DER | E: RSI |
| 46 | preferred_trend_alignment | market_regime | price와 SMA20/60/120 정렬 -1..1 | 30m/daily / 1 bar | DER | D: trend |
| 47 | preferred_realized_volatility | market_regime | trailing20 daily return 연율 std 비율 | daily / 1 trading day | DER | D: volatility |
| 48 | preferred_volume_z | market_regime | trailing20 volume z-score / level | 30m/daily / 1 bar | DER | D: volume |
| 49 | preferred_overheat_percentile | market_regime | price−SMA20 거리의 trailing252 percentile | daily / 1 trading day | DER | P: overheat 정량화 제안 |

## 2. 보조 데이터는 Factor 개수에 포함하지 않는다

OHLCV bar, corporate actions, trading calendar, consensus vintage, event actual/expected, beta, BPS, shares outstanding/free float, accounting cash/debt/financing, fab utilization/yield, source quotation은 원천 및 제약 보조 데이터다. 이를 누락한 채 49개 scalar만으로 모든 Engine을 실행할 수 있다고 가정하지 않는다.

49 ID는 9 Module에 각각 8/5/6/5/6/5/4/5/5개다. 동일 Factor의 여러 시간척도는 `(factor_id,timeframe)` 관측이며 Factor ID 수를 늘리지 않는다. 공급 capacity를 DRAM-equivalent로 변환할 수 없으면 원단위를 보존하고 비교 effect는 unknown이다.

## 3. Registry의 구현 필드

`factor_id`, `name_ko`, `module_id`, `unit`, `value_type`, `transform`, `comparison_period`, `warmup`, `cadence`, `expected_release_at`, `freshness_sla`, `critical_for_horizons`, `source_candidates`, `source_status`, `provenance_class`, `prd_reference`, `derived_from`, `economic_sign_by_regime`, `quality_tolerances`, `ontology_version`를 필수로 한다. label만 있는 빈 항목은 허용하지 않는다.

초기 required set: 1d/1w는 preferred_price/us10y/usdkrw/foreign_net_buy/volume/trend, 1m은 앞 집합+dram_contract_asp/hbm_demand/eps_revision, 3m/1y는 memory+ai_capex+supply+earnings+valuation을 포함한다. Module별 coverage .5 규칙과 함께 적용한다. 특히 critical set을 모르는 값으로 채운 경우 Forecast는 insufficient_evidence다.

## 4. Freshness·충돌·가공 규칙

- trading-day SLA는 해당 시장 거래 캘린더를 따른다. event 수치는 새 이벤트가 없다는 이유만으로 매일 stale 처리하지 않고 다음 예정 발표와 검증 일정을 기준으로 한다.
- 공시 YoY는 비교 가능한 분기·회계기준·통화를 확인한다. 가이던스와 실적, 계획 capacity와 가동 capacity는 다른 observation kind다.
- first slice의 5 핵심 series는 #40/#41/#02/#07/#31이다. timing 계산에는 별도 OHLCV history와 higher-timeframe warmup이 필요하다.
- price 소스 충돌 초기 허용범위는 동일 시각·통화·조정기준에서 0.5%, 금리 1bp, FX 0.1%다. industrial series는 같은 basket/SKU일 때만 비교한다. 이 수치는 quality-rule-experimental-v1로 version 관리한다.
- net flow의 common/preferred 집계를 혼용하지 않는다. common-only flow를 preferred proxy로 사용하는 경우 proxy flag와 감액 규칙을 별도 Design에 남긴다.
- derived Factor는 모든 input observation refs와 formula version을 기록한다. 어떤 input이 stale/unknown이면 output도 그 상태를 전파한다.
- §3의 최종 critical matrix와 source series 매핑은 P1/P2 기능 Design에 machine-readable 형태로 옮긴다. 공급자 확인이 안 된 항목은 raw/derived dummy 값으로 성공 처리하지 않는다.
