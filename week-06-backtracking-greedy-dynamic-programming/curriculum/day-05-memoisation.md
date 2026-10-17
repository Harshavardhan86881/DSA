# Day 5 — Memoisation

| | |
| --- | --- |
| **Week** | 6 |
| **Theme** | Memoisation |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 4 |
| **Deliverable** | `climbing_stairs.py` attempted |

## 1. Day objectives

1. Identify overlapping subproblems.
2. Write top-down DP with memoization.
3. Define state meaning.
4. Explain cache correctness.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read `../lessons/dp/dp.md` sections 1–8. |
| Diagrams and dry runs | 35 min | Trace climbing stairs recursion tree. |
| Guided implementation | 45 min | Run `../examples/dp/climbing_stairs.py`. |
| Independent problem solving | 70 min | Solve `../problems/easy/climbing-stairs.md` and `../problems/intermediate/coin-change.md`. |
| Tests and debugging | 25 min | Test base cases and impossible amounts. |
| Active recall and spoken explanation | 25 min | Explain memoization. |

## 3. Exact file links

- Lesson: [dp.md](../lessons/dp/dp.md)
- Example: [climbing_stairs.py](../examples/dp/climbing_stairs.py)
- Starter: [climbing_stairs.py](../exercises/starter-code/climbing_stairs.py)
- Starter: [coin_change.py](../exercises/starter-code/coin_change.py)
- Solution: [climbing_stairs.py](../exercises/solutions/climbing_stairs.py)
- Solution: [coin_change.py](../exercises/solutions/coin_change.py)
- Problem: [climbing-stairs.md](../problems/easy/climbing-stairs.md)
- Problem: [coin-change.md](../problems/intermediate/coin-change.md)
- Tests: [test_climbing_stairs.py](../exercises/test-cases/test_climbing_stairs.py)
- Tests: [test_coin_change.py](../exercises/test-cases/test_coin_change.py)

## 4. Implementation tasks

1. Implement climbing stairs iteratively.
2. Implement coin change with tabulation.
3. Write a memoized version of climbing stairs.

## 5. Edge cases

- n = 0.
- Negative n.
- Amount 0.
- Impossible amount.
- Duplicate coins.

## 6. Complexity

- Climbing stairs: O(n) time, O(1) space.
- Coin change: O(amount * coins) time, O(amount) space.

## 7. Common mistakes

- Wrong base cases.
- Forgetting impossible case.
- Vague state definition.

## 8. Debugging advice

- Print DP table.
- Test n=0 and amount=0.
- Trace a 3-4 element example.

## 9. Exit criteria

- [ ] Memoized climbing stairs.
- [ ] Coin change tests pass.

## 10. Spoken explanation

"Memoization is top-down DP. I recurse, cache each state, and reuse it. The state must capture everything relevant to the answer."

## 11. Fallback if stuck

Write brute-force recursion first, then add a dictionary cache.

## 12. Next-day retrieval task

Tomorrow, write coin change from memory.
