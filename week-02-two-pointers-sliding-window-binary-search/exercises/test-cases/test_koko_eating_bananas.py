import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from koko_eating_bananas import min_eating_speed

def test_basic():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4

def test_large_h():
    assert min_eating_speed([3, 6, 7, 11], 100) == 1

def test_single():
    assert min_eating_speed([5], 1) == 5

def test_all_equal():
    assert min_eating_speed([4, 4, 4], 3) == 4
