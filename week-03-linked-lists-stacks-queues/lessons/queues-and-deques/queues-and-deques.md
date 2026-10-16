# Queues and Deques

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Queues and deques |
| **Estimated time** | Concepts 40 min + implementation 40 min |
| **Prerequisites** | Python lists |
| **Deliverable** | `queue_using_stacks.py` attempted |

## 1. Learning objectives

1. Explain FIFO.
2. Use collections.deque.
3. Explain why list.pop(0) is O(n).
4. Implement queue operations.

## 2. Concept explanation

A queue is first-in, first-out (FIFO). Use `collections.deque` for O(1) append and popleft. `list.pop(0)` shifts all elements, so it is O(n).

## 3. Visual example

Enqueue 1,2,3:
```text
[1,2,3]
```
Dequeue:
```text
[2,3]
```

## 4. Code

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            raise IndexError("empty queue")
        return self.items.popleft()

    def peek(self):
        if not self.items:
            raise IndexError("empty queue")
        return self.items[0]

    def is_empty(self):
        return not self.items
```

## 5. Dry run

| Operation | items after |
| --- | --- |
| enqueue 1 | [1] |
| enqueue 2 | [1,2] |
| dequeue | [2] |
| peek | [2] |

## 6. Complexity

| Operation | Time |
| --- | --- |
| enqueue | O(1) |
| dequeue | O(1) amortized |
| peek | O(1) |

## 7. Common mistakes

- Using list.pop(0).
- Forgetting empty check.
- Confusing queue with stack.

## 8. Practice

### Guided exercise 1

Trace queue with enqueue 1,2 and dequeue.

### Guided exercise 2

Explain why deque is faster.

### Independent exercise 1

Implement Queue class.

### Independent exercise 2

Simulate BFS queue.

### Debugging exercise

Fix:

```python
class BadQueue:
    def __init__(self):
        self.items = []
    def dequeue(self):
        return self.items.pop(0)
```

### Prediction exercise

After enqueue 1,2 and dequeue, front?

Answer: 2.

## 9. Active-recall questions

1. What is FIFO?
2. Why list.pop(0) O(n)?
3. deque append complexity?
4. deque popleft complexity?
5. When use queue?

Answers:
1. First in first out.
2. Shifts elements.
3. O(1).
4. O(1) amortized.
5. BFS, scheduling.

## 10. Interview questions

**Q:** Why not use list for queue?  
**A:** pop(0) is O(n); deque popleft is O(1).

Follow-up: What is deque implemented as? Doubly linked list of blocks.

## 11. Spaced-repetition checklist

- Day 1: Draw queue.
- Day 3: Write Queue class.
- Day 7: Explain list.pop(0).
- Day 14: Compare with stack.

## 12. Explain aloud

"A queue is a line. People join at the back and leave from the front."
