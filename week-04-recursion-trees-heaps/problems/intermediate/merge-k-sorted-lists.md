# Merge k Sorted Lists

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | heaps, linked lists |
| **Target time** | 30 minutes |
| **Solution file** | [merge-k-sorted-lists.py](merge-k-sorted-lists.py) |

## 1. Problem statement

Merge k sorted linked lists into one sorted list.

## 2. Constraints

- Reasonable input sizes (see solution).

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion or a queue/heap as appropriate.
</details>

## 5. Optimised approach

```python
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
```

## 6. Complexity analysis

See solution docstring.

## 7. Edge cases and tests

See `../../exercises/test-cases/`.

## 8. Follow-up questions

1. Can you do it iteratively?
2. What is the space complexity?
3. How does input shape affect performance?

## 9. Related problems

- `../../exercises/starter-code/merge_k_sorted_lists.py` — starter code.
