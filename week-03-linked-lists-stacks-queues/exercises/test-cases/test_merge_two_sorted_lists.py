import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from merge_two_sorted_lists import ListNode, merge_two_lists

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
    assert to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]

def test_empty():
    assert to_list(merge_two_lists(None, build([1, 2]))) == [1, 2]

def test_both_empty():
    assert merge_two_lists(None, None) is None
