import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from range_sum_query import RangeSumQuery

def test_basic():
    rs = RangeSumQuery([1, 2, 3, 4])
    assert rs.query(1, 3) == 9

def test_single():
    rs = RangeSumQuery([5])
    assert rs.query(0, 0) == 5

def test_full():
    rs = RangeSumQuery([1, 2, 3, 4])
    assert rs.query(0, 3) == 10

def test_negatives():
    rs = RangeSumQuery([-1, 2, -3])
    assert rs.query(0, 2) == -2
