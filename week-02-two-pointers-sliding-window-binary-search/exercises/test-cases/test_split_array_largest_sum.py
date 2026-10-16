import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from split_array_largest_sum import split_array

def test_basic():
    assert split_array([7, 2, 5, 10, 8], 2) == 18

def test_m_equals_n():
    assert split_array([7, 2, 5, 10, 8], 5) == 10

def test_m_one():
    assert split_array([7, 2, 5, 10, 8], 1) == 32

def test_single():
    assert split_array([5], 1) == 5
