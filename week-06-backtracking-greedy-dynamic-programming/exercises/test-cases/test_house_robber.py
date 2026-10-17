import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from house_robber import rob

def test_basic():
    assert rob([1,2,3,1]) == 4

def test_empty():
    assert rob([]) == 0

def test_single():
    assert rob([5]) == 5

def test_two():
    assert rob([2,7]) == 7

def test_all_zeros():
    assert rob([0,0,0]) == 0
