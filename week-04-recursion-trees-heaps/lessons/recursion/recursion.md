# Recursion

| | |
| --- | --- |
| **Week** | 4 — Recursion, trees, heaps |
| **Topic** | Recursion |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Python functions, conditionals, loops |
| **Deliverable** | `exercises/starter-code/max_depth_binary_tree.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Explain recursion in plain English.
2. Identify base case, recursive case, and progress.
3. Trace a recursive call stack.
4. Explain return order.
5. Convert a simple recursion to iteration.
6. Debug infinite recursion.

## 2. Why this matters

Recursion appears in trees, graphs, backtracking, divide-and-conquer, and dynamic programming. Interviewers often ask you to trace the call stack.

## 3. Build intuition

Recursion is a function calling itself on a smaller problem. Every recursive function needs:

- Base case: stop.
- Recursive case: reduce the problem.
- Progress: each call moves toward the base case.

Analogy: Russian nesting dolls. You open one doll, find a smaller doll, repeat until the smallest doll. The analogy stops being accurate because functions also return values back up the chain.

## 4. How Python executes recursion

Each call creates a stack frame containing parameters and local variables. Frames are pushed when a call starts and popped when it returns. Return values travel back to the caller.

## 5. Worked examples

### Factorial

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case
```

Dry run for `factorial(3)`:

| Call | n | Next call | Returns |
| --- | --- | --- | --- |
| factorial(3) | 3 | factorial(2) | 6 |
| factorial(2) | 2 | factorial(1) | 2 |
| factorial(1) | 1 | none | 1 |

Descending: 3 -> 2 -> 1. Returning: 1 -> 2 -> 6.

### Fibonacci naive

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Time O(2^n), space O(n). It recomputes many values.

### Fibonacci memoized

```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

Time O(n), space O(n).

## 6. Recursion on lists

```python
def sum_list(nums):
    if not nums:
        return 0
    return nums[0] + sum_list(nums[1:])
```

This is O(n) time but O(n) auxiliary space due to slicing and stack. An iterative version uses O(1) auxiliary space.

## 7. Divide and conquer

Break a problem into independent subproblems, solve them, and combine. Example: merge sort. Recursion helps when subproblems are smaller versions of the same problem.

## 8. Complexity

| Version | Time | Auxiliary space |
| --- | --- | --- |
| Factorial | O(n) | O(n) |
| Fib naive | O(2^n) | O(n) |
| Fib memo | O(n) | O(n) |
| List sum recursive | O(n) | O(n) |

Auxiliary space excludes input storage.

## 9. Recursion limits

Python's default recursion limit is 1000. Deep recursion can raise `RecursionError`. Use iteration or increase the limit carefully with `sys.setrecursionlimit`.

## 10. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Missing base case | Infinite recursion | Add stopping condition |
| No progress | Stack overflow | Ensure input shrinks |
| Wrong return value | Incorrect result | Trace returning phase |
| Mutating shared state | Wrong results | Restore state or pass copies |

## 11. Recursive vs iterative

Choose recursion when the problem is naturally recursive (trees, DFS). Choose iteration when depth is large or performance matters. Iteration uses an explicit stack and avoids recursion limits.

## 12. Practice

### Guided exercise 1

Trace `factorial(4)`.

### Guided exercise 2

Explain why naive Fibonacci is slow.

### Independent exercise 1

Write `power(base, exp)` recursively.

### Independent exercise 2

Write `reverse_string(s)` recursively.

### Debugging exercise

Fix:

```python
def bad_factorial(n):
    if n == 0:
        return 0
    return n * bad_factorial(n - 1)
```

### Prediction exercise

What does `sum_list([1,2,3])` return?

Answer: 6.

## 13. Active-recall questions

1. What is a base case?
2. What is progress?
3. What is a stack frame?
4. Why is naive Fibonacci slow?
5. When choose iteration?

Answers:
1. Stopping condition.
2. Each call moves toward base case.
3. Function call's local state.
4. Repeated subproblems.
5. Large depth or performance.

## 14. Interview questions

**Q:** What is recursion?
**A:** A function solving a problem by calling itself on a smaller subproblem, with a base case to stop.

**Q:** Why can recursion cause stack overflow?
**A:** Each call uses stack space; deep chains exceed the limit.

Follow-up: How to avoid? Use iteration or memoization.

## 15. Spaced-repetition checklist

- Day 1: Trace factorial.
- Day 3: Write fib_memo.
- Day 7: Explain stack frames.
- Day 14: Convert recursion to iteration.

## 16. Explain aloud

"Recursion breaks a problem into smaller copies of itself. The base case stops it, and values return back up the call stack."
