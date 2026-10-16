import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from search_rotated_sorted_array import search_rotated

def test_basic():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_not_found():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

def test_single():
    assert search_rotated([1], 1) == 0

def test_no_rotation():
    assert search_rotated([1, 2, 3, 4], 3) == 2
