import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from topological_sort import topological_sort

def test_basic():
    assert topological_sort(4, [(0,1),(0,2),(1,3),(2,3)]) == [0,1,2,3]

def test_cycle():
    assert topological_sort(2, [(0,1),(1,0)]) is None

def test_empty():
    assert topological_sort(0, []) == []
