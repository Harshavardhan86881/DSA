"""Solution: Reverse a singly linked list. O(n) time, O(1) space."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    new_head = reverse_list(head)
    vals = []
    while new_head is not None:
        vals.append(new_head.val)
        new_head = new_head.next
    print(vals)
