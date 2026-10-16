# Day 1 — Backtracking

| | |
| --- | --- |
| **Week** | 6 |
| **Theme** | Backtracking |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Weeks 1–5, especially recursion |
| **Deliverable** | `subsets.py` attempted |

## 1. Day objectives

1. Explain choose, explore, undo.
2. Generate subsets.
3. Explain why path must be copied.
4. Trace a recursion tree.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read `../lessons/backtracking/backtracking.md` sections 1–8. |
| Diagrams and dry runs | 35 min | Trace subsets on `[1,2]`. |
| Guided implementation | 45 min | Run `../examples/backtracking/subsets.py`. |
| Independent problem solving | 70 min | Solve `../problems/intermediate/subsets.md`. |
| Tests and debugging | 25 min | Test empty and duplicate inputs. |
| Active recall and spoken explanation | 25 min | Explain backtracking aloud. |

## 3. Exact file links

- Lesson: [backtracking.md](../lessons/backtracking/backtracking.md)
- Example: [subsets.py](../examples/backtracking/subsets.py)
- Starter: [subsets.py](../exercises/starter-code/subsets.py)
- Solution: [subsets.py](../exercises/solutions/subsets.py)
- Problem: [subsets.md](../problems/intermediate/subsets.md)
- Problem code: [subsets.py](../problems/intermediate/subsets.py)
- Tests: [test_subsets.py](../exercises/test-cases/test_subsets.py)

## 4. Implementation tasks

1. Implement subsets with choose/explore/undo.
2. Record `path[:]`, not `path`.
3. Test on `[]`, `[1]`, and `[1,2,3]`.

## 5. Edge cases

- Empty input.
- One element.
- Duplicate values.
- Large input causing 2^n output.

## 6. Complexity

- Time: O(n 2^n).
- Auxiliary space: O(n), excluding output.

## 7. Common mistakes

- Forgetting `path.pop()`.
- Storing a mutable reference.
- Reusing the same index.

## 8. Debugging advice

- Print path at the start of backtrack.
- Check append/pop pairs.
- Count results and compare with 2^n.

## 9. Exit criteria

- [ ] Subsets from memory.
- [ ] Tests pass.

## 10. Spoken explanation

"Backtracking explores choices depth-first. I choose an element, recurse, then undo so the next choice starts clean. I copy the path when recording."

## 11. Fallback if stuck

Re-read sections 6 and 9, then retype the example without looking.

## 12. Next-day retrieval task

Tomorrow, write subsets from memory before reading the lesson.
