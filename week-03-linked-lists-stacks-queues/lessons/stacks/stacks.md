# Stacks

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Stacks |
| **Estimated time** | Concepts 40 min + implementation 40 min |
| **Prerequisites** | Python lists |
| **Deliverable** | `valid_parentheses.py` attempted |

## 1. Learning objectives

1. Explain LIFO.
2. Implement push, pop, peek.
3. Solve balanced parentheses.
4. Implement Min Stack.

## 2. Concept explanation

A stack is last-in, first-out (LIFO). Python list append/pop at the end are O(1). Use a list as a stack.

## 3. Visual example

Push 1,2,3:

```text
[]
[1]
[1,2]
[1,2,3]
```

Pop:

```text
[1,2]
```

## 4. Balanced parentheses

Push opens. On close, top must match.

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

## 5. Min Stack

Track minimum with a parallel stack. On push, push to min stack if value <= current min. On pop, pop min stack if value == current min.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
```

## 6. Dry run: Min Stack with duplicates

Push 5,5,3,3:
- min_stack: [5,5,3,3]
Pop one 3:
- min_stack: [5,5,3]
get_min: 3. Correct.

## 7. Complexity

| Operation | Time | Space |
| --- | --- | --- |
| Push/pop/peek | O(1) | O(n) |
| Valid parentheses | O(n) | O(n) |
| Min Stack | O(1) per op | O(n) |

## 8. Common mistakes

- Using `list.pop(0)`.
- Forgetting empty stack check.
- Min stack not handling duplicates.

## 9. Practice

### Guided exercise 1

Trace valid parentheses on `"([)]"`.

### Guided exercise 2

Push 2,1,1 to Min Stack and pop.

### Independent exercise 1

Implement `is_valid`.

### Independent exercise 2

Implement Min Stack.

### Debugging exercise

Fix:

```python
def bad_min(stack):
    return min(stack)
```

Why is it O(n)?

### Prediction exercise

`is_valid("{[()]}")`?

Answer: True.

## 10. Active-recall questions

1. What is LIFO?
2. Why list end operations O(1)?
3. How does Min Stack track min?
4. Why handle duplicates with `<=`?
5. What is valid parentheses algorithm?

Answers:
1. Last in first out.
2. No shifting.
3. Parallel min stack.
4. To keep count of duplicate minima.
5. Stack matching.

## 11. Interview questions

**Q:** How do you get minimum in O(1)?
**A:** Maintain a parallel stack of minimums.

Follow-up: How to handle duplicates? Use `<=` on push and `==` on pop.

## 12. Spaced-repetition checklist

- Day 1: Draw stack.
- Day 3: Write Min Stack.
- Day 7: Explain duplicate handling.
- Day 14: Compare with heap.

## 13. Explain aloud

"A stack is a pile of plates. You add and remove from the top. Min Stack keeps a second pile of the smallest plates seen."
