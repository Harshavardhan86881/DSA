import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from permutations import permute

def test_basic():
    assert sorted(permute([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

def test_single():
    assert permute([1]) == [[1]]

def test_empty():
    assert permute([]) == [[]]

def test_count():
    assert len(permute([1,2,3,4])) == 24

def test_duplicates_position_based():
    assert len(permute([1,1])) == 2
