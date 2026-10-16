import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from capacity_to_ship import ship_within_days

def test_basic():
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15

def test_single():
    assert ship_within_days([5], 1) == 5

def test_days_equals_len():
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 10

def test_one_day():
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 55
