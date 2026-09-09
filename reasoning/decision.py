"""Policy gates, independent from probability estimation."""
from typing import Literal
from .schemas.contracts import Contract


class Decision(Contract):
    action: Literal['ENTRY','SELL','WAIT','HOLD']
    reasons: tuple[str,...]
    research_only: bool = True


def decide(*,up,down,no_history_up,no_history_down,confidence,bottom,top,bottom_confirmed,
           top_confirmed,bullish_alignment,bearish_alignment,buy_liquidity,sell_liquidity,fatal,held):
    def enough(value,threshold):
        return value is not None and value>=threshold
    buy={'future_up':enough(up,.80),'without_history_up':enough(no_history_up,.80),'confidence':enough(confidence,.70),
         'bottom_timing':bottom_confirmed and enough(bottom,.75),'alignment':enough(bullish_alignment,.70),
         'liquidity':enough(buy_liquidity,.60),'meta_check':not fatal}
    sell={'future_down':enough(down,.70),'without_history_down':enough(no_history_down,.70),'confidence':enough(confidence,.65),
          'top_timing':top_confirmed and enough(top,.65),'alignment':enough(bearish_alignment,.70),
          'liquidity':enough(sell_liquidity,.60),'meta_check':not fatal}
    if held and all(sell.values()): return Decision(action='SELL',reasons=('all_sell_gates_confirmed',))
    if not held and all(buy.values()): return Decision(action='ENTRY',reasons=('all_entry_gates_confirmed',))
    gates=sell if held else buy
    return Decision(action='HOLD' if held else 'WAIT',reasons=tuple(k for k,v in gates.items() if not v))
