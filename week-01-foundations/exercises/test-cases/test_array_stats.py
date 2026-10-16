import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from array_stats import array_stats

def test_basic():
    assert array_stats([3, 1, 4, 1, 5]) == (1, 5, 14)

def test_empty():
    assert array_stats([]) is None

def test_single():
    assert array_stats([7]) == (7, 7, 7)

def test_negatives():
    assert array_stats([-3, 0, 2]) == (-3, 2, -1)
