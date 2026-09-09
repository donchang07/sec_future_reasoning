# SEC Future Reasoning

AI 기반 미래추론 시스템 연구 및 구현 프로젝트입니다.

## 목표

복잡계라고 불려온 금융시장, 경제정책, 기업경영, 지정학, 전쟁·안보 등의 문제를 대상으로 대규모 외부기억, Ontology/Knowledge Graph, Causal Reasoning, Scenario/Counterfactual Simulation, Probability Calibration, Explainable Probability, Prediction Journal, Human+AI Review, Learned Experience, Anti-Overfitting을 결합합니다.

첫 번째 Reference Domain은 삼성전자우 미래추론 시스템입니다.

## Canonical PRD

현재 구현의 기준 문서는 `docs/samsung_preferred_future_reasoning_prd_v1.1.html` 입니다.

v0.9 문서는 역사적 참고자료이며 신규 Plan/Design/Implementation의 기준으로 사용하지 않습니다.

v1.1의 핵심은 19개 Future Reasoning Engine이 방향과 확률을 판단하고, Price Wave/Reversal Engine이 단기 30분봉·중기 일봉·장기 주봉에서 Timing을 판단하며, Multi-Timeframe Alignment와 Liquidity Confirmation을 결합해 최종 ENTRY/WAIT/HOLD/SELL을 결정하는 구조입니다. 기술적 신호는 Market Regime, Capital Flow, Actor/Reflexivity로 피드백되어 Future Reasoning을 재계산합니다.

## 개발 원칙

bkit-codex PDCA를 사용합니다. Plan과 Design은 반드시 canonical PRD v1.1을 먼저 읽고 작성합니다. 첫 구현 목표는 전체 기능 완성이 아니라 하나의 실제 입력이 전체 reasoning pipeline을 통과하여 horizon별 forecast, timing, decision, explanation, Prediction Journal을 생성하는 End-to-End Vertical Slice입니다.

## PDCA 문서

- [전체 구현 Plan](docs/01-plan/features/sec-future-reasoning-v1-1.plan.md)
- [통합 Design](docs/02-design/features/sec-future-reasoning-v1-1.design.md)
- [19개 Engine·추론 모델·Timing](docs/02-design/features/sec-future-reasoning-v1-1/engines-and-model.md)
- [49 Factor Registry 설계](docs/02-design/features/sec-future-reasoning-v1-1/factor-registry.md)
- [Golden 80개 사례](docs/02-design/features/sec-future-reasoning-v1-1/golden-cases.md)

문서의 설계 가정과 테스트 명세는 실제 구현·실데이터 검증 결과와 구분합니다.

## 현재 구현

Foundation 계약과 E01–E19 최소 알고리즘을 구현했습니다. 합성 삼성전자우 fixture가 1주·1개월·1년 각각에서 추론→Wave/Alignment/Liquidity→기술 feedback 1회→Decision→Prediction Journal까지 실행됩니다. 114개 중간 EngineResult를 조회하고 contribution ledger와 전체 replay로 결과를 검증합니다.

- [설치·fixture 실행·Journal 조회](docs/VERTICAL_SLICE.md)
- [최신 Check: 결함 4개 수정과 89개 테스트](docs/03-analysis/reasoning-vertical-slice.analysis.md)
- [완료 보고서와 Horizon별 결과](docs/04-report/reasoning-vertical-slice.report.md)
- [Foundation 계약 설명](docs/FOUNDATION.md)

```powershell
python -m pip install -r requirements.lock
python -m reasoning run-fixture --output artifacts/local/prediction-journal.json
python -m reasoning verify-journal --journal artifacts/local/prediction-journal.json --replay
```

핵심 15개를 포함한 pytest 89개와 GitHub CI Python 3.11/3.12가 통과했습니다. 원래 Golden 80개 전체는 아직 실행 완료 상태가 아니므로 product release gate는 닫혀 있습니다. 합성 fixture의 calibration은 unvalidated이며 실데이터 adapter·운영 검증·DB/API/UI는 후속 범위입니다.
