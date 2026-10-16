import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from activity_selection import max_activities

def test_basic():
    assert max_activities([(1,3),(2,4),(3,5),(0,6),(5,7),(8,9)]) == 4

def test_empty():
    assert max_activities([]) == 0
