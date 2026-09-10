# 2026-09-11 vs 2026-09-10: 1주 상승확률 변화 분석

기존 봉인 Journal의 Contribution Ledger 비교이며, 모델 재실행이나 설정 변경은 수행하지 않았다.

## 비교 대상

- [9/10 Journal](../predictions/2026-09-10/2ce0e81e-6569-53de-8b7a-fc7ecd854d7a/journal.json): 12:15:33 KST 예외 실행, daily-preopen-v1.0.0.
- [9/11 Journal](../predictions/2026-09-11/ad9cf183-cd34-512e-8386-d8436b2e28e4/journal.json): 07:00:11 KST 실행, daily-preopen-v1.0.1.
- 1주 Up: 44.40744803064189% → 47.12224636255047%, 차이 +2.714798331908585%p.
- Confidence: 16.17644% → 8.03457%. 최종 Decision은 모두 WAIT.

## 장부상 증가폭 상위 3개

| Factor | 어제 Up 기여(%p) | 오늘 Up 기여(%p) | 기여 변화(%p) |
|---|---:|---:|---:|
| preferred_trend_alignment | +4.316946 | +5.791229 | +1.474283 |
| samsung_common_price | +3.647593 | +4.870645 | +1.223053 |
| samsung_preferred_price | +3.651800 | +4.813151 | +1.161350 |

이 세 항목은 세 개의 독립적인 시장 호재를 뜻하지 않는다. 공통적으로 E01의 서로 다른 관측 시점 수가 3개에서 4개로 증가하면서 quality가 0.75에서 1.00으로 증가했다. 세 항목의 정규화된 방향 신호는 모두 양일 +1.0으로 동일하다.

[E01/E06/E08 코드](../../reasoning/engines.py)의 quality는 관측 시점 수와 동일 시점 Source 간 spread로 계산된다.

```text
quality = min(1, 관측 시점 수 / 4) × max(0.1, 1 - spread / scale)
E06 contribution = normalized × sign × quality / module_expected_factor_count
```

세 항목의 E08 경로 강도는 각각 0.6075 → 0.81로 커졌다. 이것이 기존 양의 신호를 더 크게 반영한 직접적인 계산 메커니즘이다. 아래 %p는 비선형 확률 갱신 과정의 장부 값이므로 다른 항목의 선행 갱신 상태도 영향을 준다.

- 추세 정렬: 원래 값 1.0 → 1.0. 추세 자체의 추가 개선으로 해석할 수 없다.
- 보통주: snapshot의 마지막 가격은 269,500원 → 269,000원으로 하락했다. 정규화 값은 양일 +1로 포화되어 있으므로 보통주 상승이 원인이라는 설명은 잘못이다.
- 우선주: snapshot의 마지막 가격은 197,500원 → 203,000원으로 상승했지만, 정규화 값은 이미 양일 +1이다. 해당 경로 강도 증가를 가격 상승만으로 설명할 수 없다.

여기의 quality는 E01의 개별 신호 품질 계수이며 최종 Model Confidence와 다르다.

## 전체 변화 재구성

| 장부 항목 | 오늘 − 어제 Up 기여(%p) |
|---|---:|
| 추세 정렬 / E12 | +1.474283049 |
| 보통주 가격 / E12 | +1.223052635 |
| 우선주 가격 / E12 | +1.161350423 |
| RSI / E12 | +0.749559218 |
| Reflexivity / E10 | +0.513360747 |
| Historical / E13 | 0.000000000 |
| USD/KRW / E12 | -0.211164648 |
| Scenario / E17 | -0.343924032 |
| Challenger / E14 | -0.383609262 |
| Calibration / E18 | -0.428798391 |
| 미국 10년물 / E12 | -1.039311406 |
| 합계 | +2.714798332 |

상위 세 항목 +3.858686107%p에 나머지 순효과 -1.143887775%p를 더하면 최종 +2.714798332%p가 된다. 양일 Prior는 Up 40% / Down 35% / Flat 25%로 동일하다. Calibration 기여 차이는 입력 변화에 따른 동일 알고리즘의 결과이며 Calibration 설정 변경이 아니다.

RSI는 54.72383 → 57.48792로 상승했고 quality도 증가했다. 미국 10년물 입력은 4.80% → 4.95%로 높아져 하방 기여가 커졌다. 다만 Source 거래일은 9/8 → 9/10으로 바뀌었으므로 이를 단일 거래일 금리 변화로 부르면 안 된다. USD/KRW는 오늘 완료 시점 검증 문제로 unavailable이며 synthetic 또는 neutral 값으로 보충하지 않았다.

## 해석 범위와 Finding

1. 위 순위는 두 Journal의 순차적 contribution ledger에서 동일 항목의 Up 기여를 차감한 회계적 분해다. 독립적인 개입 효과나 Shapley attribution이 아니다. 비선형 갱신과 순서 의존성이 존재한다.
2. 양일 1주 Technical Feedback 전후 확률 변화는 모두 0이다. 이번 +2.71%p를 Technical Feedback 개선으로 설명할 수 없다.
3. Nasdaq/SOX/미국 반도체주 진단은 frozen model에 주입되지 않으므로 이번 확률 증가 원인에 포함하지 않는다.
4. 어제는 정오 예외 실행, 오늘은 오전 정식 실행이며 Data Timing bug-fix 운영정책도 다르다. 순수한 동일 시각·동일 수집정책의 일간 시장 변화 비교가 아니다.
5. 관측 수 증가와 고정 기준값에서의 정규화 포화 때문에 가격이 하락한 Factor의 양의 기여도 증가할 수 있다는 점을 Finding으로 남긴다. 이번 분석에서는 이를 이유로 Weight, Prior, Calibration, 계약, Threshold 또는 기존 Journal을 수정하지 않는다.
6. 상승확률은 높아졌지만 최종 Confidence는 낮아졌고 Decision은 WAIT다. 개별 quality 증가와 전체 예측 신뢰도 개선을 혼동하지 않아야 한다.

검증: 양일 ledger의 순차 before/after 연결 및 delta 합계로 최종 Up을 재구성하고, 항목별 차이 합계가 +2.714798331908585%p와 일치하는지 확인했다. 문서만 추가했으며 기존 Journal과 실행 코드는 변경하지 않았다.
