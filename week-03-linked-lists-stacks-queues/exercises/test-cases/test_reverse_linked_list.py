import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from reverse_linked_list import ListNode, reverse_list

def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_basic():
    assert to_list(reverse_list(build([1, 2, 3]))) == [3, 2, 1]

def test_empty():
    assert reverse_list(None) is None

def test_single():
    assert to_list(reverse_list(build([5]))) == [5]
