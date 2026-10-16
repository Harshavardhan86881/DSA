"""Runnable example: detect a cycle and find its start using fast/slow pointers."""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def cycle_start(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == "__main__":
    # Build 1 -> 2 -> 3 -> 4 -> 2 (cycle)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    print("has cycle:", has_cycle(n1))
    start = cycle_start(n1)
    print("cycle start value:", start.value if start else None)

    # No cycle
    a = Node(1, Node(2, Node(3)))
    print("has cycle:", has_cycle(a))
