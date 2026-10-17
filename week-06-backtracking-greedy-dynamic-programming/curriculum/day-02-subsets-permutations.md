# Day 2 — Subsets and Permutations

| | |
| --- | --- |
| **Week** | 6 |
| **Theme** | Subsets and permutations |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 1 |
| **Deliverable** | `permutations.py` attempted |

## 1. Day objectives

1. Generate permutations.
2. Use a used array.
3. Handle duplicates conceptually.
4. State n! growth.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read backtracking lesson sections 10–12. |
| Diagrams and dry runs | 35 min | Trace permutations on `[1,2,3]`. |
| Guided implementation | 45 min | Re-type permutations example. |
| Independent problem solving | 70 min | Solve `../problems/intermediate/permutations.md`. |
| Tests and debugging | 25 min | Test single and duplicate inputs. |
| Active recall and spoken explanation | 25 min | Explain permutation count. |

## 3. Exact file links

- Lesson: [backtracking.md](../lessons/backtracking/backtracking.md)
- Starter: [permutations.py](../exercises/starter-code/permutations.py)
- Solution: [permutations.py](../exercises/solutions/permutations.py)
- Problem: [permutations.md](../problems/intermediate/permutations.md)
- Problem code: [permutations.py](../problems/intermediate/permutations.py)
- Tests: [test_permutations.py](../exercises/test-cases/test_permutations.py)

## 4. Implementation tasks

1. Implement permutations with `used`.
2. Record `path[:]`.
3. Test on `[]`, `[1]`, `[1,2,3]`.

## 5. Edge cases

- Empty input.
- One element.
- Duplicate values.
- n = 10 output size.

## 6. Complexity

- Time: O(n n!).
- Auxiliary space: O(n), excluding output.

## 7. Common mistakes

- Forgetting to mark used.
- Forgetting to unmark used.
- Storing mutable path.

## 8. Debugging advice

- Print used array.
- Trace one full permutation.
- Count results and compare with n!.

## 9. Exit criteria

- [ ] Permutations from memory.
- [ ] Tests pass.

## 10. Spoken explanation

"Permutations choose an unused element at each level. There are n! permutations, so output size dominates runtime."

## 11. Fallback if stuck

Start with subsets, then add a used array.

## 12. Next-day retrieval task

Tomorrow, write permutations without looking, then compare with the solution.
