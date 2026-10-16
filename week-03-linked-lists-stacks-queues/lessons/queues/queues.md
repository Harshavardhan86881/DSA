# Queues and Deques

| | |
| --- | --- |
| **Week** | 3 — Linked lists, stacks, queues |
| **Topic** | Queues and deques |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Week 1 arrays |
| **Deliverable** | `exercises/starter-code/queue_using_stacks.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Explain FIFO and implement a queue with `collections.deque`.
2. Explain why `list.pop(0)` is O(n).
3. Implement a queue using two stacks.
4. Choose between list, deque, stack, and queue.

## 2. Prerequisites check

1. Can you use collections.deque? (If no, read section 4.)

## 3. Why this matters

Queues model BFS, scheduling, and buffering. Choosing the wrong container makes an O(n) operation O(n) per call.

## 4. Concept explanation

### 4.1 FIFO

First in, first out. Use `deque.append` and `popleft`.

### 4.2 Why not list.pop(0)

Removing the first element shifts all others: O(n).

### 4.3 Queue using two stacks

Push to in-stack; move to out-stack only when out-stack is empty.

## 5. Worked examples

### Example 1 — Deque queue

```python
from collections import deque
q = deque()
q.append(1)
q.append(2)
print(q.popleft())  # 1
```

### Example 2 — Queue using stacks

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x):
        self.in_stack.append(x)
    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
```

## 6. Complexity

| Operation | Time | Space |
| --- | --- | --- |
| Deque append/popleft | O(1) | O(n) |
| Queue using stacks push | O(1) amortised | O(n) |
| Queue using stacks pop | O(1) amortised | O(n) |

## 7. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Using list.pop(0) | Slow | Use deque |
| Forgetting to move stacks | Wrong order | Move when out empty |
| Confusing stack and queue | Wrong output | State FIFO vs LIFO |

## 8. Practice exercises

1. Implement Queue using Stacks → `exercises/starter-code/queue_using_stacks.py`

## 9. Hints

<details><summary>Hint 1</summary>
Move all elements only when needed.
</details>
