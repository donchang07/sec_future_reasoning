from pathlib import Path
from publication.briefing import HEADER_SVG, render_briefing


def journal():
    technical_1w={
        'wave':{'bottom_score':0.1,'top_score':0.2},
        'bullish_alignment':0.1333333333,'bearish_alignment':0.2666666667,
        'buy_liquidity':None,'sell_liquidity':None,
    }
    technical_1m={
        'wave':{'bottom_score':0.3,'top_score':0.45},
        'bullish_alignment':0.4,'bearish_alignment':0.0,
        'buy_liquidity':None,'sell_liquidity':None,
    }
    technical_1y={
        'wave':{'bottom_score':0.0,'top_score':0.1},
        'bullish_alignment':0.4,'bearish_alignment':0.0,
        'buy_liquidity':None,'sell_liquidity':None,
    }
    return {
        'run_id':'00000000-0000-0000-0000-000000000001',
        'prediction_timestamp':'2026-09-14T22:00:11+00:00',
        'data_cutoff':'2026-09-14T22:00:11+00:00',
        'contract_version':'real-world-contract-v2.0.0',
        'mapping_version':'semantic-mapping-v1.0.0',
        'p0':{'value':183400.0,'unit':'krw_per_share','timeframe':'30m',
              'effective_at':'2026-09-14T06:30:00+00:00',
              'definition':'last eligible completed close, not execution quote'},
        'sources':[
            {'status':'fresh','used_by_model':True},
            {'status':'fresh','used_by_model':False},
            {'status':'unavailable','used_by_model':False},
        ],
        'horizons':[
            {'horizon':'1w','final':{'probabilities':{'up':0.36,'down':0.42,'flat':0.22},'confidence':0.051},
             'decision':{'action':'WAIT','reasons':['future_up','confidence','liquidity','custom|gate']},
             'passed_gates':['meta_check'],'technical':technical_1w,
             'assessment':{'eligible':True,'reasons':[],'strong_missing':['foreign_net_buy','usdkrw']}},
            {'horizon':'1m','final':{'probabilities':{'up':0.37,'down':0.40,'flat':0.23},'confidence':0.04},
             'decision':{'action':'WAIT','reasons':['future_up','confidence','alignment','liquidity']},
             'passed_gates':['meta_check'],'technical':technical_1m,
             'assessment':{'eligible':True,'reasons':[],'strong_missing':['dram_contract_asp','hbm_demand']}},
            {'horizon':'1y','final':None,
             'decision':{'action':'WAIT','reasons':['meta_check','confidence','liquidity']},
             'passed_gates':[],'technical':technical_1y,
             'assessment':{'eligible':False,'reasons':['coverage:memory','memory_family_quorum'],
                           'strong_missing':['dram_contract_asp','hbm_demand','samsung_eps']}},
        ],
    }


def test_navy_header_is_accessible_and_self_contained():
    svg=HEADER_SVG.decode('utf-8')
    assert '#081A33' in svg and 'DAILY MARKET BRIEFING' in svg
    assert 'role="img"' in svg and '<title>' in svg
    assert '<script' not in svg.lower()
    assert svg.count('http://')==1 and 'www.w3.org/2000/svg' in svg
    assert 'https://' not in svg and '<image' not in svg.lower()
    asset=Path(__file__).resolve().parents[1]/'docs/predictions/assets/daily-briefing-navy.svg'
    assert asset.read_bytes()==HEADER_SVG


def test_briefing_leads_with_professional_summary_and_key_forecasts():
    text=render_briefing(journal())
    first=text.index('## 오늘의 결론')
    forecasts=text.index('## 오늘의 주요 예측')
    detail=text.index('## 전문 브리핑')
    assert first < forecasts < detail
    assert 'daily-briefing-navy.svg' in text
    assert '2026년 9월 15일 07:00 KST' in text
    assert '183,400원' in text and '실행 가능 호가가 아닙니다' in text
    assert '## 오늘의 결론 — 관망 (WAIT)' in text
    assert '| 1주 | 36.0% | 42.0% | 22.0% | 하락 우위 (+6.0%p) | 5.1% · 매우 낮음 | 관망 (WAIT) |' in text
    assert '| 1개월 | 37.0% | 40.0% | 23.0% | 상승·하락 경합 (3.0%p) | 4.0% · 매우 낮음 | 관망 (WAIT) |' in text
    assert '| 1년 | 산출 보류 | 산출 보류 | 산출 보류 | 필수 근거 부족 | 산출 보류 | 관망 (WAIT) |' in text


def test_briefing_separates_direction_timing_liquidity_and_unknowns():
    text=render_briefing(journal())
    assert '타이밍 지표이며 방향 확률을 결정하지 않습니다' in text
    assert '확인 불가' in text
    assert '외국인 순매수 (foreign_net_buy)' in text
    assert 'DRAM 계약가격 (dram_contract_asp)' in text
    assert '메모리 커버리지 부족 (coverage:memory)' in text
    assert 'custom\\|gate' in text
    assert 'None' not in text
    assert '[전체 설명·기여도 감사 보고서](explainability.md)' in text
    assert '[봉인된 Prediction Journal](journal.json)' in text
    assert 'professional-briefing-v1.0.0' in text


def test_empty_horizons_remain_explicitly_insufficient():
    item=journal();item['horizons']=[]
    text=render_briefing(item)
    assert '산출 가능한 Horizon이 없습니다' in text
    assert 'INSUFFICIENT_EVIDENCE' in text
