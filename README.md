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

문서의 설계 가정과 테스트 명세는 실제 구현·실데이터 검증 결과와 구분합니다. 다음 구현은 `reasoning-foundation`의 기능별 Plan/Design부터 시작합니다.
