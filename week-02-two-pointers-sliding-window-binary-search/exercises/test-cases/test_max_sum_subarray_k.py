import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from max_sum_subarray_k import max_sum_subarray_k

def test_basic():
    assert max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9

def test_k_equals_n():
    assert max_sum_subarray_k([1, 2, 3], 3) == 6

def test_k_one():
    assert max_sum_subarray_k([5], 1) == 5

def test_k_too_large():
    assert max_sum_subarray_k([1, 2, 3], 5) == 0
