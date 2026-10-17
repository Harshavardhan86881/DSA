import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from has_cycle import ListNode, has_cycle

def test_cycle():
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3)
    n1.next = n2; n2.next = n3; n3.next = n2
    assert has_cycle(n1) is True

def test_no_cycle():
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert has_cycle(head) is False

def test_empty():
    assert has_cycle(None) is False
