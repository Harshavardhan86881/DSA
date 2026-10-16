import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from remove_duplicates import remove_duplicates

def test_basic():
    data = [1, 1, 2]
    assert remove_duplicates(data) == 2
    assert data[:2] == [1, 2]

def test_empty():
    assert remove_duplicates([]) == 0

def test_all_equal():
    data = [4, 4, 4]
    assert remove_duplicates(data) == 1

def test_already_unique():
    data = [1, 2, 3]
    assert remove_duplicates(data) == 3
