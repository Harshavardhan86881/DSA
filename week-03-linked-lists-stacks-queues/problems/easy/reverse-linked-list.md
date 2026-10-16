# Reverse Linked List

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | linked lists |
| **Target time** | 20 minutes |
| **Solution file** | [reverse-linked-list.py](reverse-linked-list.py) |

## 1. Problem statement

Given the head of a singly linked list, reverse the list and return the new head.

## 2. Constraints

- `0 ≤ number of nodes ≤ 5000`
- `-5000 ≤ Node.val ≤ 5000`

## 3. Examples

**Example 1**

```text
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
```

**Example 2 — edge case**

```text
Input: []
Output: []
```

## 4. Hints

<details><summary>Hint 1</summary>
Use three pointers: prev, current, next.
</details>
<details><summary>Hint 2</summary>
Update current.next before moving forward.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
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

- `../../exercises/starter-code/reverse_linked_list.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
