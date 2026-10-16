# Week 6 — Backtracking, greedy, dynamic programming

**Status: structure ready; lesson content NOT generated.**
Scope is fixed here; lessons are generated week by week after Week 1 is complete.

## 1. Learning objectives

By the end of Week 6 you can:

1. Write a backtracking solution with the three-part shape: choose, explore, un-choose, and add
   pruning when the search space is too large.
2. Generate subsets, permutations and combinations systematically, and state how many there are.
3. Decide whether a greedy strategy is valid for a problem, and give a counterexample when it is not.
4. Recognise overlapping subproblems and write both a memoised recursion and an iterative
   bottom-up version of the same solution.
5. Derive a DP state, transition and base case for 1-D problems, and state the complexity in terms
   of the state count and transition cost.
6. Compare brute force, greedy and DP on the same problem and justify the chosen approach.
7. Explain a DP solution aloud by stating the state meaning before writing any code.

## 2. Prerequisites

- Weeks 1–5 gates passed, especially recursion (Week 4) and traversal reasoning (Week 5).
- Comfort with lists of lists and passing/undoing state.

## 3. Planned topics

| # | Topic | Core idea |
| --- | --- | --- |
| 1 | Backtracking template | Choose, recurse, undo; explicit "path" and "choices" |
| 2 | Subsets, permutations, combinations | Decision trees, counting results, duplicate handling |
| 3 | Pruning | Reject partial solutions early; when pruning changes the complexity |
| 4 | Greedy algorithms | Local choice, exchange-argument intuition, counterexamples |
| 5 | Greedy vs DP | Coin change and interval problems as the classic contrast |
| 6 | Memoisation | Top-down DP: cache on the state, recursion depth, `functools.lru_cache` |
| 7 | Tabulation | Bottom-up DP: base rows first, filling order, space optimisation |
| 8 | Classic 1-D DP problems | Climbing stairs, house robber, coin change, longest increasing subsequence (preview) |

## 4. Planned deliverables

| Folder | Planned contents |
| --- | --- |
| `lessons/` | Backtracking template, subsets/permutations, pruning, greedy fundamentals, memoisation, tabulation |
| `examples/` | Runnable decision-tree printer, subset generator, greedy counterexample demo, memoised vs tabulated comparison |
| `exercises/` | Complete a backtracking template, convert recursion to DP, greedy validity checks, fixtures and solutions |
| `problems/easy/`, `problems/intermediate/` | Full problems: subsets, permutation generation, combination sum with pruning, activity-selection style greedy, climbing stairs, house robber, coin change, longest increasing subsequence |
| `interview-prep/` | Questions on state definition, complexity of DP, greedy proof sketches, pruning, recursion limits, with spoken answers and a mock interview |
| `revision/` | Flashcards on DP state shapes and complexities, active recall, spaced-repetition schedule |
| `assessments/` | Daily quizzes, weekly assessment, answer key, rubric |

## 5. Internal structure

```text
week-06-backtracking-greedy-dynamic-programming/
├── README.md
├── lessons/          (empty — content pending)
├── examples/         (empty)
├── exercises/        (empty)
├── problems/         (empty)
├── interview-prep/   (empty)
├── revision/         (empty)
└── assessments/      (empty)
```

## 6. Exit criteria

- [ ] Backtracking solutions always un-choose state before returning.
- [ ] Every DP solution is preceded by a written state definition and transition.
- [ ] At least one greedy solution is accompanied by a counterexample for a greedy that fails.
- [ ] Complexity of every DP solution stated as states × transition cost.
- [ ] Weekly assessment passed according to its rubric.

## 7. Related documents

- [../docs/course-overview.md](../docs/course-overview.md) — sequence and scope.
- [../docs/complexity-cheatsheet.md](../docs/complexity-cheatsheet.md) — needed for DP complexity statements.
- [../week-05-graphs/README.md](../week-05-graphs/README.md) — prerequisite week.
