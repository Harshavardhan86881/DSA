import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from first_last_occurrence import first_and_last

def test_basic():
    assert first_and_last([5, 7, 7, 8, 8, 10], 8) == [3, 4]

def test_not_found():
    assert first_and_last([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

def test_empty():
    assert first_and_last([], 0) == [-1, -1]

def test_single():
    assert first_and_last([1], 1) == [0, 0]

def test_all_same():
    assert first_and_last([2, 2, 2], 2) == [0, 2]
