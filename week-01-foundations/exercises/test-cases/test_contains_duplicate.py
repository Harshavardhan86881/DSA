import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from contains_duplicate import contains_duplicate

def test_basic():
    assert contains_duplicate([1, 2, 3, 1]) is True

def test_distinct():
    assert contains_duplicate([1, 2, 3]) is False

def test_empty():
    assert contains_duplicate([]) is False

def test_all_equal():
    assert contains_duplicate([4, 4, 4]) is True
