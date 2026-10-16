import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from best_time_to_buy_sell_stock import max_profit

def test_basic():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

def test_decreasing():
    assert max_profit([7, 6, 4, 3, 1]) == 0

def test_empty():
    assert max_profit([]) == 0

def test_single():
    assert max_profit([5]) == 0

def test_increasing():
    assert max_profit([1, 2, 3, 4]) == 3
