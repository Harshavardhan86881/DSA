# Middle of the Linked List

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | linked lists, two pointers |
| **Target time** | 15 minutes |
| **Solution file** | [middle-of-the-linked-list.py](middle-of-the-linked-list.py) |

## 1. Problem statement

Given the head of a singly linked list, return the middle node. If there are two middles, return the second.

## 2. Constraints

- `1 ≤ number of nodes ≤ 100`
- `1 ≤ Node.val ≤ 100`

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use slow and fast pointers.
</details>
<details><summary>Hint 2</summary>
Fast moves two steps, slow moves one.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
"""Solution for 'Middle of the Linked List'. O(n) time, O(1) space."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
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

- `../../exercises/starter-code/middle_of_the_linked_list.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
