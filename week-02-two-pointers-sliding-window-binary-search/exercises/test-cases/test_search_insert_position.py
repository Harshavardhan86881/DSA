import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from search_insert_position import search_insert

def test_present():
    assert search_insert([1, 3, 5, 6], 5) == 2

def test_insert():
    assert search_insert([1, 3, 5, 6], 2) == 1

def test_end():
    assert search_insert([1, 3, 5, 6], 7) == 4

def test_empty():
    assert search_insert([], 5) == 0
