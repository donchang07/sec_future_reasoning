# 실행 가능한 삼성전자우 fixture vertical slice

2026-09-09 · PRD v1.1 · 모델 `slice-v1` (Python 소스 SHA256 포함)

기존 Foundation의 19개 payload, Artifact, EngineResult, Forecast, Contribution 계약을 그대로 사용한다. E01부터 E19까지 계산한 뒤 OHLCV 기술 근거를 만들고, Market Regime·Capital Flow·Actor/Reflexivity에 반영하여 한 번 재계산한다. 1주·1개월·1년 각각 38회, 총 114개 실행 결과를 하나의 Prediction Journal에 저장한다.

## 실행

저장소 루트, Python 3.11 또는 3.12:

```powershell
python -m pip install -r requirements.lock
python -m pytest -q
python -m reasoning validate
python -m reasoning run-fixture --fixture fixtures/samsung-preferred-v1.json --output artifacts/local/prediction-journal.json
python -m reasoning verify-journal --journal artifacts/local/prediction-journal.json --replay
python -m reasoning inspect-journal --journal artifacts/local/prediction-journal.json --horizon 1w --engine E18 --generation 1
```

Windows 가상환경에서는 `python` 대신 `.\.venv\Scripts\python.exe`를 사용한다. `inspect-journal`의 engine/horizon/generation 필터를 생략하면 해당 범위 전체를 출력한다. E18 payload의 `forecast.ledger`가 확률 변화 원장이다. E08은 인과 경로, E09는 중복 제거 전후 효과, E12는 기간별 효과, E19는 발행 검증 결과다.

Journal은 exclusive create로 저장한다. 기존 파일과 내용이 같으면 재실행을 허용하고, 다르면 덮어쓰기를 거절한다. 코드나 fixture가 변경되었다면 새 출력 경로를 사용한다. `--replay`는 저장된 전체 fixture로 계산을 다시 실행하여 Journal 전체를 비교한다. 원래 소스·버전으로 실행해야 하며, 버전 변경에 따른 차이를 성공으로 덮지 않는다.

## 입력과 재현성

`fixtures/samsung-preferred-v1.json`은 합성 연구 데이터다. 미국 10년물, 원/달러, DRAM, HBM, AI CAPEX/수요, 생산능력, EPS, 외국인·기관·프로그램·업종 수급, 보통주/우선주 가격, 밸류에이션, 기술 지표를 포함하는 20개 Factor와 80개 관측이다. 전체 49개 registry 중 fixture 범위에 해당하는 Factor만 사용한다.

30분·일·주·월 OHLCV 각 160개, pre-event consensus와 제한 문법 원문 이벤트, 회계 identity 입력, 성숙된 합성 유사 사례, 29개 DAG edge가 포함된다. 실시간 외부 연결이나 실제 과거 성과를 주장하지 않는다. `scripts/build_slice_fixture.py`는 원시 입력만 생성하며 기대 확률·정답 결정은 저장하지 않는다.

모델 소스 SHA256, graph 내용 SHA256, ontology/model/prompt/calibration/policy/source/calendar/19 engine version, 마지막 reasoning 코드 commit을 pin한다. UUID5, cutoff 기준 시각, 고정 simulation seed를 사용하며 wall clock은 결과에 들어가지 않는다. 동일 입력·코드·버전·실행 환경에서 Journal은 byte-identical이다. 서로 다른 OS/Python의 부동소수점 결과까지 같은 hash라고 가정하지 않는다.

## 계산 경로

| Engine | 실행 계산 |
|---|---|
| E01 | cutoff/revision 선택, 이력 변화·가속·분위·정규화, source 불일치·기간 부족에 따른 품질 감점 |
| E02 | `type actor factor actual unit` 원문 파싱, entity/unit 검증, 원문 span |
| E03 | 사전 consensus 평균·표준편차와 surprise; consensus 부족은 unknown |
| E04 | surprise와 같은 방향의 사전 움직임만 priced-in 처리, residual shock |
| E05 | signed economic evidence, positive/negative, conflict/missing, dominant theme |
| E06 | 9개 Module별 품질 가중 score·coverage·confidence 및 기술 feedback |
| E07 | 상승/하락/횡보 가설, 지지/반대 근거, 방향에 맞는 반증 조건 |
| E08 | DAG DFS, edge 부호·강도·신뢰도 곱, root가 연결된 causal path |
| E09 | root별 최대 절댓값 대표 경로, 중복 경로 효과 0 및 competing refs |
| E10 | flow/trend와 feedback에 따른 actor의 bounded response range |
| E11 | 생산≤capacity, 매출=수량×가격, FCF=영업현금−CAPEX 검증 |
| E12 | 기존 설계 Horizon weight, lag maturation, decay를 적용한 경로 효과 |
| E13 | mature case cosine similarity≥.8, regime/coverage/recency gate, 표본수 감점 |
| E14 | 반대 경로 강도·품질·consensus 결측·제약 위반에 따른 challenge/confidence |
| E15 | causal/actor/challenge 기반 base/up/down/tail 분포와 가중치 |
| E16 | 시나리오 가중치·분포·단위·가설 참조·회계 제약 검증 |
| E17 | 고정 seed Gaussian 2,048회/시나리오, class count와 q10/q50/q90 |
| E18 | causal→actor→simulation→challenge→history→temperature 확률 원장 |
| E19 | Forecast 재검증, missing/constraint/scenario/history cap/driver 검증 |

E18의 prior는 [.4,.35,.25], causal logit 변화는 3×effect×[1,−1,−.5×sign(effect)], simulation log-probability 가중치는 .20, temperature는 1.15이다. 매 변화마다 before/after와 %p delta를 남긴다. prior에 delta/100을 순서대로 더하면 최종 확률이 복원된다. history 없는 shadow도 동일한 calibrator를 거치며, 최종 history 영향은 class별 .05 및 L1 .10 이내다. 이 수치는 사전 설계의 연구 가정이며 case ID를 읽거나 정답별 분기를 두지 않는다.

## Timing과 Decision

단기 30분+일, 중기 일+주, 장기 주+월이다. Wilder RSI14·ATR14, SMA20/60/120, 좌우 2봉 확인 pivot으로 double bottom/top, RSI divergence, neckline 2봉 돌파, 이동평균 회복/이탈, pivot 거래량 수축·현재 거래량 확장을 계산한다. 점수와 개별 boolean feature, neckline, pivot index를 모두 보존한다. 충분한 bar가 없으면 `available=false`이고 alignment는 null이다.

ENTRY는 up≥.80, confidence≥.70, bottom confirmed 및 score≥.75, bullish alignment≥.70, buy liquidity≥.60, E19 통과를 모두 요구한다. SELL은 보유 상태에서 down≥.70, confidence≥.65, top confirmed 및 score≥.65, bearish alignment≥.70, sell liquidity≥.60을 모두 요구한다. history 없는 확률도 같은 방향 threshold를 넘어야 한다. 미확인 gate는 미보유 WAIT/보유 HOLD로 처리한다.

기술 feedback은 generation=1에서 Regime/Flow 해석과 Actor response에만 들어간다. E01 원시 관측은 그대로이며 확률을 다시 기술 입력으로 넣는 반복 루프는 없다. 기술신호 단독 ENTRY/SELL은 금지된다. 모든 결정은 `research_only=true`, calibration은 `unvalidated`다.

## 검증 범위와 후속 작업

`tests/test_vertical_slice.py`의 core 15개: all-positive, all-negative, hawkish FOMC, priced-in, missing, conflicting source, duplicate root, horizon divergence, false/true bottom, low confidence, ENTRY 79/80, SELL 69/70. 별도 테스트에서 모든 엔진의 실제 산출물, true top, feedback 횟수/대상, 제약 위반, Journal 재현·변조·불변성을 확인한다.

CK-01은 잘못된 metadata로 release 통과하던 경로를 typed evidence 검증 및 fail-closed로 막았다. 원래 80개 oracle 전부가 실행 가능해질 때까지 product release gate는 계속 false다. CK-02는 MetaCheck applicability/driver/evidence, CK-03은 같은 시각 revision 충돌, CK-04는 명시적 49 Factor transform/window와 ontology-design-v2로 수정했다. 이미 YoY인 지표를 다시 YoY 처리하지 않도록 level과 diff도 구분했다.

Foundation+slice 테스트 수를 원래 Golden 80개 통과 수로 해석하면 안 된다. 실데이터 adapter, 운영 calibration/backtest, 전체 registry 데이터 연결, DB/API/UI와 원래 80개 전체 oracle은 후속 범위다. GitHub Actions는 Python 3.11/3.12에서 테스트·fixture·전체 replay를 수행하고 각 실행의 Journal을 artifact로 업로드한다.
