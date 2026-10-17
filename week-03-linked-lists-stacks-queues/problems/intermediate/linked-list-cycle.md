# Linked List Cycle

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | linked lists, two pointers |
| **Target time** | 20 minutes |
| **Solution file** | [linked-list-cycle.py](linked-list-cycle.py) |

## 1. Problem statement

Given a linked list, determine if it has a cycle.

## 2. Constraints

- `0 ≤ number of nodes ≤ 10^4`

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use fast and slow pointers.
</details>
<details><summary>Hint 2</summary>
If fast meets slow, there is a cycle.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
"""Solution: Linked List Cycle detection. O(n) time, O(1) space."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## 7. Complexity analysis

O(n) time, O(1) space.

## 8. Edge cases and tests

See `../../exercises/test-cases/` for automated tests.

## 9. Follow-up questions

1. How would you change the approach for a very large input?
2. What is the space complexity and can it be reduced?
3. How would you test this function thoroughly?

## 10. Related problems

- `../../exercises/starter-code/linked_list_cycle.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
