import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from subsets import subsets

def test_basic():
    assert sorted(subsets([1,2,3])) == sorted([[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]])

def test_empty():
    assert subsets([]) == [[]]

def test_single():
    assert subsets([5]) == [[], [5]]

def test_count():
    assert len(subsets([1,2,3,4])) == 16

def test_duplicates_position_based():
    assert len(subsets([1,1])) == 4
