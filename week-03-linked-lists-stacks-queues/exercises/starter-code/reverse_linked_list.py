"""Starter code: Reverse a singly linked list."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    # implement here
    pass


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    print(reverse_list(head))
