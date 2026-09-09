# reasoning-vertical-slice — Design

> 2026-09-09 · v1.0 · fixture-model-v1 · Foundation payload 재사용

## 기준과 범위 변경

[Plan](../../01-plan/features/reasoning-vertical-slice.plan.md), [기존 통합 설계](sec-future-reasoning-v1-1.design.md)를 따른다. 최신 사용자 지시에 따라 실데이터·외부 LLM/Neo4j/Supabase를 요구하지 않고 고정 fixture와 로컬 graph, 규칙 기반 구조화 추론, 파일 Journal로 완결한다. 통합 설계의 학습된 분포·운영 calibration 요구는 이번 연구용 slice에서 고정 실험 파라미터로 대체하며 `unvalidated` 표시를 유지한다. 정책 숫자는 기존 v1.1을 유지한다.

## CK-01–04 수정 설계

- CK-01: Golden 실행 결과는 typed Result/VersionBundle, UUID, SHA256와 검증 assertion 목록으로 검증한다. release CLI는 fixture 파일 hash와 실행 증거 JSON hash를 확인하고 assertion actual/expected를 직접 평가한다. 임의 passed 플래그는 판정 기준이 아니다. 자료가 없는 기존 80개 카탈로그는 계속 fail-closed. 이 로컬 무결성 검사는 신뢰된 test runner를 대체하는 서명/인증 장치가 아니다.
- CK-02: publishable Meta는 applicable=true 및 driver_refs 필수, 실패 check 없음. EngineResult evidence 예외로 이를 우회할 수 없게 한다.
- CK-03: cutoff 이하 자료를 우선 timestamp별로 고르고, 가장 최신 시각의 동일 source 상충 revision은 RevisionConflict를 반환한다. UUID/문자열 revision 순서를 신뢰하지 않는다. 동률 동일 값·단위는 deterministic dedup 가능.
- CK-04: 49 Factor 각각 transform/window를 명시한 mapping으로 전환. EPS revision은 precomputed 30-day change, DRAM contract ASP는 monthly pct-change, yoy는 1year, level은 point-in-time. 생성 함수의 자체 결과 비교 외 독립 oracle를 추가한다. ontology version을 올린다.

## 입력과 계약

`Fixture`는 cutoff/seed, FactorSpec(baseline,scale,economic sign,module,critical,source quality), Observation 이력, raw event text 및 event 전 consensus/priced-in response, DAG edge 목록, actor/회계 facts, historical 사례, OHLCV의 30m/1d/1w/1mo, flow 5개 항목을 포함하는 frozen 타입이다. 봉은 cutoff 이전에 닫힌 오름차순이다. 모든 가격·volume은 finite·양수 검증, source 충돌은 quality 감액 및 conflict ID로 보존한다.

새 타입은 fixture/technical/실행기/journal 확장에만 사용한다. Engine 사이 output은 기존 DataInterpretation부터 MetaCheck까지 19 payload 및 Artifact/EngineResult를 그대로 사용한다. RunContext는 타입 있는 fixture와 해당 Horizon·generation·기술 Evidence를 보유한다. 결과를 계산할 때 upstream payload를 실제로 소비하며 case ID나 expected probability를 읽지 않는다.

## 19 Engine의 최소 실행 알고리즘

| Engine | 실제 수행할 처리 |
|---|---|
| E01 | cutoff/revision 선택, 4개 이상 이력의 level/change/velocity/acceleration/percentile, fixture baseline/scale 표준화, source 충돌 감액 |
| E02 | 제한 문법 raw event에서 type/actor/factor/actual/unit 추출, fixture ontology 참조·원문 span 검증 |
| E03 | event 이전 consensus와 (actual−expected)/dispersion 계산 |
| E04 | event 이전 관측 움직임/expected response로 priced-in 비율, residual shock 계산 |
| E05 | Signal 경제적 부호+residual shock으로 positive/negative·dominant theme·missing/conflict 구조화 |
| E06 | 품질 가중 Factor 집계, 9 Module score/direction/confidence/coverage, 기술 evidence로 Regime/Flow 갱신 |
| E07 | bull/bear/flat 가설을 support/contradiction과 threshold falsifier로 생성 |
| E08 | 버전 고정 DAG를 DFS 탐색, edge sign/strength/confidence 곱, cycle 방지, hypothesis/root 근거 연결 |
| E09 | root별 경로를 대표 최대 절댓값으로 제한, duplicate 효과 0, signed adjusted effect 기록 |
| E10 | 자금 actor의 flow/trend/technical 근거 반응을 bounded response range로 계산 |
| E11 | capacity·매출 identity·cash identity 검사; violation 이후 발행 차단 |
| E12 | lag/horizon 성숙도, Module별 Horizon weight, 영향 decay 계산 |
| E13 | 현재 vector와 성숙 historical 사례 similarity·recency·regime gate, class delta cap |
| E14 | 가설 반대 근거의 강도·coverage·충돌을 평가하고 counterclaim/심각도·대체 가설 생성 |
| E15 | E12 effect/E10 response/E14 challenge에서 base/up/down/tail 평균·분산·weight 구성 |
| E16 | scenario weight/distribution/override/identity 모순 검사 |
| E17 | 고정 seed의 Gaussian draws로 가격수익 분포·quantile·up/down/flat count 계산 |
| E18 | prior→개별 causal vector→actor→scenario likelihood fusion→challenge→history cap→temperature calibration ledger 구성 |
| E19 | ledger 재구성·확률·cutoff·critical missing·constraint·시나리오·history 영향 검증, publishable/driver/falsifier/error 분류 |

최소 알고리즘은 fixture 연구용이다. 해당 없음도 E13의 similarity gate 등 실제 검사 후 진단으로 반환한다. 필수 근거가 부족하면 E18은 numeric Forecast를 만들지 않고 insufficient_evidence, E19는 발행 불가 MetaCheck를 생성한다. 정상 fixture에서는 모든 19 Engine이 nonempty typed 계산 결과를 생성한다.

## 수치·정책·설명

1w/1m/1y를 독립 실행한다. 정규화는 clip((latest−baseline)/scale,−1,1), fixture 모델에서 기준·scale을 공개한다. Horizon 가중치는 통합 설계 표를 사용한다. lag maturation=min(1,max(0,(days−lag_days)/duration_days)). cumulative logit effect의 strength는 모델 설정이며 사례별로 조정하지 않는다.

E18 prior=[.4,.35,.25], class vector=[x,−x,−abs(x)/2], causal gain=3을 초기 연구 가정으로 둔다. simulation은 [up,down,flat] frequency와 log-probability의 .20 혼합; history 최종 class당 .05 이하, L1 .10 이하; temperature=1.15. 바뀐 모든 확률 vector는 기존 Contribution before/after/delta_pp로 저장한다. 가격구간은 E17 q10–q90. history 제외 shadow도 같은 calibrator를 통과시킨다. 단위는 확률 [0,1], 표시 %p=100배다.

Decision은 독립 함수: ENTRY(up≥.80, bottom confirmed≥.75, alignment≥.70, liquidity≥.60, confidence≥.70, fatal 없음), SELL(down≥.70, top confirmed≥.65, bearish alignment≥.70, sell liquidity≥.60, confidence≥.65, held). history 제외 확률도 방향 gate 충족. 미보유 WAIT/보유 HOLD 기본. fixture unvalidated라도 연구용 candidate Action을 반환하고 `research_only=true`를 필수 표시한다.

## Wave·Alignment·Liquidity

완료된 OHLCV만 사용한다. RSI14 Wilder, SMA20/60/120, ATR14, pivot 좌우2봉 확인, 최근60봉 안의 두 저점/고점, neckline은 두 pivot 사이 극값이다. RSI divergence와 double-bottom/top을 별개 feature로 기록하고 neckline 2봉 돌파와 SMA 2개 이상 회복/이탈을 confirmed 필수로 한다. volume은 1/2 pivot 주변 3봉 비교 및 최근 volume/20봉평균, ATR contraction/expansion도 계산한다. reversal weight는 기존 .20/.15/.10/.10/.10/.20/.15를 따른다.

1w=30m+1d, 1m=1d+1w, 1y=1w+1mo. Alignment는 primary confirmation .4+higher SMA agreement .4+higher pivot agreement .2, 상위 강한 반대 추세는 .69 cap. Liquidity는 foreign/institution/program/sector directional flow와 volume direction 확인 각 .2. 필요한 bar/flow 결측이면 unknown이고 Action 차단.

## 실행과 Journal

1차 E01–E19 실행 뒤 Wave→Alignment→Liquidity를 계산한다. 각 Horizon별 TechnicalEvidence(batch_id,source bar/flow refs,signed regime/flow/reflexivity effect)를 생성한다. generation=1에 동일 input cutoff로 E01–E19를 한 번만 재실행한다. Regime/Flow는 E06, actor는 E10에 반영하고 해당 root의 추가 효과를 기록한다. 같은 raw flow의 수치 자체를 두 번 더하지 않는다. 확률을 다시 technical 입력으로 쓰지 않는다.

`RunJournal`은 root run_id/data_cutoff/VersionBundle/fixture hash/source hash, Horizon별 initial/final Forecast(없으면 null), positive/negative paths, timing/alignment/liquidity/Decision/explanation, 114개 Engine execution records와 typed Artifact를 담는다. id는 fixture+code hash+Horizon+generation에서 UUID5, 시각은 cutoff 기준으로 만들어 재실행이 byte-identical하다. 파일은 생성 전 전체 검증 후 exclusive create로 저장, 이미 존재하면 같은 bytes만 허용하고 다른 내용은 거절한다. sealed SHA256은 journal body 기준이며 검사 CLI로 재검증한다.

CLI: `python -m reasoning run-fixture --fixture fixtures/samsung-preferred-v1.json --output artifacts/local/prediction-journal.json`; `inspect-journal`은 horizon/engine/generation별 artifact 조회, `verify-journal`은 hash/ledger/연결 검사.

## 핵심 15개 oracle (선행 작성)

all-positive, all-negative, hawkish FOMC, priced-in event, missing critical data, conflicting source, double-count prevention, horizon divergence, false bottom, true bottom, low-confidence no-action, ENTRY79, ENTRY80, SELL69, SELL70. Direction 사례는 상대 확률/방향·confidence·근거를 검증하고 gate 경계는 독립 Decision 입력으로 고정한다. 추가 테스트는 true top, technical-only 금지, 114 execution/재현/Journal 변조/ledger 복원/feedback 한 번/중간artifact 참조를 검증한다.

이 core suite의 성공을 원래 80개 전체 성공으로 바꾸지 않는다. 실데이터 adapter/DB/UI의 미완료 상태도 유지한다.
