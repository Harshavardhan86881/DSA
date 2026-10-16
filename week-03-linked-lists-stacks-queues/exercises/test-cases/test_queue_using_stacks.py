import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from queue_using_stacks import MyQueue

def test_basic():
    q = MyQueue()
    q.push(1); q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False

def test_empty():
    q = MyQueue()
    assert q.empty() is True
