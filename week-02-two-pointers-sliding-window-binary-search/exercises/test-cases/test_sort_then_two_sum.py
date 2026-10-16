import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from sort_then_two_sum import has_pair_sum

def test_true():
    assert has_pair_sum([3, 2, 4], 6) is True

def test_false():
    assert has_pair_sum([3, 2, 4], 10) is False

def test_empty():
    assert has_pair_sum([], 0) is False

def test_duplicates():
    assert has_pair_sum([2, 2, 3], 4) is True
