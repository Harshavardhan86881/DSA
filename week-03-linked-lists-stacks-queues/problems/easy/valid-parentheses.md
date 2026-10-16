# Valid Parentheses

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | stacks, strings |
| **Target time** | 20 minutes |
| **Solution file** | [valid-parentheses.py](valid-parentheses.py) |

## 1. Problem statement

Given a string containing only `()[]{}`, determine if it is valid. Open brackets must be closed by the same type in the correct order.

## 2. Constraints

- `1 ≤ s.length ≤ 10^4`

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use a stack.
</details>
<details><summary>Hint 2</summary>
Push open brackets; on close, check the top.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
"""Solution for 'Valid Parentheses'. O(n) time, O(n) space."""


def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
```

## 7. Complexity analysis

O(n) time, O(n) space.

## 8. Edge cases and tests

See `../../exercises/test-cases/` for automated tests.

## 9. Follow-up questions

1. How would you change the approach for a very large input?
2. What is the space complexity and can it be reduced?
3. How would you test this function thoroughly?

## 10. Related problems

- `../../exercises/starter-code/valid_parentheses.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
