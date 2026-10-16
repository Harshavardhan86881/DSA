"""Runnable example: reverse a singly linked list iteratively and recursively."""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
    return result


def reverse_iterative(head):
    prev = None
    current = head
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    head = build([1, 2, 3, 4])
    print("original:", to_list(head))
    r1 = reverse_iterative(head)
    print("iterative:", to_list(r1))
    r2 = reverse_recursive(r1)
    print("recursive back:", to_list(r2))
