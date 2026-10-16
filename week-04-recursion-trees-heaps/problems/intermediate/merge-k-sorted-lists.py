"""Solution for 'Merge K Sorted Lists'.
#Merge k Sorted Lists. O(n log k) time, O(k) space."""


import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node is not None:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode()
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
