# Recursion

| | |
| --- | --- |
| **Week** | 4 — Recursion, trees, heaps |
| **Topic** | Recursion |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Week 1 functions |
| **Deliverable** | `exercises/starter-code/max_depth_binary_tree.py` attempted |

## 1. Learning objectives

1. Write a base case and recursive case.
2. Trace the call stack.
3. Explain recursion depth limits.
4. Convert simple recursion to iteration.

## 2. Why this matters

Recursion models trees, graphs, backtracking, and divide-and-conquer. Interviewers check base cases and state.

## 3. Concept explanation

A recursive function calls itself on a smaller subproblem. It needs:
- Base case: stops recursion.
- Recursive case: reduces input.
- Progress: each call moves toward base case.

Python has a recursion limit (default 1000). Deep recursion may need iteration.

## 4. Worked examples

### Factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Fibonacci with memoisation
```python
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

## 5. Dry run

factorial(3):
- factorial(3) = 3 * factorial(2)
- factorial(2) = 2 * factorial(1)
- factorial(1) = 1
- returns 2, then 6.

## 6. Complexity

| Version | Time | Space |
| --- | --- | --- |
| Factorial | O(n) | O(n) stack |
| Fib naive | O(2^n) | O(n) |
| Fib memo | O(n) | O(n) |

## 7. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Missing base case | Infinite recursion | Add stopping condition |
| No progress | Stack overflow | Ensure input shrinks |
| Mutating shared state | Wrong results | Pass copies or restore |

## 8. Practice

1. Maximum depth of binary tree.
2. Same tree.
