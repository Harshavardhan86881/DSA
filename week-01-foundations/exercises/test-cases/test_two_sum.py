import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from two_sum import two_sum

def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]

def test_negatives():
    assert two_sum([-1, 2, 0], 1) == [0, 1]

def test_small():
    assert two_sum([3, 2, 4], 6) == [1, 2]
