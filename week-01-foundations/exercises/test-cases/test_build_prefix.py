import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from prefix_sum import build_prefix

def test_basic():
    assert build_prefix([1, 2, 3, 4]) == [0, 1, 3, 6, 10]

def test_empty():
    assert build_prefix([]) == [0]

def test_single():
    assert build_prefix([5]) == [0, 5]

def test_negatives():
    assert build_prefix([-1, 2, -3]) == [0, -1, 1, -2]
