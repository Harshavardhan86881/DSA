# Day 6 — Tabulation and DP

| | |
| --- | --- |
| **Week** | 6 |
| **Theme** | Tabulation and DP |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 5 |
| **Deliverable** | `house_robber.py` and `longest_increasing_subsequence.py` attempted |

## 1. Day objectives

1. Convert memoization to tabulation.
2. Solve house robber.
3. Solve LIS in O(n^2).
4. Derive complexity from states and transitions.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read DP lesson sections 9–11. |
| Diagrams and dry runs | 35 min | Trace house robber and LIS. |
| Guided implementation | 45 min | Re-type house robber and LIS. |
| Independent problem solving | 70 min | Solve `../problems/intermediate/house-robber.md` and `../problems/intermediate/longest-increasing-subsequence.md`. |
| Tests and debugging | 25 min | Test empty, single, decreasing, duplicates. |
| Active recall and spoken explanation | 25 min | Explain tabulation. |

## 3. Exact file links

- Lesson: [dp.md](../lessons/dp/dp.md)
- Starter: [house_robber.py](../exercises/starter-code/house_robber.py)
- Starter: [longest_increasing_subsequence.py](../exercises/starter-code/longest_increasing_subsequence.py)
- Solution: [house_robber.py](../exercises/solutions/house_robber.py)
- Solution: [longest_increasing_subsequence.py](../exercises/solutions/longest_increasing_subsequence.py)
- Problem: [house-robber.md](../problems/intermediate/house-robber.md)
- Problem: [longest-increasing-subsequence.md](../problems/intermediate/longest-increasing-subsequence.md)
- Tests: [test_house_robber.py](../exercises/test-cases/test_house_robber.py)
- Tests: [test_longest_increasing_subsequence.py](../exercises/test-cases/test_longest_increasing_subsequence.py)

## 4. Implementation tasks

1. Implement house robber with O(1) space.
2. Implement LIS in O(n^2).
3. State why this LIS is not O(n log n).

## 5. Edge cases

- Empty list.
- Single element.
- All decreasing.
- Duplicates.
- Alternating high/low values.

## 6. Complexity

- House robber: O(n) time, O(1) space.
- LIS O(n^2): O(n^2) time, O(n) space.

## 7. Common mistakes

- Wrong fill order.
- Using `<=` instead of `<` in LIS.
- Forgetting empty input.

## 8. Debugging advice

- Print DP array.
- Test decreasing input.
- Trace one increasing subsequence.

## 9. Exit criteria

- [ ] House robber from memory.
- [ ] LIS from memory.

## 10. Spoken explanation

"Tabulation fills a table in dependency order. House robber chooses take or skip. LIS uses dp[i] as the best increasing subsequence ending at i."

## 11. Fallback if stuck

Write the O(n^2) LIS with nested loops, then optimize later.

## 12. Next-day retrieval task

Tomorrow, write house robber and LIS without looking.
