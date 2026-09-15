"""Deterministic Korean executive briefing for validated public journals."""
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo


VERSION='professional-briefing-v1.0.0'
KST=ZoneInfo('Asia/Seoul')
HORIZON_LABELS={'1d':'1일','1w':'1주','1m':'1개월','3m':'3개월','1y':'1년'}
ACTION_LABELS={
    'WAIT':'관망 (WAIT)','HOLD':'보유 유지 (HOLD)','ENTRY':'진입 검토 (ENTRY)',
    'SELL':'매도 검토 (SELL)','WATCH':'주의 관찰 (WATCH)','NO_ACTION':'행동 보류 (NO_ACTION)',
}
GATE_LABELS={
    'future_up':'방향 확률 기준','without_history_up':'역사자료 제외 강건성',
    'confidence':'확신도 기준','bottom_timing':'반전 타이밍 기준',
    'alignment':'다중 시간축 정렬','liquidity':'유동성 확인','meta_check':'메타 검증',
}
REASON_LABELS={
    'coverage:memory':'메모리 커버리지 부족','memory_family_quorum':'메모리 근거군 정족수 부족',
}
FACTOR_LABELS={
    'foreign_net_buy':'외국인 순매수','institution_net_buy':'기관 순매수','program_net_buy':'프로그램 순매수',
    'usdkrw':'원·달러 환율','dram_contract_asp':'DRAM 계약가격','hbm_demand':'HBM 수요',
    'hbm_price':'HBM 가격','samsung_eps':'삼성전자 EPS','samsung_eps_revision':'삼성전자 EPS 추정치 변화',
    'bit_supply':'메모리 비트 공급','cxmt_memory_capacity':'CXMT 메모리 생산능력','equity_discount_rate':'주식 할인율',
    'fab_capacity':'팹 생산능력','gpu_demand_growth':'GPU 수요 성장','hyperscaler_capex':'하이퍼스케일러 CAPEX',
    'memory_bit_shipment':'메모리 비트 출하','memory_inventory':'메모리 재고','new_capacity':'신규 생산능력',
    'samsung_forward_per':'삼성전자 선행 PER','samsung_free_cash_flow':'삼성전자 잉여현금흐름',
    'yield_rate':'수율',
}
P0_LABELS={'last eligible completed close, not execution quote':'마지막 적격 완료 가격'}

HEADER_SVG='''<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="260" viewBox="0 0 1400 260" role="img" aria-labelledby="title desc">
  <title>SEC Future Reasoning Daily Market Briefing</title>
  <desc>Navy professional briefing header for Samsung Electronics preferred-share forecasts</desc>
  <rect width="1400" height="260" rx="18" fill="#081A33"/>
  <rect x="0" y="0" width="18" height="260" rx="9" fill="#4DB6D0"/>
  <rect x="82" y="62" width="58" height="4" fill="#C8A96A"/>
  <text x="82" y="112" fill="#A9C2D9" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="24" font-weight="600" letter-spacing="5">SEC FUTURE REASONING</text>
  <text x="82" y="172" fill="#FFFFFF" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="52" font-weight="700" letter-spacing="1">DAILY MARKET BRIEFING</text>
  <text x="84" y="218" fill="#D7E2EC" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="23">Samsung Electronics Preferred · Explainable Forecast</text>
  <circle cx="1284" cy="88" r="38" fill="none" stroke="#4DB6D0" stroke-width="3" opacity="0.9"/>
  <circle cx="1284" cy="88" r="12" fill="#C8A96A"/>
  <path d="M1190 190 H1320" stroke="#4DB6D0" stroke-width="4"/>
  <path d="M1220 170 L1252 142 L1282 158 L1320 120" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
'''.encode('utf-8')


def _safe(value):
    if value is None:return '확인 불가'
    return str(value).replace('\\','\\\\').replace('|','\\|').replace('\r',' ').replace('\n',' ')


def _time(value):
    if not value:return '확인 불가'
    try:
        stamp=datetime.fromisoformat(str(value).replace('Z','+00:00'))
        if stamp.tzinfo is None:return '시간대 미확인'
        stamp=stamp.astimezone(KST)
        return f'{stamp.year}년 {stamp.month}월 {stamp.day}일 {stamp:%H:%M} KST'
    except (TypeError,ValueError):return '확인 불가'


def _pct(value):return '산출 보류' if value is None else f'{100*float(value):.1f}%'


def _confidence(value):
    if value is None:return '산출 보류'
    value=float(value)
    band='매우 낮음' if value<.25 else '낮음' if value<.5 else '보통' if value<.7 else '높음'
    return f'{_pct(value)} · {band}'


def _action(value):
    value=str(value or 'NO_ACTION')
    return ACTION_LABELS.get(value,_safe(value))


def _horizon(value):return HORIZON_LABELS.get(str(value),_safe(value))


def _direction(final):
    if not final:return '필수 근거 부족'
    p=final.get('probabilities') or {};up=p.get('up');down=p.get('down')
    if up is None or down is None:return '필수 근거 부족'
    spread=abs(float(up)-float(down))*100
    if spread<5:return f'상승·하락 경합 ({spread:.1f}%p)'
    leader='상승' if float(up)>float(down) else '하락'
    return f'{leader} 우위 (+{spread:.1f}%p)'


def _overall(horizons):
    if not horizons:return '근거 부족 (INSUFFICIENT_EVIDENCE)'
    actions={str((h.get('decision') or {}).get('action') or 'NO_ACTION') for h in horizons}
    if len(actions)==1:return _action(next(iter(actions)))
    return '기간별 혼합 판단'


def _liquidity(technical):
    buy=technical.get('buy_liquidity');sell=technical.get('sell_liquidity')
    if buy is None and sell is None:return '확인 불가'
    return f"매수 {_pct(buy) if buy is not None else '확인 불가'} / 매도 {_pct(sell) if sell is not None else '확인 불가'}"


def _gate_list(values):
    values=list(values or [])
    if not values:return '없음'
    return ', '.join(GATE_LABELS.get(str(v),_safe(v)) for v in values)


def _reason_list(values):
    values=list(values or [])
    if not values:return '없음'
    return ', '.join(f"{REASON_LABELS.get(str(v),_safe(v))} ({_safe(v)})" if str(v) in REASON_LABELS else _safe(v) for v in values)


def _missing(values):
    unique=[]
    for value in values or []:
        value=str(value)
        if value not in unique:unique.append(value)
    shown=unique[:8];items=[]
    for value in shown:
        label=FACTOR_LABELS.get(value)
        items.append(f'{label} ({_safe(value)})' if label else _safe(value))
    if len(unique)>8:items.append(f'외 {len(unique)-8}개')
    return ', '.join(items) if items else '추가 누락 없음'


def _reference_price(p0):
    if not p0 or p0.get('value') is None:return '확인 불가'
    value=float(p0['value'])
    if p0.get('unit')=='krw_per_share':return f'{value:,.0f}원'
    return f"{value:,.2f} {_safe(p0.get('unit'))}"


def _executive(horizons):
    if not horizons:return '산출 가능한 Horizon이 없습니다. 현재 상태는 INSUFFICIENT_EVIDENCE이며 숫자 전망을 대신 만들어 표시하지 않습니다.'
    quantified=[h for h in horizons if h.get('final')]
    withheld=[h for h in horizons if not h.get('final')]
    parts=[]
    if quantified:
        signals='; '.join(f"{_horizon(h.get('horizon'))} {_direction(h.get('final'))}" for h in quantified)
        parts.append(f'방향성은 {signals}입니다.')
        confidences=[float(h['final']['confidence']) for h in quantified if h['final'].get('confidence') is not None]
        if confidences:
            lo=min(confidences);hi=max(confidences)
            display=_pct(lo) if lo==hi else f'{_pct(lo)}~{_pct(hi)}'
            band='매우 낮은 수준' if hi<.25 else '낮은 수준' if hi<.5 else '중간 이상'
            parts.append(f'정량 전망 확신도는 {display}로 {band}입니다.')
    if withheld:parts.append(f"{', '.join(_horizon(h.get('horizon')) for h in withheld)} 전망은 필수 근거 부족으로 산출을 보류했습니다.")
    if any(_liquidity(h.get('technical') or {})=='확인 불가' for h in horizons):
        parts.append('거래 유동성 확인이 없어 ENTRY/SELL 확정 조건은 충족되지 않았습니다.')
    return ' '.join(parts)


def render_briefing(journal):
    horizons=list(journal.get('horizons') or []);p0=journal.get('p0') or {};overall=_overall(horizons)
    sources=list(journal.get('sources') or []);statuses=Counter(str(s.get('status') or 'unknown') for s in sources)
    status_labels={'fresh':'신선','stale':'지연','unavailable':'사용 불가','unknown':'상태 미확인'}
    status_text=', '.join(f"{status_labels.get(k,_safe(k))} {v}개" for k,v in sorted(statuses.items())) or '등록 정보 없음'
    used=sum(1 for source in sources if source.get('used_by_model') is True)
    lines=[
        '<p align="center">','  <img src="../../assets/daily-briefing-navy.svg" alt="SEC Future Reasoning professional daily market briefing" width="100%">','</p>','',
        '| 브리핑 기준 | 대상 | 기준가격(P0) | 기준가격 시각 |','|---|---|---:|---|',
        f"| {_time(journal.get('prediction_timestamp'))} | 삼성전자우 (005935) | {_reference_price(p0)} | {_time(p0.get('effective_at'))} |",'',
        f"> **P0 기준:** {P0_LABELS.get(str(p0.get('definition')),_safe(p0.get('definition')))}. 화면의 기준가격은 마지막 적격 완료 가격이며 **실행 가능 호가가 아닙니다.**",'',
        f'## 오늘의 결론 — {overall}','',_executive(horizons),'',
        '## 오늘의 주요 예측','',
    ]
    if horizons:
        lines+=['| 기간 | 상승 | 하락 | 보합 | 방향 요약 | 확신도 | 최종 판단 |','|---|---:|---:|---:|---|---|---|']
        for item in horizons:
            final=item.get('final');p=(final or {}).get('probabilities') or {};decision=item.get('decision') or {}
            lines.append('| '+' | '.join([
                _horizon(item.get('horizon')),_pct(p.get('up')),_pct(p.get('down')),_pct(p.get('flat')),
                _direction(final),_confidence((final or {}).get('confidence')),_action(decision.get('action')),
            ])+' |')
    else:lines+=['> **INSUFFICIENT_EVIDENCE** — 산출 가능한 Horizon이 없습니다.','']

    lines+=['','## 전문 브리핑','','### 1. 방향 해석','']
    if horizons:
        for item in horizons:
            label=_horizon(item.get('horizon'));final=item.get('final');decision=_action((item.get('decision') or {}).get('action'))
            if not final:
                reasons=_reason_list((item.get('assessment') or {}).get('reasons'))
                lines.append(f'- **{label}:** 확률 산출 보류. 근거 상태는 {reasons}이며 공식 판단은 {decision}입니다.')
                continue
            p=final.get('probabilities') or {};up=p.get('up');down=p.get('down')
            lines.append(f"- **{label}:** 상승 {_pct(up)}, 하락 {_pct(down)}로 {_direction(final)}입니다. 확신도는 {_confidence(final.get('confidence'))}이며 공식 판단은 {decision}입니다.")
    else:lines.append('- 해석할 방향 확률이 없습니다.')

    lines+=['','### 2. 타이밍·시간축 정렬·유동성','',
        '| 기간 | 바닥 반전 | 천장 반전 | 상승/하락 정렬 | 유동성 |','|---|---:|---:|---|---|']
    for item in horizons:
        technical=item.get('technical') or {};wave=technical.get('wave') or {}
        lines.append('| '+' | '.join([
            _horizon(item.get('horizon')),_pct(wave.get('bottom_score')),_pct(wave.get('top_score')),
            f"{_pct(technical.get('bullish_alignment'))} / {_pct(technical.get('bearish_alignment'))}",_liquidity(technical),
        ])+' |')
    if not horizons:lines.append('| — | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |')
    lines+=['', '> Price Wave/Reversal은 **진입·청산 타이밍 지표이며 방향 확률을 결정하지 않습니다.** 방향, 시간축 정렬, 반전 타이밍, 유동성이 함께 확인되어야 최종 ENTRY/SELL이 가능합니다.','',
        '### 3. 의사결정 게이트','',
        '| 기간 | 통과한 게이트 | 미충족 게이트 | 정책 결과 |','|---|---|---|---|']
    for item in horizons:
        decision=item.get('decision') or {}
        lines.append(f"| {_horizon(item.get('horizon'))} | {_gate_list(item.get('passed_gates'))} | {_gate_list(decision.get('reasons'))} | {_action(decision.get('action'))} |")
    if not horizons:lines.append('| — | 없음 | 메타 검증 | 근거 부족 (INSUFFICIENT_EVIDENCE) |')

    lines+=['','## 데이터 신뢰도와 핵심 리스크','',
        f'- **Source 상태:** 총 {len(sources)}개 · {status_text} · 모델 사용 {used}개',
        '- **Unknown 처리:** 누락·충돌·확인 불가는 중립이나 0으로 바꾸지 않으며 확신도를 낮추거나 전망을 보류합니다.','',
        '| 기간 | 적격성 | 전망 보류 사유 | 주요 누락 근거 |','|---|---|---|---|']
    for item in horizons:
        assessment=item.get('assessment') or {};eligible='적격' if assessment.get('eligible') is True else '산출 보류'
        lines.append(f"| {_horizon(item.get('horizon'))} | {eligible} | {_reason_list(assessment.get('reasons'))} | {_missing(assessment.get('strong_missing'))} |")
    if not horizons:lines.append('| — | 산출 보류 | Horizon 없음 | 구조화된 전망 없음 |')

    lines+=['','## 읽는 법과 한계','',
        '- 이 문서는 봉인된 시스템 출력을 읽기 쉽게 요약한 **research-only 브리핑**이며 개인화된 투자자문이 아닙니다.',
        '- 확률의 상대적 우위와 실제 매매 행동은 다릅니다. 최종 행동은 저장된 Decision Policy 결과만 표시합니다.',
        '- 예측 시점 이후의 정보로 이 브리핑이나 원본 Journal을 고쳐 쓰지 않습니다. Outcome은 별도 불변 기록으로 연결됩니다.','',
        '## 감사 및 재현성','',
        '- [전체 설명·기여도 감사 보고서](explainability.md)',
        '- [봉인된 Prediction Journal](journal.json)',
        f"- Run ID: `{_safe(journal.get('run_id'))}`",
        f"- Data cutoff: `{_safe(journal.get('data_cutoff'))}`",
        f"- Contract / mapping: `{_safe(journal.get('contract_version'))}` / `{_safe(journal.get('mapping_version'))}`",
        f'- Briefing renderer: `{VERSION}`','',
    ]
    return '\n'.join(lines)
