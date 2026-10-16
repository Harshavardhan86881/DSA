# Min Stack

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | stacks |
| **Target time** | 25 minutes |
| **Solution file** | [min-stack.py](min-stack.py) |

## 1. Problem statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## 2. Constraints

- `-2^31 ≤ val ≤ 2^31 - 1`
- At most 3 * 10^4 calls

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Keep a parallel min stack.
</details>
<details><summary>Hint 2</summary>
Push to min stack when value <= current min.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
"""Solution for 'Min Stack'. O(1) per operation, O(n) space."""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]
```

## 7. Complexity analysis

O(1) per operation, O(n) space.

## 8. Edge cases and tests

See `../../exercises/test-cases/` for automated tests.

## 9. Follow-up questions

1. How would you change the approach for a very large input?
2. What is the space complexity and can it be reduced?
3. How would you test this function thoroughly?

## 10. Related problems

- `../../exercises/starter-code/min_stack.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
