# Plan: real-data-minimum-slice

2026-09-09 · PRD v1.1 · 기존 기준 commit 5b159709d502448c0a43c60ffbb8471f06a8a2a1

## 목표와 범위

deterministic fixture와 89개 회귀 테스트를 보존하면서 실제 시장 데이터의 첫 live_forward 실행을 추가한다. E01–E19, Wave, Alignment, Liquidity, feedback 1회, Decision, immutable Journal 경로를 재사용한다. UI, Supabase, Neo4j 전체 구현, 49개 전체 연결은 제외한다. 시장 결과를 본 후 weight, calibration, ENTRY .80/SELL .70 threshold를 조정하지 않는다.

최초 원천 Factor 범위는 삼성전자우 OHLCV, 삼성전자 OHLCV, US10Y, USD/KRW, KOSPI, 외국인 수급, 기관 수급, 프로그램 수급, DRAM/검증된 memory price proxy, DXY까지 최대 10개다. unavailable 항목을 synthetic 값이나 타 경제개념으로 대체하지 않는다. 최소 6개 source는 서로 다른 instrument/series feed를 뜻하며 독립 Provider 수와 구분하여 보고한다.

## 요구사항

- R01: 공식 API/공개 machine-readable source 우선, provider/authority/단위/timezone/freshness/revision/missing/conflict 정책 명세.
- R02: 각 수집 응답을 immutable raw snapshot으로 저장. HTTP 실패도 source status로 기록. credential은 저장·출력하지 않는다.
- R03: 모든 Observation과 Journal에 synthetic_fixture/historical_replay/live_forward 구분. 실제 실행에 fixture 값 혼합 금지.
- R04: observed/released/collected/effective 시각과 known-at 증거를 구분. 공개 시각 불명은 null, 수집 시각보다 과거에 알려졌다고 가정하지 않는다.
- R05: cutoff 이후 공개·수집된 revision 배제. 같은 raw snapshot replay는 네트워크와 wall clock을 사용하지 않는다.
- R06: 실제 30분봉, 일봉 및 동일 일봉에서 생성한 주봉·월봉. 미완성 봉, 휴장, timezone, 결측을 구분.
- R07: 기존 엔진 수치 알고리즘 그대로 최초 실행. missing 상태는 E01 실행 기록부터 추적하고 신뢰도/중단 이유를 노출.
- R08: 3 Horizon 전후 확률·delta·경로·timing·alignment·liquidity·Decision·통과/실패 gate·반증 조건 보고.
- R09: 사람이 읽을 수 있는 contribution ledger와 positive/negative driver 최대 5개. 없는 driver를 만들어 개수를 채우지 않는다.
- R10: Journal 불변, 1일/1주/1개월 Outcome은 별도 append-only 객체로 run_id/hash 참조. 첫 예측을 과거 날짜로 소급하지 않는다.
- R11: 기존 89개 유지 및 unavailable/stale/conflict/timezone/cutoff/revision/look-ahead/30m missing/intraday-vs-close/immutability/replay 검사.

## 완료조건

사용자 지정 조건을 그대로 평가한다: 최소 6개 실제 series 연결, 실제 preferred 30m/daily/weekly Wave 실행, 19개 engine 경로, feedback 재실행 1회, Horizon별 확률·Decision, explainability, 첫 live_forward immutable Journal, raw replay 일치, 기존 회귀 통과. 충족하지 못한 항목은 blocked/partial로 기록하며 임의로 100% 완료 판정하지 않는다.

## 확인된 위험과 대응

1. Yahoo chart JSON은 접근 가능하지만 공식 안정성 SLA가 없는 fallback이다. API adapter를 격리하고 이를 공식 거래소 API라고 표시하지 않는다. KIS/KRX 권한이 확보되면 우선순위를 올린다.
2. Treasury 공식 XML 접근 성공, FRED CSV는 초기 요청 timeout. 한국 수급·DRAM의 인증 가능한 무료 source는 미확보다.
3. 기존 fixture profile에서 DRAM은 critical이다. unavailable이면 기존 E18은 insufficient_evidence를 반환한다. 숫자 확률을 얻으려고 critical flag를 낮추지 않는다.
4. E11 Accounting 필수 구조는 실데이터 missing을 표현할 수 없다. missing 지원은 명시적인 계약/실행 경계 보완으로 구분하고 수치 알고리즘을 변경하지 않는다. 정상 회계값으로 위조하지 않는다.
5. 현재 reversal output은 검증되지 않은 score다. 이를 경험적으로 calibration된 확률이라고 이름만 바꾸지 않는다.
6. 30분봉/실거래 데이터 재배포 조건이 불명확하면 raw와 full Journal은 로컬에 보존하고 GitHub에는 코드·문서·hash·요약 증거를 게시한다.

## 순서

Plan 게시 → Source probe 및 Design 게시 → 확보 범위 보고 → 선행 테스트 → adapter/contract/availability boundary → 최초 live snapshot/실행 봉인 → replay/회귀/Check → Act에서 수집·계약 결함만 수정. 첫 live 결과를 보고 모델을 튜닝하지 않는다. 외부 권한으로 막힌 조건은 보고서에 남긴다.

## 원천 참고

- [미 재무부 XML feed](https://home.treasury.gov/treasury-daily-interest-rate-xml-feed)
- [KIS 공식 API 예제](https://github.com/koreainvestment/open-trading-api)
- [한국은행 ECOS 안내](https://www.bok.or.kr/portal/bbs/B0000522/view.do?menuNo=201692&nttId=10070977)
- [Yahoo 거래소/데이터 공급자 안내](https://help.yahoo.com/kb/SLN2310.html)

Plan 단계 직접 접근 증거: Yahoo 005935.KS 30m 264행, 장기 일봉 4,936행; common/KOSPI/FX/DXY 응답 성공; Treasury 연간 XML 266,413 bytes. 이는 운영 SLA나 독립 교차 검증 완료를 뜻하지 않는다.
