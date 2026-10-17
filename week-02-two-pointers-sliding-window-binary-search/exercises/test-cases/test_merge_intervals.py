import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from merge_intervals import merge_intervals

def test_basic():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

def test_empty():
    assert merge_intervals([]) == []

def test_touching():
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]

def test_nested():
    assert merge_intervals([[1, 10], [2, 3]]) == [[1, 10]]
