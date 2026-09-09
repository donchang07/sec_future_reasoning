> Update 2026-09-09: CK-01 through CK-04 are fixed and rechecked in the [vertical slice Check](reasoning-vertical-slice.analysis.md). The evaluation below is historical and refers to its original commit. Full-product completion is not claimed.

# reasoning-foundation — 초기 Gap Analysis (재검토 전 기록)

> **2026-09-09 Check 재검토:** 아래 100%는 초기 판정 이력이다. 추가 검증에서 F01/F03/F05/F06 결함을 재현하여 현재 판정은 3/7 match, 4/7 partial, Act 필요로 정정했다. [최신 Check 결과](sec-future-reasoning-v1-1.analysis.md)를 따른다.

> 2026-09-09 · P1 범위 · Design 1.0.0 · Match rate: 7/7 = 100%

기준: [P1 Design](../02-design/features/reasoning-foundation.design.md). 이 비율은 전체 제품 또는 19 Engine 알고리즘 구현률이 아니다.

| 항목 | 구현 | 검증 / 결과 |
|---|---|---|
| F01 typed Engine contract | `reasoning/schemas/artifacts.py` | 19 discriminator branch roundtrip/extra-field 차단, engine ID 불일치, 상태별 artifact/evidence 검증 |
| F02 Probability/ledger | `reasoning/schemas/contracts.py` | NaN/Infinity/bool/string/range/합계·ledger 순서/연결/delta·target·가격범위 거절 |
| F03 cutoff/version | `contracts.py` VersionBundle/Observation/select_as_of | 19 version 필수, naive 시각 거절, 미래 revision 제외, source 충돌 보존 |
| F04 immutable journal | JournalSnapshot/SealedJournal | 중첩 수정·중복 관측·cutoff 위반·hash 변조 거절, UTC canonical hash |
| F05 registry | `ontology/registry.json`, `reasoning/registry.py` | 49 ID/9 Module, dependency 검증, 미확인 공급자 connected 거절, 설계 문서 drift 검사 |
| F06 Golden catalog | `tests/golden/catalog.json`, validation CLI | 원문 80개 보존, unresolved 표시, release gate exit 1, CRLF/LF 동일 hash |
| F07 schema/test/CI | `packages/schemas`, `tests`, `.github/workflows/test.yml` | 6 schema 재생성 일치, 50 pytest 통과, 원격 Python 3.11/3.12 CI 성공 |

## 실행 증거

- 로컬 Python 3.11.9 / Pydantic 2.12.5 / pytest 9.0.2.
- `python -m pytest -q`: 50 passed.
- `python -m reasoning validate`: engines=19, factors=49, modules=9, golden_cases=80.
- `python -m reasoning release-check`: release_ready=false, cases=80, exit 1 (예상 동작).
- `python -m compileall -q reasoning scripts/build_foundation_data.py`: 성공.
- [GitHub CI run 34313771803](https://github.com/donchang07/sec_future_reasoning/actions/runs/34313771803): 성공, 구현 커밋 `72a0c3a` 대상.

## 테스트 선행 및 수정 사항

최초 테스트는 구현 패키지 부재로 실패했다. 구현 후 추가 경계 테스트에서 빈 applicable output 허용과 중복 journal observation 허용을 발견해 수정했다. Windows/Linux의 Git 줄바꿈 차이로 source hash가 달라지는 회귀 테스트도 먼저 실패시킨 뒤 UTF-8/LF 정규화로 수정했다. 전체 50개를 재실행하여 통과했다.

## 설계 구체화와 잔여 범위

- Python 운영 목표 3.12에 더해 로컬 3.11을 지원한다. CI 두 버전으로 확인했다.
- schema cross-field 의미 검증은 Pydantic validator가 수행한다. JSON Schema만으로 동일한 보호를 제공한다고 주장하지 않는다.
- 명시적인 non-applicable artifact는 계약 검증 fixture다. 실제 Engine 실행 성공으로 집계하지 않는다.
- DB append-only/실제 수집/추론 실행/Wave·Decision 알고리즘/API/UI는 P1 범위 밖이며 미구현이다.
- Golden 80개는 전부 unresolved다. 제품 성능/Golden 실행 통과율은 아직 없다.

P1의 문서화된 일곱 기준은 충족했다. 다음은 `reasoning-vertical-slice`의 기능 Plan/Design 및 구현이다.
