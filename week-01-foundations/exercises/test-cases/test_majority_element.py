import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from majority_element import majority_element

def test_basic():
    assert majority_element([3, 2, 3]) == 3

def test_none():
    assert majority_element([1, 2, 3]) is None

def test_empty():
    assert majority_element([]) is None

def test_single():
    assert majority_element([5]) == 5

def test_all_equal():
    assert majority_element([4, 4, 4]) == 4
