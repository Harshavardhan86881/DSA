import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from next_greater_element import next_greater_element

def test_basic():
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

def test_empty():
    assert next_greater_element([], [1, 2]) == []

def test_subset():
    assert next_greater_element([2], [1, 2, 3]) == [3]
