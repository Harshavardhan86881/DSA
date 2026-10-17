import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from maximum_subarray import max_subarray

def test_basic():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative():
    assert max_subarray([-1, -2, -3]) == -1

def test_empty():
    assert max_subarray([]) == 0

def test_single():
    assert max_subarray([5]) == 5

def test_all_positive():
    assert max_subarray([1, 2, 3]) == 6
