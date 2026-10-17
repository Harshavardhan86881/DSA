import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "exercises" / "solutions"))
from middle_of_linked_list import ListNode, middle_node

def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head

def test_odd():
    assert middle_node(build([1, 2, 3, 4, 5])).val == 3

def test_even():
    assert middle_node(build([1, 2, 3, 4])).val == 3

def test_single():
    assert middle_node(build([1])).val == 1
