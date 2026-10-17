import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from kth_largest_element import find_kth_largest

def test_basic():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

def test_single():
    assert find_kth_largest([1], 1) == 1

def test_duplicates():
    assert find_kth_largest([3, 3, 3], 2) == 3
