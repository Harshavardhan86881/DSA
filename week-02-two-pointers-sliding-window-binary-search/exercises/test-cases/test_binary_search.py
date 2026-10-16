import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from binary_search import binary_search

def test_basic():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_not_found():
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

def test_empty():
    assert binary_search([], 5) == -1

def test_single():
    assert binary_search([5], 5) == 0

def test_first():
    assert binary_search([-1, 0, 3], -1) == 0
