import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from two_sum_sorted import two_sum_sorted

def test_basic():
    assert two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]

def test_negatives():
    assert two_sum_sorted([-1, 0], -1) == [0, 1]

def test_duplicates():
    assert two_sum_sorted([1, 1, 2], 2) == [0, 1]

def test_not_found():
    assert two_sum_sorted([1, 2, 3], 100) == [-1, -1]
