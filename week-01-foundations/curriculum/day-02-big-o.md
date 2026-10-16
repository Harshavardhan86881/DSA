# Day 2 — Big-O Complexity

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Theme** | Time and space complexity |
| **Estimated time** | 4 hours (45 + 45 + 90 + 30) |
| **Prerequisites** | Day 1 problem-solving routine; Python loops and lists |
| **Deliverable** | `exercises/starter-code/running_sum.py` attempted; complexity rewrites of Day 1 solutions |

## 1. Day objectives

By the end of today you can:

1. Explain Big-O, Big-Theta and Big-Omega at a beginner level.
2. Classify growth as constant, logarithmic, linear, linearithmic, quadratic or exponential.
3. Distinguish best, average and worst cases.
4. Separate time complexity from space complexity.
5. Count loops correctly and drop constant factors.
6. Compare a brute-force and an improved version of the same task.
7. State the complexity of common Python operations from the cheatsheet.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Concepts (45 min) | Read `lessons/complexity/big-o-complexity.md` sections 1–8. |
| Guided implementation (45 min) | Run `examples/complexity/growth_comparison.py` and `counting_loops.py`; modify n and observe. |
| Problem solving (90 min) | Solve `problems/easy/running-sum-of-1d-array.md`; rewrite Day 1 solutions with explicit complexity comments. |
| Active recall (30 min) | Complexity table flashcards; classify 10 snippets. |

## 3. Concepts to learn

- What Big-O measures and what it ignores (constants, small inputs).
- Big-O (upper bound), Big-Omega (lower bound), Big-Theta (tight bound).
- Growth rates and the table of operations per second.
- Best / average / worst case, with hashing stated as average O(1).
- Time vs space; extra space excludes the input.
- Counting loops: single, nested, halving, fixed inner count.
- Python operation costs: list, string, dict, set.
- Amortised complexity (list append).

## 4. Guided implementation

1. Run `examples/complexity/growth_comparison.py` with n = 10, 100, 1000. Record the times.
2. Predict which growth wins for n = 10⁶ before running.
3. Run `examples/complexity/counting_loops.py` and match each snippet to its class.
4. Rewrite your Day 1 reverse-array solution to avoid O(n) extra space; state the trade-off.

## 5. Problems for today

1. `problems/easy/running-sum-of-1d-array.md` — target time 15 minutes.
2. Complexity rewrite of `reverse-an-array` and `find-the-second-largest-distinct-element`.

## 6. Practice exercises (starter code)

- `exercises/starter-code/running_sum.py`
- `exercises/starter-code/complexity_rewrite.py`

## 7. Active recall checklist

- [ ] Define Big-O, Big-Theta, Big-Omega in one sentence each.
- [ ] Name the six growth classes in increasing order.
- [ ] State the complexity of `x in list`, `x in set`, `lst.append`, `lst.insert(0, x)`.
- [ ] Explain why `s = s + c` in a loop is quadratic.
- [ ] Give the constraint-to-complexity link for n = 5,000.

## 8. Common mistakes today

- Reporting the complexity of the code instead of the worst case.
- Counting the input as extra space.
- Forgetting that dict lookups are average, not worst-case, O(1).
- Ignoring `sorted()` cost inside a loop.

## 9. Exit criteria for Day 2

- [ ] Running sum solved and tested.
- [ ] Day 1 solutions rewritten with complexity comments.
- [ ] Complexity table flashcards answered in under 2 seconds.
- [ ] 10 snippets classified correctly.
