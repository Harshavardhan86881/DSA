# Fast and Slow Pointers

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Fast and slow pointers |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Linked lists, cycle detection |
| **Deliverable** | `has_cycle.py` attempted |

## 1. Learning objectives

1. Find the middle of a list.
2. Detect a cycle.
3. Find a cycle's start.
4. Explain why fast/slow works.

## 2. Concept explanation

Use two pointers:
- `slow` moves one step.
- `fast` moves two steps.

If there is a cycle, fast and slow eventually meet. If fast reaches None, there is no cycle.

To find the middle, when fast reaches the end, slow is at the middle.

To find cycle start, after meeting, reset slow to head and move both one step; they meet at the start.

## 3. Middle of list

```python
def middle_node(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
```

## 4. Cycle detection

```python
def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## 5. Find cycle start

```python
def cycle_start(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow
```

## 6. Dry run: middle of 1->2->3->4

| Step | slow | fast |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | None (end) |

Slow at 3, which is the middle (second middle for even length).

## 7. Correctness and complexity

Time: O(n).
Auxiliary space: O(1).

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Wrong loop condition | Crash or wrong middle | Check fast and fast.next |
| Resetting wrong pointer | Wrong cycle start | Reset slow to head |
| Infinite loop | Hang | Ensure fast advances two steps |

## 9. Practice

### Guided exercise 1

Find middle of `1 -> 2 -> 3 -> 4 -> 5`.

### Guided exercise 2

Detect cycle in `1 -> 2 -> 3 -> 2`.

### Independent exercise 1

Implement `has_cycle` and test self-loop.

### Independent exercise 2

Find cycle start.

### Debugging exercise

Fix:

```python
def bad_middle(head):
    slow = fast = head
    while fast is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Prediction exercise

List `1 -> 2 -> 3 -> 4`. Middle?

Answer: 3.

## 10. Active-recall questions

1. How many steps does slow move?
2. How many steps does fast move?
3. What indicates a cycle?
4. How to find cycle start?
5. What is complexity?

Answers:
1. One.
2. Two.
3. slow == fast.
4. Reset slow to head, move both one step.
5. O(n) time, O(1) space.

## 11. Interview questions

**Q:** How do you detect a cycle?  
**A:** Fast and slow pointers; if they meet, there is a cycle.

Follow-up: How to find the start? Reset one pointer to head.

## 12. Spaced-repetition checklist

- Day 1: Draw fast/slow.
- Day 3: Write has_cycle.
- Day 7: Explain cycle start proof.
- Day 14: Solve middle without code.

## 13. Explain aloud

"Slow walks one step, fast runs two. If fast laps slow, there is a cycle. To find the start, send slow back to the beginning and walk both one step."
