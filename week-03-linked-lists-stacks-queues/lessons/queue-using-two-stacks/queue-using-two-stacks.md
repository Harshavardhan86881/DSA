# Queue Using Two Stacks

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Queue using two stacks |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Stacks, queues |
| **Deliverable** | `queue_using_stacks.py` attempted |

## 1. Learning objectives

1. Implement FIFO with two LIFO stacks.
2. Explain amortized O(1).
3. Preserve order.

## 2. Concept explanation

Use `in_stack` and `out_stack`. Enqueue pushes to in_stack. Dequeue pops from out_stack; if out_stack is empty, move all elements from in_stack to out_stack. This reverses order once, restoring FIFO.

## 3. Visual example

Enqueue 1,2,3:
- in: [1,2,3], out: []

Dequeue:
- move all: in [], out [3,2,1]
- pop out: 1
- out: [3,2]

## 4. Code

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._move()
        return self.out_stack.pop()

    def peek(self):
        self._move()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack
```

## 5. Dry run

| Operation | in_stack | out_stack | Return |
| --- | --- | --- | --- |
| push 1 | [1] | [] | - |
| push 2 | [1,2] | [] | - |
| pop | [] | [2] | 1 |
| push 3 | [3] | [2] | - |
| pop | [3] | [] | 2 |
| pop | [] | [] | 3 |

## 6. Correctness and complexity

Each element is pushed to in_stack once, moved once, popped from out_stack once. Total O(n) for n operations, so amortized O(1) per operation.

Auxiliary space: O(n).

## 7. Common mistakes

- Moving stacks on every operation.
- Forgetting to check out_stack first.
- Returning from in_stack.

## 8. Practice

### Guided exercise 1

Trace push 1,2, pop, push 3, pop, pop.

### Guided exercise 2

Why move only when out_stack empty?

### Independent exercise 1

Implement MyQueue.

### Independent exercise 2

Test empty queue.

### Debugging exercise

Fix:

```python
def pop(self):
    while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
    return self.out_stack.pop()
```

It moves every time, still correct but less efficient.

### Prediction exercise

After push 1,2, pop, pop returns?

Answer: 1 then 2.

## 9. Active-recall questions

1. When do you move elements?
2. Why is it amortized O(1)?
3. What preserves FIFO?
4. What is peek?
5. What is empty condition?

Answers:
1. When out_stack empty.
2. Each element moved once.
3. Reversal of in_stack.
4. Front element.
5. Both stacks empty.

## 10. Interview questions

**Q:** Implement queue using stacks.  
**A:** Two stacks; move all elements only when output stack is empty.

Follow-up: What is amortized complexity? O(1).

## 11. Spaced-repetition checklist

- Day 1: Draw stacks.
- Day 3: Write from memory.
- Day 7: Explain amortized.
- Day 14: Compare with deque.

## 12. Explain aloud

"Push to the in stack. When you need to dequeue, flip the in stack into the out stack once; then pop from out."
