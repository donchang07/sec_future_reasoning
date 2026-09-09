# live-forward-v2 preflight

Completed before fresh collection and before viewing any v2 live forecast.

- Executable commit: `73c30f77608813bafcecf137e413e88b3c01d7cf`.
- Local tests: 187 passed (170 existing + 17 new).
- CI: https://github.com/donchang07/sec_future_reasoning/actions/runs/34320231170 — Python 3.11 and 3.12 passed, fixture replay and release-gate checks passed.
- Released contract manifest verifies unchanged. Original engine, technical, decision, graph/profile and refinement sources have no diff from the prior release.
- Both original journals replayed successfully in their original recorded-code worktrees; neither was edited.
- Raw/source cutoff, typed E11 company projection, missing-domain non-applicability, unsupported graph routing, value-only exclusion, 114 invocations, one feedback, withholding and contribution reconstruction passed offline tests.
- Lock: [pre-run-lock](live-forward-v2.pre-run-lock.json). Includes normalized source/dependency/ontology/test hashes, runtime, versions and historical journal byte hashes.

The raw replay test uses authored synthetic HTTP responses. It is not a historical v2 prediction and is not published as live evidence. No v2 live result has been inspected at this checkpoint. Code/config changes are now prohibited for the impending run. Collection failures and forecast limitations will be retained as evidence and findings.
