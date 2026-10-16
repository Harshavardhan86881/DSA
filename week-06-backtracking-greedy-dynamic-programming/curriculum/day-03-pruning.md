# Day 3 — Pruning

| | |
| --- | --- |
| **Week** | 6 |
| **Theme** | Pruning |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 2 |
| **Deliverable** | `combination_sum.py` attempted |

## 1. Day objectives

1. Distinguish generating from rejecting candidates.
2. Add safe pruning to combination sum.
3. Explain why pruning is not guaranteed worst-case improvement.
4. Trace explored and pruned branches.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read backtracking lesson section 14 and combination sum. |
| Diagrams and dry runs | 35 min | Trace combination sum for target 7. |
| Guided implementation | 45 min | Re-type combination sum. |
| Independent problem solving | 70 min | Solve `../problems/intermediate/combination-sum.md`. |
| Tests and debugging | 25 min | Test no solution and target 0. |
| Active recall and spoken explanation | 25 min | Explain safe pruning. |

## 3. Exact file links

- Lesson: [backtracking.md](../lessons/backtracking/backtracking.md)
- Starter: [combination_sum.py](../exercises/starter-code/combination_sum.py)
- Solution: [combination_sum.py](../exercises/solutions/combination_sum.py)
- Problem: [combination-sum.md](../problems/intermediate/combination-sum.md)
- Problem code: [combination-sum.py](../problems/intermediate/combination-sum.py)
- Tests: [test_combination_sum.py](../exercises/test-cases/test_combination_sum.py)

## 4. Implementation tasks

1. Implement combination sum with reuse.
2. Add `remaining < 0` pruning.
3. Sort candidates to enable pruning when appropriate.
4. Test target 0 and impossible target.

## 5. Edge cases

- Empty candidates.
- Target 0.
- Target smaller than smallest candidate.
- Duplicate candidates.
- Large target.

## 6. Complexity

- Worst case: O(n^(target/min)) without effective pruning.
- Pruning improves practical runtime but not guaranteed worst-case asymptotic complexity.

## 7. Common mistakes

- Pruning a valid branch.
- Assuming pruning always improves big-O.
- Forgetting to sort before pruning by candidate size.

## 8. Debugging advice

- Print remaining and current path.
- Trace a case where a branch is pruned.
- Test a counterexample for unsafe pruning.

## 9. Exit criteria

- [ ] Combination sum from memory.
- [ ] Pruning explained.

## 10. Spoken explanation

"Pruning rejects a partial candidate early. The condition must be logically safe; otherwise a valid answer can be lost. Sorting can enable pruning but does not guarantee better worst-case complexity."

## 11. Fallback if stuck

Remove pruning, get correct results first, then add one pruning condition and test.

## 12. Next-day retrieval task

Tomorrow, implement combination sum with and without pruning.
