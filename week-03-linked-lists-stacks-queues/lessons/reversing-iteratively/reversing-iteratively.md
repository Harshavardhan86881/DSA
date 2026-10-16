# Reversing a Linked List Iteratively

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Iterative reversal |
| **Estimated time** | Concepts 40 min + implementation 40 min |
| **Prerequisites** | Singly linked lists |
| **Deliverable** | `exercises/starter-code/reverse_linked_list.py` attempted |

## 1. Learning objectives

1. Reverse a singly linked list in O(n) time and O(1) space.
2. Explain why three pointers are needed.
3. Handle empty and single-node lists.
4. Trace reference changes.

## 2. Why this matters

Reversal is a classic interview problem. It tests whether you can update references without losing data.

## 3. Concept explanation

We need to reverse the direction of every `next` arrow. Use three pointers:

- `prev`: the node already reversed.
- `current`: the node being processed.
- `nxt`: the next node to process, saved before overwriting.

Algorithm:
1. Save `nxt = current.next`.
2. Set `current.next = prev`.
3. Move `prev = current`.
4. Move `current = nxt`.

## 4. Visual example

Input: `1 -> 2 -> 3 -> None`

Step 0:
```text
prev=None, current=1, nxt=2
None <-?  1 -> 2 -> 3
```

Step 1:
```text
prev=1, current=2, nxt=3
None <- 1    2 -> 3
```

Step 2:
```text
prev=2, current=3, nxt=None
None <- 1 <- 2    3
```

Step 3:
```text
prev=3, current=None
None <- 1 <- 2 <- 3
```

Return `prev`.

## 5. Python implementation

```python
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
```

## 6. Dry run table

Input: `1 -> 2 -> 3`

| Iteration | prev before | current before | nxt | current.next after | prev after | current after |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | None | 1 | 2 | None | 1 | 2 |
| 2 | 1 | 2 | 3 | 1 | 2 | 3 |
| 3 | 2 | 3 | None | 2 | 3 | None |

Loop ends. Return 3. New list: `3 -> 2 -> 1`.

## 7. Correctness and complexity

Precondition: `head` is None or a valid chain ending in None.

Result: returns the new head of the reversed list.

Time: O(n), one pass.
Auxiliary space: O(1), only three pointers.

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Not saving nxt | Lose rest of list | Save before overwrite |
| Returning current | Returns None | Return prev |
| Moving prev before setting next | Wrong links | Set next first |

## 9. Practice

### Guided exercise 1

Trace reversal on `4 -> 5`.

### Guided exercise 2

Predict the new head for `1 -> 2 -> 3 -> 4`.

### Independent exercise 1

Reverse a list and return its length too.

### Independent exercise 2

Reverse only the first k nodes.

### Debugging exercise

Fix:

```python
def bad_reverse(head):
    prev = None
    current = head
    while current is not None:
        current.next = prev
        prev = current
        current = current.next
    return prev
```

Explain the bug.

### Prediction exercise

Input `1 -> 2`. What is returned?

Answer: node with value 2.

## 10. Active-recall questions

1. Why save `nxt` first?
2. What does `prev` represent?
3. What is returned?
4. What is time complexity?
5. What is auxiliary space?

Answers:
1. To avoid losing the rest.
2. Reversed prefix.
3. New head.
4. O(n).
5. O(1).

## 11. Interview questions

**Q:** Reverse a linked list.  
**A:** Use prev/current/next; O(n) time, O(1) space.

Follow-up: Can you do it recursively? Yes, but O(n) stack space.

## 12. Spaced-repetition checklist

- Day 1: Draw pointer updates.
- Day 3: Write from memory.
- Day 7: Explain why nxt is saved.
- Day 14: Compare iterative and recursive.

## 13. Explain aloud

"Save the next node, reverse the current arrow, then move all three pointers forward."
