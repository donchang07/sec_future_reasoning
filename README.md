# SEC Future Reasoning

AI 기반 미래추론 시스템 연구 및 구현 프로젝트입니다.

## 목표

복잡계라고 불려온 금융시장, 경제정책, 기업경영, 지정학, 전쟁·안보 등의 문제를 대상으로 다음 구조를 실험합니다.

- 대규모 외부기억
- Ontology와 Knowledge Graph
- Causal Reasoning
- Scenario / Counterfactual Simulation
- Probability Calibration
- Explainable Probability
- Prediction Journal
- Human + AI Review
- Learned Experience
- Anti-Overfitting
- Horizon-based Decision Engine

첫 번째 Reference Domain은 삼성전자우 미래추론 시스템입니다.

## 현재 문서

- `docs/universal_ai_future_reasoning_prd_v0.9.html`
- `docs/samsung_preferred_future_reasoning_prd_v0.9.html`

## 현재 상태

v0.9는 구현 이전의 Reasoning Engine 중심 PRD입니다.

핵심은 19개 Reasoning Engine의 Input → Process → Output → Memory Read/Write → Failure/Retry 구조와 Golden Test Cases입니다.

다음 단계는 실제 코드 구조, ontology/graph seed, Supabase schema, Neo4j constraints, API, UI wireframe, ingestion과 test harness를 만드는 것입니다.
