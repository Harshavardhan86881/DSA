# Reversing a Linked List Recursively

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Recursive reversal |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Iterative reversal, recursion |
| **Deliverable** | Explain recursive reversal aloud |

## 1. Learning objectives

1. Reverse a list recursively.
2. Trace descending and returning calls.
3. Explain why `head.next.next = head` works.
4. State complexity and stack usage.

## 2. Concept explanation

Base case: if the list has 0 or 1 node, it is already reversed.

Recursive case:
1. Reverse the rest of the list.
2. Make the next node point back to the current node.
3. Set current node's next to None.

## 3. Code

```python
def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

## 4. Call stack trace

Input: `1 -> 2 -> 3`

Descending:
- reverse(1) calls reverse(2)
- reverse(2) calls reverse(3)
- reverse(3) returns 3

Returning:
- At node 2: `2.next.next = 2` makes 3 -> 2; `2.next = None`
- At node 1: `1.next.next = 1` makes 2 -> 1; `1.next = None`

Result: `3 -> 2 -> 1`.

## 5. Dry run table

| Call | head | Returns | Action |
| --- | --- | --- | --- |
| reverse(3) | 3 | 3 | base case |
| reverse(2) | 2 | 3 | 3.next=2, 2.next=None |
| reverse(1) | 1 | 3 | 2.next=1, 1.next=None |

## 6. Correctness and complexity

Time: O(n).
Auxiliary space: O(n) recursion stack.

## 7. Common mistakes

- Forgetting base case.
- Forgetting `head.next = None`.
- Returning `head` instead of `new_head`.

## 8. Practice

### Guided exercise 1

Trace recursive reversal on `1 -> 2`.

### Independent exercise 1

Write recursive reversal and test on empty list.

### Debugging exercise

Fix:

```python
def bad(head):
    if head is None:
        return None
    new_head = bad(head.next)
    head.next.next = head
    return new_head
```

### Prediction exercise

What happens if `head.next = None` is omitted?

Answer: a cycle is created.

## 9. Active-recall questions

1. What is the base case?
2. What does `head.next.next = head` do?
3. Why set `head.next = None`?
4. What is returned?
5. What is space complexity?

Answers:
1. 0 or 1 node.
2. Makes next node point back.
3. Removes forward link.
4. New head.
5. O(n).

## 10. Interview questions

**Q:** Explain recursive reversal.  
**A:** Reverse the tail first, then make the next node point back to the current node.

Follow-up: Why is iterative preferred? O(1) space.

## 11. Spaced-repetition checklist

- Day 1: Draw call stack.
- Day 3: Write from memory.
- Day 7: Explain returning phase.
- Day 14: Compare with iterative.

## 12. Explain aloud

"First reverse everything after the current node. Then make the next node point back to me, and disconnect my forward pointer."
