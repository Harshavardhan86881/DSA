import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from coin_change import coin_change

def test_basic():
    assert coin_change([1,2,5], 11) == 3

def test_none():
    assert coin_change([2], 3) == -1

def test_zero():
    assert coin_change([1,2,5], 0) == 0

def test_duplicates():
    assert coin_change([1,1,2], 4) == 2

def test_greedy_counterexample_system():
    assert coin_change([1,3,4], 6) == 2
