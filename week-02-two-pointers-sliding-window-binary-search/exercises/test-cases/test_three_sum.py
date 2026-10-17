import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from three_sum import three_sum

def test_basic():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted([sorted(t) for t in result]) == sorted([[-1, -1, 2], [-1, 0, 1]])

def test_empty():
    assert three_sum([]) == []

def test_no_triplet():
    assert three_sum([1, 2, 3]) == []
