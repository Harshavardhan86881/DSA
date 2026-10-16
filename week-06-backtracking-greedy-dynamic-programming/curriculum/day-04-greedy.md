# Day 4 — Greedy

| | |
| --- | --- |
| **Week** | 6 |
| **Theme** | Greedy |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 3 |
| **Deliverable** | `activity_selection.py` attempted |

## 1. Day objectives

1. Explain greedy-choice property.
2. Sort intervals by finish time.
3. Provide a greedy counterexample.
4. Test a greedy rule.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read `../lessons/greedy/greedy.md` sections 1–8. |
| Diagrams and dry runs | 35 min | Compare sort by start, duration, finish. |
| Guided implementation | 45 min | Run `../examples/greedy/activity_selection.py`. |
| Independent problem solving | 70 min | Solve `../problems/intermediate/activity-selection.md`. |
| Tests and debugging | 25 min | Test equal endpoints and empty input. |
| Active recall and spoken explanation | 25 min | Explain exchange argument. |

## 3. Exact file links

- Lesson: [greedy.md](../lessons/greedy/greedy.md)
- Example: [activity_selection.py](../examples/greedy/activity_selection.py)
- Starter: [activity_selection.py](../exercises/starter-code/activity_selection.py)
- Solution: [activity_selection.py](../exercises/solutions/activity_selection.py)
- Problem: [activity-selection.md](../problems/intermediate/activity-selection.md)
- Problem code: [activity-selection.py](../problems/intermediate/activity-selection.py)
- Tests: [test_activity_selection.py](../exercises/test-cases/test_activity_selection.py)

## 4. Implementation tasks

1. Implement activity selection.
2. Use `start >= last_end`.
3. Find a greedy counterexample for coin change.

## 5. Edge cases

- Empty intervals.
- One activity.
- Equal start/end times.
- Nested intervals.
- Back-to-back activities.

## 6. Complexity

- Time: O(n log n).
- Extra space: O(1) if sorting in place.

## 7. Common mistakes

- Sorting by start time.
- Using `>` instead of `>=`.
- Assuming greedy works without proof.

## 8. Debugging advice

- Print sorted intervals.
- Print selected intervals.
- Compare with brute force on small random inputs.

## 9. Exit criteria

- [ ] Activity selection from memory.
- [ ] Counterexample explained.

## 10. Spoken explanation

"Greedy picks the locally best option. For intervals, sorting by finish time leaves the most room, and an exchange argument shows it is safe."

## 11. Fallback if stuck

Try all three sort keys by hand on one example.

## 12. Next-day retrieval task

Tomorrow, implement activity selection and find one greedy counterexample.
