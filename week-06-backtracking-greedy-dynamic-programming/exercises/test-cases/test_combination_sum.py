import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from combination_sum import combination_sum

def test_basic():
    assert sorted(combination_sum([2,3,6,7],7)) == sorted([[2,2,3],[7]])

def test_none():
    assert combination_sum([2],1) == []
