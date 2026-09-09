# Engine 계약·추론 모델·Timing 상세

> Design 1.0.0 · 2026-09-09 · [통합 Design](../sec-future-reasoning-v1-1.design.md)
> 이 문서의 실험 수치는 검증된 금융 예측 파라미터가 아니다. 모델·정책 버전과 함께 기록할 구현 가정이다.

## 1. Artifact payload 계약

모든 타입은 통합 Design의 공통 envelope를 포함한다. 근거는 evidence_refs로 연결하고, 배열은 ID로 결정론적으로 정렬한다. confidence는 [0,1] 또는 알려지지 않음을 나타내는 null이다. 자유형 설명은 표시용이며 다음 Engine의 계산 입력으로 파싱하지 않는다.

| Engine / 타입 | 필수 payload | 처리 / memory read | write / next / 실패 |
|---|---|---|---|
| E01 Data Interpretation / FactorSignal[] | factor_id, observation_ids, unit, level, change, velocity, acceleration, percentile, normalized, quality | cutoff 관측과 registry transform; 과거 기준 통계만 사용 | artifact factor_signals → E02; 단위 오류 quarantine, 표본 부족 표시 |
| E02 Event Understanding / StructuredEvent[] | event_id, type, actor_ids, factor_refs, actual, unit, occurred/published_at, evidence spans | source registry·ontology; LLM schema extraction 후 entity/수치 검증 | events/evidence refs → E03; 존재하지 않는 entity는 conflict, 재추출 최대 2회 |
| E03 Expectation & Surprise / SurpriseObject[] | event_id, actual, expected, surprise, scale, consensus_ids | event 이전 consensus, dispersion; (actual−expected)/scale | event_surprises → E04; consensus 없으면 surprise unknown |
| E04 Priced-in / PricedInEstimate[] | event_id, surprise_id, priced_in_fraction, residual_shock, pre_event_window | 사전 market path와 버전 있는 response mapping; 분모 0 차단 | priced_in_estimates → E05; mapping 불가하면 unknown, 임의 0 금지 |
| E05 Situation / SituationState | theme_ids, positive/negative refs, conflict_ids, missing_ids, dominant_module_ids | Signals/Events/ResidualShock/technical evidence; LLM 분류 후 refs 검증 | situation_states → E06; citation 불일치 retry |
| E06 State Estimation / ModuleState[] | module_id, score, direction, momentum, regime, confidence, coverage, top_factors, outgoing_effects | 9 Module registry와 정량 집계; unknown과 neutral 분리 | module_states → E07; critical data 부족 insufficient_evidence |
| E07 Hypothesis / Hypothesis[] | id, direction, horizon, claim_codes, support/contradict refs, falsifiers | E05/E06·domain ontology; bull/bear/flat 대안 생성 | hypotheses → E08; 근거 없는 주장 삭제, 빈 대안이면 부족 |
| E08 Causal Expansion / CausalPath[] | path_id, hypothesis_id, node/edge IDs, root_evidence_group, sign, strength, confidence, graph_version | pin된 Neo4j graph, 유효기간·regime 필터, path 길이≤6 | causal_paths → E09; graph 불일치 failed |
| E09 Interaction / AdjustedPath[] | path_id, original_effect, adjusted_effect, adjustment_codes, competing_refs, root_group | 중복·상쇄·포화·threshold, 교차 Module 중복 통제 | interaction_runs → E10; 순환/동일 근거 이중 가산 차단 |
| E10 Actor & Reflexivity / ActorResponse[] | actor_id, trigger_refs, action_code, response_range, constraints, feedback_refs | actor profile·정책/자금/설비 한계; LLM 후보→Rule 검증 | actor_runs → E11; 근거 없는 Fed/CXMT 반응 거절 |
| E11 Constraint & Identity / ConstraintResult[] | target_id, constraint_id, lhs, rhs, tolerance, valid, evidence_refs | revenue=price×volume, cash bridge, capacity×utilization×yield 등 | constraints → E12; violation은 경로/scenario 제외, 모두 무효면 부족 |
| E12 Temporal / TemporalPath[] | path_id, horizon, lag, active_fraction, decay, effect | graph lag/duration·target_at·calendar·경로 시작시각 | temporal_runs → E13; 해당 horizon에서 미성숙 효과 0과 unknown 구분 |
| E13 Historical Analogy / HistoricalEvidence | case_ids, similarity, recency, sample_count, regime_match, relevance, capped_delta | cutoff 이전 성숙 journal/outcome/experience만 | analogy_runs → E14; 사례 없음 applicable:false, current evidence 대체 금지 |
| E14 Challenger / ChallengeReport | claims[], refutation_refs, severity, fatal, replacement_hypothesis_id, confidence | 별도 반대 evidence 조회·기존 가설; LLM 검증 | challenge_runs → E15; ref 없는 fatal 판정 거절; evidence 부족 표시 |
| E15 Scenario Generation / Scenario[] | id, kind, hypothesis_id, prior_weight, overrides, shock_distributions, constraints | base/up/down/tail/user, distribution registry | scenarios → E16; 부적합 변수/범위 retry |
| E16 Consistency / ValidatedScenario[] | scenario_id, valid, violations, accepted_distribution_refs | financial/causal/actor/temporal rule | scenario_validation → E17 또는 E15; 재생성 예산 후 failed |
| E17 Simulation / SimulationResult[] | scenario_id, seed, samples, return_quantiles, class_counts, price_anchor, distribution_version | 동일 random draws, graph·quant structural map | simulation_runs → E18; 분포/price anchor 없음 부족 |
| E18 Probability & Calibration / ForecastCandidate + Contribution[] | horizon, target, probabilities, confidence, range, ledger, calibration_status | §3 알고리즘, 버전 고정 calibrator | forecast_candidate → E19; normalization/hash/finite 오류 failed |
| E19 Meta / MetaCheck + Explanation + ErrorDiagnosis | publishable, failed_checks, offending_engines, driver_refs, falsifiers, error_class | 모든 artifact·ledger·coverage·history cap·bias 검증 | meta_checks → publish 또는 offending engine; 예산 초과 failed |

E19 사후 오류 분류는 동일 모듈의 별도 review 모드다. 예측 시점에는 아직 생기지 않은 actual outcome을 읽지 않는다. mode가 달라도 기존 Forecast/MetaCheck를 덮어쓰지 않는다.

## 2. 정량 해석과 인과 계산

### 2.1 Signal과 품질

Factor registry는 `transform=level|diff|pct_change|log_return|yoy|ratio`, 비교 period, unit, 경제적 sign/경로, warmup를 가진다. 0으로 나눌 수 있는 percentage 변화는 허용하지 않고 기준값 부족으로 반환한다.

초기 정규화는 과거 rolling median/MAD를 사용한다. `z=clip((x−median)/(1.4826×MAD),−3,3)/3`. MAD=0이면 normalized unknown이다. Macro/market은 과거 252 daily 표본, 월간은 36개, 분기는 12개를 목표로 하며 최소 표본은 각각 60/12/8이다. 부족하면 confidence와 coverage에서 제외하고 percentile을 만들어내지 않는다. series index/YoY처럼 transform된 값도 unit 및 비교기간을 보존한다.

Evidence quality는 `q=authority × freshness × completeness × agreement`. 초기 authority는 official 1.0, licensed vendor .9, attributed secondary .6, rumor .3이다. 실제 공급자 검증 후 source version에서 조정한다. freshness는 registry SLA 안에서 1, SLA 초과 뒤 반감기=SLA로 감소하고 3×SLA 초과는 stale exclusion이다. 완전한 필수 값이면 completeness=1, 핵심 필드 부족이면 0이다. 수치 충돌 허용범위는 registry/source 단위로 정의하며 범위를 넘는 같은 시점 source는 agreement≤.5로 감액한다. 충돌의 양방향 evidence를 모두 보존한다.

Module score는 측정된 Factor의 경제적 방향 정렬값 `d_i*z_i`를 이용한다. `score=100×Σ(w_i q_i d_i z_i)/Σ(w_i q_i)`; 기본 w_i는 Module 안에서 동일하지만 weight_version으로 고정한다. coverage=관측된 required weight/전체 required weight. confidence=`coverage × weighted_mean(q_i) × (1−contradiction_ratio)`. w_i 재정규화만으로 누락을 감추지 않는다. score 절댓값≤10이면 neutral, 부호에 따라 positive/negative다. coverage<.5 또는 critical Factor 누락이면 direction=unknown, score=null. neutral은 실제로 측정된 균형 상태에만 사용한다.

### 2.2 Surprise와 priced-in

Surprise scale은 발표 당시 이용 가능 consensus 표준편차 또는 과거 surprise의 robust scale을 사용한다. 둘 다 없으면 actual−expected 원 단위만 보존하고 normalized surprise는 unknown이다.

Priced-in fraction은 `clip(abs(pre_event_abnormal_move)/abs(expected_response),0,1)`를 동일 방향 움직임일 때만 계산한다. 반대 방향은 0으로 인정할 근거가 있는 경우에만 0, response mapping 미정은 unknown이다. `residual=surprise×(1−priced_in)`. pre-event window와 benchmark는 model version으로 고정한다. Fixture 기본 window는 이벤트 이전 5개 거래 세션, 기준은 semiconductor index return이며 해당 자료가 없으면 priced-in 성공을 주장하지 않는다.

### 2.3 Graph·interaction·time

경로 부호는 edge sign의 곱, strength/confidence는 각각 edge 값의 곱이다. 동일 graph version과 valid interval, regime applicability를 만족하는 경로만 남긴다. visited node 집합으로 cycle을 차단한다. reflexivity는 E10의 명시된 제한 step으로 처리하고 무한 graph cycle로 구현하지 않는다.

같은 root_evidence_group의 같은 종착점 효과는 독립 증거가 아니다. 동일 방향은 절댓값이 가장 큰 경로를 대표로, 반대 방향은 signed sum을 대표 최대 절댓값 범위로 clip한다. 서로 다른 root는 합산하되 endpoint effect는 [-1,1]로 포화한다. 어떤 경로를 제외/감액했는지 ledger adjustment로 남긴다.

`H=target_at−cutoff`, `L=sum(edge lag)`. H≤L이면 해당 horizon 효과는 0. H>L이면 `active_fraction=min(1,(H−L)/duration)`이고 decay는 해당 충격 age의 반감기로 적용한다. duration/lag/반감기 미명세는 unknown이며 0 lag로 추정하지 않는다. 분기/연간 supply expansion을 발표 다음날 실물 공급으로 반영하지 않는다.

E10의 actor 반응은 profile의 허용 action/latency/capacity constraint를 따른다. max 2 step feedback을 기본으로 하며 누적 효과 크기를 초기 외생 충격의 1.5배로 제한하는 실험 규칙을 둔다. 이는 market technical batch 재실행 횟수와 별개다.

## 3. 확률·가격구간·기여도

### 3.1 표본과 prior

각 Horizon의 class는 동일 security의 total-return 기준으로 정한다. 초기 flat band는 1d .005, 1w .015, 1m .03, 3m .05, 1y .10이다. `r>band` up, `r<−band` down, 나머지 flat. 현금배당·분할 조정 version과 target calendar를 저장한다. price range는 가격수익률로 별도 계산해 배당을 주가에 더하는 오류를 피한다.

Prior는 cutoff 이전 성숙한 Horizon 표본의 empirical class frequency에 Laplace pseudocount 1을 적용한다. 최소 100개 표본을 초기 요구치로 하고 겹치는 horizon 표본의 유효 표본수도 보고한다. 충분하지 않으면 live Forecast prior unavailable로 반환한다. 고정 fixture prior는 `mode=fixture`에서만 허용하며 실제 forecast로 승격하지 않는다.

### 3.2 설명 가능한 log-odds 모델

클래스 순서는 [up,down,flat], `l0[k]=log(prior[k])`. 모듈 단순 합계와 graph propagation을 두 번 더하지 않는다. E06 state는 graph 충격의 입력이며 최종 evidence 효과는 E09/E12를 통과한 root별 `a_j∈[-1,1]`다.

초기 class vector는 `v_j=[a_j,−a_j,−abs(a_j)/2] × horizon_weight(module_j)`. class별 무게도 model_version에 기록한다. 각 vector를 canonical order `(module_id,root_id,path_id)`로 logit에 더하고 softmax를 계산한다. 순서에 따른 waterfall attribution 차이가 있으므로 순서를 저장하고 인과적 기여의 유일한 정답이라고 표현하지 않는다.

| Module | 1d | 1w | 1m | 3m | 1y |
|---|---:|---:|---:|---:|---:|
| macro | .20 | .20 | .15 | .10 | .10 |
| ai_demand | .03 | .05 | .12 | .15 | .15 |
| memory | .05 | .08 | .15 | .15 | .15 |
| supply | .02 | .03 | .08 | .12 | .15 |
| earnings | .05 | .08 | .15 | .18 | .18 |
| capital_flow | .25 | .20 | .10 | .06 | .03 |
| valuation | .05 | .08 | .10 | .12 | .12 |
| preferred | .10 | .10 | .08 | .07 | .07 |
| market_regime | .25 | .18 | .07 | .05 | .05 |

각 열의 합계는 1이다. 수치는 초기 실험값이며 Golden 기대값에 맞추려고 사후에 조용히 변경하지 않는다.

Scenario simulation에서 class 빈도를 얻는다. 인과 근거를 재가산하지 않고 동일 인과 상태의 예측 분포로 융합한다. 초기 산식은 `l := (1−alpha)×l + alpha×log(p_sim)`, alpha=.25이며 p_sim에 Laplace smoothing을 적용한다. alpha도 model_version에 고정한다. prior, causal, scenario fusion 단계마다 확률 vector의 before/after를 ledger에 남긴다.

History는 regime 일치, 유사도≥.8, 성숙 case≥20을 gate로 한다. cosine similarity 입력은 고정 정규화 특징과 missing mask이며 검색 사례의 source/availability를 검증한다. relevance는 similarity×recency×sample_factor, recency 반감기는 365일, sample_factor=min(n/100,1)이다. history에 의한 확률 변화의 L1 크기를 .10 이하, 각 class 절대차를 .05 이하로 제한한다. current evidence가 neutral/부족이면 history만으로 강한 방향을 만들지 않는다.

Challenger는 반증 confidence에 따라 해당 causal effect를 축소·제외하고 재계산한다. 근거 없는 일률적인 down penalty를 더하지 않는다. 적용 순서는 causal→scenario→challenge→history→calibration이며 모든 단계를 기록한다.

Calibration은 고정 temperature `softmax(log(p)/T)`로 시작하며 T는 cutoff 이전의 독립 calibration split으로 학습한다. 성숙 표본 100개 이상 및 각 class 20개 이상을 초기 fit 조건으로 하고 부족하면 identity T=1과 `calibration_status=unvalidated`를 사용한다. 미검증 출력은 research_only다. 이후 T 변경은 새 calibration version이며 기존 결과를 보존한다.

History의 최종 출력 영향도 제한하기 위해 history 없는 shadow를 동일 calibrator로 처리한다. 최종 차이가 class별 .05/L1 .10을 초과하면 제약 안으로 축소하고 `history_cap` ledger를 추가한다. history만으로 policy eligibility가 바뀌지 않도록 Decision은 `without_history_probabilities`에서도 up/down gate 충족을 요구한다. 이는 canonical anti-overfit을 구체화하는 추가 정책이며 Forecast 생성은 threshold를 참조하지 않는다.

### 3.3 Confidence와 설명

Model confidence는 coverage, source agreement, graph confidence, simulation validity를 반영하며 critical missing이면 Forecast를 발행하지 않는다. 초기에는 Horizon 가중 Module confidence×mean(active edge confidence)×(1−fatal_conflict_fraction)을 사용하고, confidence와 calibration 정확도를 구분한다. rumor-only는 최대 .49, 필수 memory 데이터가 없는 중기 예측은 insufficient_evidence다. 과거 유사 사례의 수만으로 confidence를 올리지 않는다.

`Contribution = {sequence,stage,engine_id,root_ids,edge_ids,version,before[3],after[3],delta_pp[3]}`. `delta_pp=100×(after−before)`이며 각 행 vector 합계는 0이다. `prior + Σ(delta_pp/100)=final`을 1e-9 오차로 검증한다. calibration/history cap도 행으로 기록하고 UI 반올림 잔차는 표시 전용 행으로 명시한다. Top driver는 ledger의 up/down 성분과 근거 refs를 표시한다.

What Would Change My Mind는 `{factor_id,operator,threshold,unit,valid_horizon,evidence_refs}` 구조의 반증 조건이다. LLM이 검증 불가능한 모호한 문장만 생성하면 게시하지 않는다.

### 3.4 Simulation과 가격구간

각 scenario는 검증된 shock distribution, 양의 정부호 covariance, 가격 변환 계수 version을 갖는다. 10,000 draws와 저장 seed로 실행한다. covariance 부재 시 독립을 가정한다면 fixture/research 가정으로 명시하고 live 성공 조건에서 제외한다.

가격 추정은 anchor_price×exp(simulated_price_log_return), 구간은 q10–q90이다. total-return class와 price-return의 배당 차이를 분리한다. 가격 변환 계수가 미학습/미정의라면 price range unknown으로 Forecast 필수 조건을 충족하지 못한다. up 확률만으로 상하 가격을 산출하지 않는다.

Baseline/user scenario는 같은 random draws로 비교한다. 회계·공급·actor·시간 제약을 위반한 draw/분포를 제외하고 reject 비율>.20이면 scenario_invalid로 재생성한다. .20도 실험 version 설정이다.

## 4. 부족·검증·재현

같은 input manifest·graph·model·저장된 LLM artifact·seed의 quant replay는 1e-9 허용오차로 일치시킨다. LLM 재호출은 별도 Run이며 완전 일치를 보장하지 않는다. replay는 외부 네트워크 없이 저장 artifact를 사용한다.

E19는 schema, cutoff, graph manifest, dependency generation, ledger, history cap, finite values, confidence provenance, critical missing, feedback_checked를 검증한다. 실패한 후보를 최신 Forecast로 반환하지 않는다. probability를 threshold로 끌어올려 검증을 통과시키는 행위는 금지한다.

## 5. Price Wave·Alignment·Liquidity

### 5.1 미래 정보를 사용하지 않는 특징 계산

완료 bar와 당시 알려진 corporate action 조정만 사용한다. RSI14는 Wilder smoothing, trend는 SMA20/60/120, ATR14, volume은 20bar 기준이다. SMA120과 pivot 탐색을 위해 최소 150개 완료 bar를 요구한다. 주봉/월봉 context 부족은 unknown이며 짧은 이력을 늘려 채우지 않는다.

Pivot low/high는 좌우 2bar 비교로 확정하며 오른쪽 2bar가 닫히기 전에는 사용하지 않는다. 최근 60bar 안에서 5–40bar 떨어진 두 pivot을 비교한다. Bottom은 두 번째 저점이 첫 저점−.5×ATR 이상이고 해당 RSI가 첫 저점의 RSI보다 3point 이상 높아야 한다. 두 저점 사이 최고 고가가 neckline이며 Top은 대칭 정의다. 동가 pivot은 먼저 발생한 시각으로 고정한다.

Bottom 특징은 RSI≤30에서 회복, double-bottom 형태, bullish divergence, 두 번째 저점 주변 3bar의 매도 volume이 첫 저점 대비≤.8, ATR 비율≤.9, neckline을 .1ATR 초과한 2bar 종가 상향 돌파, SMA20/60/120 회복이다. Top은 RSI≥70에서 하락, lower high, bearish divergence, 매수 volume 감소, ATR 비율≥1.1, neckline/SMA 하향 이탈을 사용한다. 매도/매수 volume은 실제 체결 분류가 없으면 하락/상승 bar volume proxy로 명시한다.

### 5.2 Score와 상태

초기 feature weight는 geometry .20, RSI divergence .15, extreme recovery .10, volume .10, volatility .10, neckline .20, trend .15다. trend는 세 SMA 중 회복 비율이다. Score는 측정된 성립 weight의 합계이며 누락 weight를 재정규화하지 않는다. 필수 feature가 unknown이면 score=null이다.

상태는 none→first_pivot→second_pivot→divergence→breakout_pending→confirmed다. Score≥threshold 외에 geometry/divergence/2bar neckline confirmation/세 SMA 중 2개 이상 회복을 필수로 한다. neckline 실패는 invalidated다. score는 보정 전 timing_score로 `probability=null, calibration_status=unvalidated`를 함께 반환한다. 연구 Decision gate는 score를 사용하고 운영 eligibility는 보정된 timing 모델을 요구한다. 보정 label은 해당 Horizon 안에서 목표 방향 1ATR 도달이 반대 방향 1ATR 도달보다 먼저인 경우로 정의하고, 양쪽 모두 미도달은 미확정으로 분리한다. 이 초기 정의도 timing-model version에 고정한다.

### 5.3 Timeframe alignment

방향마다 primary_confirmed와 higher_context를 계산한다. higher_context는 SMA20/60/120 방향 일치율, SMA20의 5bar 기울기, 확정 pivot의 higher-low/lower-high로 판단한다. strong bullish는 가격>SMA20>SMA60>SMA120이며 SMA20 기울기가 양수인 경우, strong bearish는 대칭이다. aligned/transition/opposed/unknown enum을 갖는다.

초기 alignment score는 primary confirmation .4 + higher trend agreement .4 + higher pivot agreement .2다. unknown이 있으면 score=null, 상위 강한 반대 추세면 최대 .69로 제한한다. 근거 bar ID를 기록하고 미완성 상위 bar를 사용하지 않는다.

### 5.4 Liquidity

동일 cutoff까지의 foreign/institution/program net buy, volume expansion, semiconductor relative flow를 사용한다. 방향별 support는 buy면 flow>0, sell이면<0이며 과거 20bar/일의 MAD 기반 noise scale을 초과해야 한다. volume expansion은 과거 20개 평균 대비≥1.2이고 가격 확인 방향이 같을 때 support다. 다섯 항목에 각각 .2를 부여한 합계를 초기 score로 한다.

foreign와 volume은 필수이며 나머지 세 항목 중 둘 이상이 관측되어야 한다. 미관측 weight는 0으로 두고 coverage를 별기하며 재정규화하지 않는다. program 거래가 foreign/institution에 포함되면 overlap metadata를 기록하고 자금량을 합산하지 않는다. 일별 flow만 있다면 당일 장중 flow를 만들어내지 않고 cutoff까지 확정된 최신 일별 값의 freshness/cadence를 표시한다.

Bottom/Top volume feature와 liquidity는 각각 timing 구조와 자금 방향의 gate다. 같은 volume을 Forecast에 두 번 더하지 않으며 E09가 root observation refs로 중복 제거한다.

## 6. 구현 전 추가 검증 사례

- EC01: E02의 존재하지 않는 Factor ID를 schema/ontology 검증에서 거절한다.
- EC02: E04의 expected_response=0이면 fraction을 계산하지 않는다.
- EC03: 같은 foreign observation이 E01과 feedback에 있어도 한 번만 반영한다.
- EC04: E19 retry 후 과거 E18 generation을 발행하지 않는다.
- EC05: history가 .79→.82로 올려도 without_history gate 미달이면 ENTRY 불가다.
- EC06: calibration이 history 차이를 확대해도 최종 cap을 유지한다.
- EC07: pivot 오른쪽 bar가 cutoff 이후라면 bottom 확인에 사용하지 않는다.
- EC08: score가 높아도 neckline 미확정이면 WAIT/HOLD다.
- EC09: policy만 변경해도 Forecast vector는 불변이다.
- EC10: transaction 응답 소실 후 재송신해도 Journal은 한 건이다.
- EC11: 월봉 warmup 부족이면 장기 alignment는 unknown이다.
- EC12: 같은 seed의 baseline/scenario 비교에는 같은 draws를 사용한다.
- EC13: price distribution 없이 up/down 확률로 price range를 만들지 않는다.
- EC14: source conflict가 confidence를 올리지 않는다.
- EC15: neutral과 unknown은 표시·schema·Decision reason이 다르다.

위 항목은 테스트 명세이며 아직 구현하거나 실행하지 않았다.
