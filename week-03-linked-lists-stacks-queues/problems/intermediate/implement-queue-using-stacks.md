# Implement Queue using Stacks

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | queues, stacks |
| **Target time** | 25 minutes |
| **Solution file** | [implement-queue-using-stacks.py](implement-queue-using-stacks.py) |

## 1. Problem statement

Implement a FIFO queue using only two stacks.

## 2. Constraints

- At most 100 calls

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use an in-stack and an out-stack.
</details>
<details><summary>Hint 2</summary>
Move elements only when out-stack is empty.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
"""Solution: Queue using two stacks. Amortised O(1) per operation."""


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
```

## 7. Complexity analysis

Amortised O(1) per operation, O(n) space.

## 8. Edge cases and tests

See `../../exercises/test-cases/` for automated tests.

## 9. Follow-up questions

1. How would you change the approach for a very large input?
2. What is the space complexity and can it be reduced?
3. How would you test this function thoroughly?

## 10. Related problems

- `../../exercises/starter-code/queue_using_stacks.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
