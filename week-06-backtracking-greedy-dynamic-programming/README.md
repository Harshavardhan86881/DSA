# Week 6 — Backtracking, Greedy, Dynamic Programming

**Status: deep teaching content complete for all required Week 6 topics.**

## 1. Learning objectives

By the end of Week 6 you can:

1. Write backtracking with choose, explore, un-choose, and safe pruning.
2. Generate subsets, permutations, and combinations, and state their counts.
3. Decide whether a greedy strategy is valid and give a counterexample when it is not.
4. Recognise overlapping subproblems and write memoised and tabulated versions.
5. Derive DP state, transition, and base case for 1-D problems.
6. Compare brute force, greedy, and DP and justify the chosen approach.
7. Explain a DP solution by stating the state meaning first.

## 2. Prerequisites

- Weeks 1–5, especially recursion and graph traversal.

## 3. Topics

| # | Topic | Core idea |
| --- | --- | --- |
| 1 | Backtracking | Choose, explore, undo |
| 2 | Subsets, permutations, combinations | Decision trees and counts |
| 3 | Pruning | Safe early rejection |
| 4 | Greedy | Local choice and proof |
| 5 | Memoisation | Top-down DP |
| 6 | Tabulation | Bottom-up DP |
| 7 | Classic DP | Climbing stairs, house robber, coin change, LIS |

## 4. Actual files

| Area | Files |
| --- | --- |
| Lessons | [lessons/backtracking/backtracking.md](lessons/backtracking/backtracking.md), [lessons/greedy/greedy.md](lessons/greedy/greedy.md), [lessons/dp/dp.md](lessons/dp/dp.md) |
| Examples | [examples/backtracking/](examples/backtracking/), [examples/greedy/](examples/greedy/), [examples/dp/](examples/dp/) |
| Starter code | [exercises/starter-code/](exercises/starter-code/) |
| Solutions | [exercises/solutions/](exercises/solutions/) |
| Tests | [exercises/test-cases/](exercises/test-cases/) |
| Problems | [problems/easy/](problems/easy/), [problems/intermediate/](problems/intermediate/) |
| Day plans | [curriculum/](curriculum/) |
| Interview prep | [interview-prep/questions.md](interview-prep/questions.md) |
| Revision | [revision/](revision/) |
| Assessment | [assessments/week-6-assessment.md](assessments/week-6-assessment.md), [assessments/answer-key.md](assessments/answer-key.md) |

## 5. Pattern to problem map

| Pattern | Problems |
| --- | --- |
| Backtracking | subsets, permutations, combination sum |
| Greedy | activity selection |
| DP | climbing stairs, house robber, coin change, longest increasing subsequence |

## 6. Exit criteria

- [ ] Backtracking solutions un-choose before returning.
- [ ] Every DP solution has a written state definition.
- [ ] At least one greedy solution has a counterexample.
- [ ] Complexity stated as states times transition cost.
- [ ] Weekly assessment passed.

## 7. Related documents

- [../docs/course-overview.md](../docs/course-overview.md)
- [../week-05-graphs/README.md](../week-05-graphs/README.md)
