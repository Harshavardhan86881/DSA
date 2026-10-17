import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from minimum_size_subarray_sum import min_subarray_len

def test_basic():
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2

def test_none():
    assert min_subarray_len(100, [1, 2, 3]) == 0

def test_single():
    assert min_subarray_len(4, [1, 4, 4]) == 1

def test_whole_array():
    assert min_subarray_len(10, [1, 2, 3, 4]) == 4
