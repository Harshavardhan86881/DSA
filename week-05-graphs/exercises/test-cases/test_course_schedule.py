import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from course_schedule import can_finish

def test_true():
    assert can_finish(2, [[1,0]]) is True

def test_cycle():
    assert can_finish(2, [[1,0],[0,1]]) is False

def test_none():
    assert can_finish(1, []) is True
