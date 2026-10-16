# Merge Two Sorted Lists

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | linked lists |
| **Target time** | 20 minutes |
| **Solution file** | [merge-two-sorted-lists.py](merge-two-sorted-lists.py) |

## 1. Problem statement

Merge two sorted linked lists and return the head of the merged list.

## 2. Constraints

- `0 ≤ number of nodes ≤ 50`

## 3. Examples

**Example 1**

```text
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

**Example 2 — edge case**

```text
Input: [], []
Output: []
```

## 4. Hints

<details><summary>Hint 1</summary>
Use a dummy head.
</details>
<details><summary>Hint 2</summary>
Advance the pointer with the smaller value.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
"""Solution for 'Merge Two Sorted Lists'. O(n + m) time, O(1) extra space."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 is not None else list2
    return dummy.next
```

## 7. Complexity analysis

O(n + m) time, O(1) extra space.

## 8. Edge cases and tests

See `../../exercises/test-cases/` for automated tests.

## 9. Follow-up questions

1. How would you change the approach for a very large input?
2. What is the space complexity and can it be reduced?
3. How would you test this function thoroughly?

## 10. Related problems

- `../../exercises/starter-code/merge_two_sorted_lists.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
