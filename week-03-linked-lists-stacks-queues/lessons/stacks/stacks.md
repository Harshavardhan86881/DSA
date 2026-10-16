# Stacks

| | |
| --- | --- |
| **Week** | 3 — Linked lists, stacks, queues |
| **Topic** | Stacks |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Week 1 arrays |
| **Deliverable** | `exercises/starter-code/valid_parentheses.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Explain LIFO and implement a stack with a Python list.
2. Solve balanced brackets.
3. Implement a min-stack.
4. Use a monotonic stack for next greater element.

## 2. Prerequisites check

1. Can you use list append/pop? (If no, review lists.)

## 3. Why this matters

Stacks model undo, parsing, DFS, and monotonic problems. They are one of the most common interview structures.

## 4. Concept explanation

### 4.1 LIFO

Last in, first out. Python list append/pop at the end are O(1).

### 4.2 Balanced brackets

Push opens; on a close, the top must match.

### 4.3 Min stack

Keep a parallel stack of minimums.

### 4.4 Monotonic stack

Maintain increasing/decreasing values to answer "next greater/smaller" in O(n).

## 5. Worked examples

### Example 1 — Valid parentheses

```python
def is_valid(s):
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

### Example 2 — Monotonic stack

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            result[stack.pop()] = value
        stack.append(i)
    return result
```

## 6. Complexity

| Operation | Time | Space |
| --- | --- | --- |
| Push/pop/top | O(1) | O(n) |
| Valid parentheses | O(n) | O(n) |
| Next greater element | O(n) | O(n) |

## 7. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Using list.pop(0) | O(n) | Use end of list |
| Forgetting empty stack check | Crash | Check before pop |
| Wrong monotonic direction | Wrong answers | Trace small example |

## 8. Practice exercises

1. Valid Parentheses → `exercises/starter-code/valid_parentheses.py`
2. Min Stack → `exercises/starter-code/min_stack.py`
3. Next Greater Element → `exercises/starter-code/next_greater_element.py`

## 9. Hints

<details><summary>Hint 1</summary>
The stack stores unmatched opens.
</details>
