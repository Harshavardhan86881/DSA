import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from activity_selection import max_activities

def test_basic():
    assert max_activities([(1,3),(2,4),(3,5),(0,6),(5,7),(8,9)]) == 4

def test_empty():
    assert max_activities([]) == 0

def test_single():
    assert max_activities([(1,2)]) == 1

def test_back_to_back():
    assert max_activities([(1,2),(2,3)]) == 2

def test_equal_endpoints():
    assert max_activities([(1,2),(1,2)]) == 1
