import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from min_stack import MinStack

def test_basic():
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2

def test_single():
    s = MinStack()
    s.push(5)
    assert s.top() == 5
    assert s.get_min() == 5
