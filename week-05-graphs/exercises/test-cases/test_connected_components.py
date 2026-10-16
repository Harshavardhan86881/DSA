import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from connected_components import count_components

def test_basic():
    assert count_components(5, [[0,1],[1,2],[3,4]]) == 2

def test_none():
    assert count_components(3, []) == 3

def test_single():
    assert count_components(1, []) == 1
