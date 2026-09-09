# 완료 보고: reasoning-vertical-slice

2026-09-09 · [Plan](../01-plan/features/reasoning-vertical-slice.plan.md) → [Design](../02-design/features/reasoning-vertical-slice.design.md) → 구현 → [Check](../03-analysis/reasoning-vertical-slice.analysis.md)

기존 결함 CK-01~04를 수정하고, Foundation 계약 그대로 E01–E19 실제 최소 알고리즘을 구현했다. 합성 fixture 한 세트가 세 Horizon에서 E01→E19→Wave→Alignment→Liquidity→Feedback→Decision→Journal 경로를 통과했다. 기술 feedback은 한 번만 적용되고, 최종 확률은 25행 contribution ledger로 각각 재구성된다.

- **구현 commit:** `1f38e7fad801b4bc7e1d65b09becf7eba2ec1de4`
- **검증:** 로컬 pytest 89 passed. 요청 핵심 15개 모두 실행·통과. 114개 EngineResult success. 저장 후 전체 replay 일치.
- **GitHub CI:** [Python 3.11/3.12 모두 성공](https://github.com/donchang07/sec_future_reasoning/actions/runs/34315461362). 실행 Journal을 각 matrix job의 artifact로 제공한다.
- **로컬 Journal:** `artifacts/local/prediction-journal.json`
- **run_id:** `f7a47f5a-af4b-5681-b12a-185da7aa619d`
- **Journal SHA256:** `43c01ba07a8755f6357e7dac026ba555bb4e96ed3d4bbb538dbdab30574c6067`
- **사용법:** [VERTICAL_SLICE.md](../VERTICAL_SLICE.md). 모든 중간 artifact를 CLI의 horizon/engine/generation 필터로 조회한다.

| 기간 | 상승 | 하락 | 횡보 | Confidence | 결정 |
|---|---:|---:|---:|---:|---|
| 단기 1주 | 79.01% | 9.20% | 11.78% | 98.19% | WAIT |
| 중기 1개월 | 75.47% | 11.50% | 13.04% | 96.54% | WAIT |
| 장기 1년 | 69.08% | 15.60% | 15.32% | 94.15% | WAIT |

바닥 timing .90, alignment 1.00, liquidity 1.00이지만 상승확률이 .80 미만이어서 ENTRY를 내지 않았다. DRAM/HBM·AI 수요 등 positive path와 CXMT 공급증가·PER 등 negative path를 함께 제공한다. fixture 수치이며 calibration은 unvalidated, 결정은 research_only다.

Check에서 최소 요청 범위 31/31개를 충족했다. 원래 Golden 80개 전체를 통과했다는 뜻은 아니다. 제품 release gate는 false를 유지한다. 실데이터 adapter, 전체 49개 데이터 연결, 운영 검증·calibration, DB/API/UI는 다음 기능별 Plan/Design 대상이다.

문서·코드·PDCA 상태는 origin/main에 게시했다. 기존 로컬 `.codex/config.toml` 변경은 이번 commit에서 제외했다. API key나 외부 계정 정보는 fixture에 없으며 합성 자료만 게시했다.
