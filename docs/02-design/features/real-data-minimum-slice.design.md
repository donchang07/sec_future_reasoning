# Design: real-data-minimum-slice

2026-09-09 · [Plan](../../01-plan/features/real-data-minimum-slice.plan.md) · 구현 전 Source Architecture

## 1. 확인한 Source와 우선순위

2026-09-09 직접 HTTP probe 결과다. 연결 성공은 source 응답 성공이며 production SLA나 독립 교차 검증을 의미하지 않는다. 6개는 instrument/series feed 기준이고 독립 Provider는 Treasury와 Yahoo의 2개다.

| Series | 우선 Provider / 현재 가능한 Provider | 형식·확보 범위 | timezone·단위 | authority·revision | freshness / missing |
|---|---|---|---|---|---|
| 005935 삼성전자우 | KRX/KIS 권한 API / Yahoo chart | JSON 30m 264행, daily 20y 4,936행 확인 | Asia/Seoul; KRW/share, volume shares | 거래소/공식 broker 우선; 현재 vendor fallback, 수정 가능 | 30m 최근 완료봉 2시간(장중), daily 4 calendar days; 부족하면 unavailable |
| 005930 삼성전자 | KRX/KIS / Yahoo chart | daily JSON 응답 확인, 20y 요청 | Asia/Seoul; KRW/share, shares | 동일 | daily 4일; 결측 보충 금지 |
| US10Y | US Treasury XML / Yahoo ^TNX 보조 | Treasury 2026 연간 XML 266,413 bytes 확인 | America/New_York; annual percent | Treasury primary official, 수정 가능 | 7 calendar days; 다른 instrument인 ^TNX로 무음 대체 금지 |
| USD/KRW | BOK ECOS / Yahoo KRW=X | Yahoo daily 263행 확인; ECOS key 미확보 | provider metadata timezone; KRW/USD | 공식 fixing과 vendor quote 정의가 다름; vendor quote 명시 | 4일; fixing과 quote 충돌 비교 금지 |
| KOSPI | KRX / Yahoo ^KS11 | daily JSON 응답 확인 | Asia/Seoul; index points | vendor fallback, 수정 가능 | 4일; missing |
| DXY | ICE 허가 feed / Yahoo DX-Y.NYB | daily JSON 응답 확인 | America/New_York; index points | vendor fallback, 수정 가능 | 4일; missing |
| 외국인·기관·프로그램 수급 | KRX/KIS 공식 API | 인증키 없음, 확보 못함 | Asia/Seoul; KRW million, 투자자/시장 범위 명시 필수 | unavailable | 대체·0 삽입 금지, liquidity unknown |
| DRAM/Memory 가격 | 라이선스 원자료 / BOK 세부 가격지수 검증 후보 | 신뢰 가능한 machine-readable series 및 이용권한 미확보 | series 확정 전 단위 미확정 | unavailable | 광범위 반도체 ETF/PPI를 DRAM이라고 재명명하지 않음 |

Yahoo endpoint: `https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={range}&interval={interval}`. 공식 지원 API/SLA가 없는 machine-readable fallback으로 분리한다. HTML scraping은 adapter에 없다. 응답 실패 시 status를 기록하며 우회 인증·개인 계정 탐색을 하지 않는다. 공식 KIS는 [공식 저장소](https://github.com/koreainvestment/open-trading-api), Treasury 형식은 [공식 XML 문서](https://home.treasury.gov/treasury-daily-interest-rate-xml-feed), Yahoo 공급자 정보는 [공식 도움말](https://help.yahoo.com/kb/SLN2310.html)을 참조한다.

priority는 official_original > official_distributor > licensed_vendor > public_vendor_fallback이다. 동일 factor/단위/관측시각/시장 범위에서만 비교한다. priority가 높더라도 차이가 허용오차를 넘으면 conflict를 보존하고 해당 관측을 reasoning에서 제외한다. 공식 값과 vendor 추정값을 평균하지 않는다. revision은 collected/available 순서를 사용하며 같은 effective time의 다른 값은 conflict다.

## 2. 시각·원본·모드

RawResponse: source_id, provider, instrument, URL(비밀값 없음), requested_at, collected_at, status, HTTP status, response bytes SHA256, body, error, authority, timezone, unit, revision policy. 먼저 모든 원본 응답을 저장하고 그 뒤 UTC prediction_timestamp와 data_cutoff를 고정한다. cutoff는 모든 채택한 응답의 수집 완료 이후이며 예측 실행 시작 이전이다.

Observation 1.1: 기존 observed_at/published_at/available_at에 data_mode와 nullable released_at/collected_at/effective_at, 원본 ref를 추가한다. `released_at=null`은 공개 시각을 모른다는 뜻이다. 이때 published_at/available_at은 보수적으로 collected_at이며 과거 날짜로 소급하지 않는다. 원본에는 date-only인지 intraday timestamp인지 precision을 별도 기록한다. effective_at은 가격봉 종료 또는 source 기간 종료이며 collected_at과 다르다.

세 mode는 synthetic_fixture/historical_replay/live_forward. 기존 fixture는 명시적 synthetic_fixture default로 migration한다. 실제 관측은 모두 live_forward이며 batch/journal/observation mode 불일치를 거절한다. 과거 시장 관측을 현재 수집하여 오늘 forward 예측에 쓰는 것은 live_forward이다. 동일 raw를 재현하는 replay는 원래 prediction mode/cutoff를 그대로 보존한다. 새 과거 예측을 생성하는 historical_replay와 구분한다.

새 schema가 추가된 기존 sealed 파일은 원래 파일을 수정하지 않는다. legacy 원본 hash 검증을 우선하는 read 경로 또는 별도 migration을 제공하고, 새 Journal과 이전 schema hash를 혼동하지 않는다. 이전 89개 fixture 테스트와 확률 oracle은 유지한다.

## 3. Bar와 aggregation

30m epoch는 봉 시작 시각으로 해석하고 end=start+30m를 사용한다. 마지막 실시간 quote처럼 정규 grid가 아닌 항목은 제외한다. Asia/Seoul 정규장 09:00–15:30 내의 완성된 30분봉만 사용한다. provider delay를 고려하여 end+20분≤cutoff인 봉을 채택한다. 현재 진행 중인 봉은 raw에는 보존하되 Wave에 넣지 않는다.

daily의 원본 timestamp가 장 시작이어도 실제 관측 effective_at은 해당 세션 종료 15:30 KST다. cutoff가 종료+20분 이전이면 그날 daily는 intraday_partial로 제외한다. daily raw OHLCV에서 ISO week/month로 first open, max high, min low, last close, sum volume을 계산한다. 현재 주/월은 제외한다. 주봉은 금요일 세션 종료, 월봉은 달력 월말까지 기간이 완료되어야 채택한다. 최초 bucket의 partial 기간도 제외한다. 주식 split/adjustment metadata를 보존하고 Yahoo adjclose를 raw OHLC와 혼합하지 않는다.

Wave/Alignment 알고리즘은 그대로이며 150개보다 적으면 available=false. 20년 daily로 weekly/monthly warmup을 확보한다. primary 1w=30m, 1m=daily, 1y=weekly와 각각 상위 daily/weekly/monthly를 사용한다. provider calendar 대신 weekday 기반 검증을 사용하는 제한은 명시하고 휴장일 가격을 생성하지 않는다.

## 4. 기존 엔진을 보존하는 실행 경계

`reasoning/engines.py`, `technical.py`, `decision.py`의 수치 계산과 weights/threshold는 고정하고 hash를 회귀 검사한다. synthetic input 파일은 live 코드가 읽지 않는다. 기존 FactorSpec baseline/scale/sign/critical과 graph는 독립 model-profile JSON으로 분리한다. 이는 모델 설정이며 관측값이 아니다. 기존 model metadata 밖 Factor(KOSPI/DXY)는 원본/context로 저장하되 첫 실행에서 임의 edge를 만들어 방향 계산에 추가하지 않는다. 연결된 feed 수와 실제 모델에 투입된 Factor 수를 따로 보고한다.

현재 모델에서 실제 관측을 연결할 수 있는 것은 preferred/common price, US10Y, USDKRW다. 기술 지표는 실제 OHLCV에서 계산한다. 나머지 예상 Factor는 observation을 만들지 않아 기존 E01/E05/E06 경로의 missing·coverage penalty가 유지된다. DRAM critical을 optional로 낮추지 않는다.

E11에 필요한 capacity/production/revenue/cash identity가 없으면 실행 경계에서 명시적 non-applicable ConstraintIdentity를 생성하고 unavailable 진단을 기록한다. missing guard만 추가하며 정상 계산을 통과했다고 기록하지 않는다. E18은 기존 critical-missing 규칙대로 insufficient_evidence를 반환하고 E19는 nonpublishable이다. 따라서 현재 확보 범위에서 **숫자 Horizon 확률 생성이라는 완료조건은 막혀 있다**. 이것을 해결하려고 모델·critical set·threshold를 바꾸지 않는다. 19 engine 경로의 실행/진단과 전체 자료를 최초 forward evidence로 보존한다.

## 5. Journal·설명·Outcome

LiveJournal은 data_mode, prediction_timestamp, cutoff, source manifest/raw hashes, missing/conflict, source age/freshness, 기존 114 execution, 3 Horizon 결과, availability 진단, model-profile/core-code hash를 포함한다. 없는 확률은 null/insufficient_evidence이며 prior를 final로 복사하지 않는다. reversal에는 기존 bottom/top score와 `calibration_status=unvalidated`를 표시하고 calibrated probability를 발명하지 않는다.

설명서는 source별 상태, 전후 probability와 delta(있을 때만), 원장 단계 before/after/%p, E09 interaction 제거, E13 history, calibration, 최대 positive/negative 5개 경로, timing feature, pass/fail gate, What Would Change My Mind를 출력한다. missing으로 E18이 중단되면 숫자 재구성 불가능한 이유와 누락 upstream을 보여준다. 경로가 5개보다 적으면 있는 것만 표시한다.

Outcome은 별도 immutable 객체로 journal_sha256/run_id, due_at(+1d/+7d/+1calendar month), observed_at, collected_at, raw source ref, 실제 가격/수익률을 저장한다. due 이전 연결·미래 가격·다른 mode를 거절한다. 예측 파일을 업데이트하지 않는다. 이번 단계에서는 미래 가격을 수집한 척하지 않고 pending schedule만 생성한다.

## 6. 구현 및 테스트

모듈: `reasoning/market_data.py`(source contracts/adapters/normalization), `reasoning/live.py`(availability execution/journal/report/replay/outcome), `config/live-model-profile.json`(기존 모델 metadata), CLI live-run/replay-live/verify-live/attach-outcome. 원본/Journal은 `artifacts/local/live/{snapshot_id}/`에 exclusive create. CI는 네트워크 없이 저장된 테스트용 JSON/XML response를 parser에 주입하며 테스트용 데이터가 live_forward 산출물로 게시되지 않도록 한다.

선행 검사 11종: source unavailable, stale, conflict, market timezone, cutoff, revision, look-ahead, missing30m, intraday/close 구분, live journal immutability, same raw replay. mode 혼합/unknown release/aggregate partial/outcome future 및 기존 fixture hash·engine source hash도 검사한다.

Plan/Design 완료 후 본 문서의 Source 범위를 사용자에게 보고하고 구현한다. Check는 6 feeds/3 Wave/19 execution/feedback/numeric forecasts/report/sealed live/replay/89 regression 항목을 각각 판정한다. 숫자 확률·전체 19 정상 계산이 외부 근거 부족으로 막히면 해당 완료조건을 미충족으로 남기고 Act는 외부 소스 확보 의존성을 명시한다.
