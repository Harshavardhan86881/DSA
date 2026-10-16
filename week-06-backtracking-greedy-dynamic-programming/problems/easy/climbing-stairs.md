# Climbing Stairs

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | dynamic programming |
| **Target time** | 15 minutes |
| **Solution file** | [climbing-stairs.py](climbing-stairs.py) |

## 1. Problem statement

You are climbing a staircase with `n` steps. Each move, you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.

Function contract: `climb_stairs(n: int) -> int`, where `n >= 0`.

## 2. Constraints

- `0 <= n <= 45`
- `n` is an integer.

## 3. Examples

Input: `n = 2`
Output: `2`
Explanation: 1+1, 2.

Input: `n = 3`
Output: `3`
Explanation: 1+1+1, 1+2, 2+1.

## 4. Hints

<details><summary>Hint 1</summary>
The last move is either 1 step or 2 steps.
</details>

<details><summary>Hint 2</summary>
This gives `ways(n) = ways(n-1) + ways(n-2)`.
</details>

## 5. Brute-force approach

A naive recursion tries both final moves and recomputes the same subproblems many times. This is exponential.

## 6. Optimised approach

Use dynamic programming. Define `dp[i]` as the number of ways to reach stair `i`. Then `dp[i] = dp[i-1] + dp[i-2]`, with `dp[0] = dp[1] = 1`. Optimize space to two variables.

Important code lines:

- `if n <= 1: return 1`: base cases.
- `prev2, prev1 = 1, 1`: previous two states.
- `cur = prev1 + prev2`: recurrence.
- `prev2, prev1 = prev1, cur`: shift state.

## 7. Complexity analysis

- Time: O(n).
- Auxiliary space: O(1).

## 8. Edge cases and tests

- `n = 0` returns 1 by the empty-path convention.
- `n = 1` returns 1.
- Negative input is invalid and raises `ValueError`.

## 9. Common mistakes

- Returning 0 for `n = 0`.
- Using Fibonacci indexing incorrectly.
- Forgetting base cases.

## 10. Follow-up questions

1. How would you handle 3-step moves?
2. Can you write the memoized version?
3. How does the recurrence change with different step sizes?

## 11. Related problems

- `../../exercises/starter-code/climbing_stairs.py` — starter code.
- `../../exercises/solutions/climbing_stairs.py` — solution.
- `../../exercises/test-cases/test_climbing_stairs.py` — tests.
- `../../lessons/dp/dp.md` — lesson.
