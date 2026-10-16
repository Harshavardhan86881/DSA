# Recursion

Recursion solves a problem by solving smaller subproblems. Every recursive function needs a base case and a recursive case that shrinks the input.

## Key ideas
- Base case stops recursion.
- Recursive case reduces the problem.
- Call stack depth matters in Python.
- Memoisation avoids repeated work.

## Example
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```
