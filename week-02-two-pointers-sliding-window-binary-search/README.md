# Week 2 — Two pointers, sliding window, binary search, sorting patterns

**Status: Days 1-2 content generated (two pointers, sliding window); Days 3-7 pending.**
This week is scoped here so the folder layout and the sequence are fixed. Lessons follow the same
templates and rules as Week 1 and will be generated week by week.

## 1. Learning objectives

By the end of Week 2 you can:

1. Use two pointers on sorted arrays to replace an O(n²) search with an O(n) scan, and explain why
   the pointers never need to move backwards.
2. Use the fast/slow pointer idea for in-place filtering and cycle-style thinking.
3. Recognise a fixed-size sliding window ("size k") and a variable-size window ("longest/smallest
   with a condition") and implement both.
4. Apply binary search on a sorted array, and on an answer space where the predicate is monotonic.
5. Use sorting as a tool: when sorting first makes the rest of the algorithm simple, and what it
   costs.
6. Test pointer and window solutions against the standard edge cases (empty input, single element,
   all equal, window larger than the input).
7. Explain a window or pointer solution aloud in three parts, including why the invariant holds.

## 2. Prerequisites

- Week 1 gate passed: complexity analysis is automatic, arrays and strings are comfortable, and
  hashing patterns are solved without hints.
- Specifically: [../docs/complexity-cheatsheet.md](../docs/complexity-cheatsheet.md) should be
  answerable from memory.

## 3. Planned topics

| # | Topic | Core idea |
| --- | --- | --- |
| 1 | Two pointers on sorted arrays | One pointer at each end, move the one that can still improve the answer |
| 2 | Same-direction two pointers (read/write) | One pass that writes valid elements in place |
| 3 | Fixed-size sliding window | Add the entering element, remove the leaving element, keep a running aggregate |
| 4 | Variable-size sliding window | Grow the right edge, shrink the left edge while the condition is violated |
| 5 | Binary search on a sorted array | Halve the search space; correct bounds and termination |
| 6 | Binary search on the answer | Monotonic predicate, feasible() function, search the smallest/largest valid value |
| 7 | Sorting as a pattern | Sort then scan, sort to group, cost O(n log n) and when it is worth it |
| 8 | Pattern selection drills | Given a statement, choose the pattern and justify it in one sentence |

## 4. Planned deliverables

| Folder | Planned contents |
| --- | --- |
| `lessons/` | 5–7 lesson files, one per topic above, in the Week 1 lesson shape |
| `examples/` | Runnable scripts: pointer scans, window demos with printed state, binary search variants |
| `exercises/` | Starter code, fixtures and separated solutions for each pattern |
| `problems/easy/`, `problems/intermediate/` | Full problems: pair sums in sorted arrays, longest window without repetition (sliding window), minimum window with a condition, search in rotated sorted array, first/last occurrence, square-root-by-binary-search, merged sorted arrays, container-of-water style pointer problems |
| `interview-prep/` | Questions on invariants, off-by-one bounds, monotonicity, window correctness, plus spoken answers and one mock interview |
| `revision/` | Flashcards on pattern recognition and complexity, active-recall drills, spaced-repetition schedule |
| `assessments/` | Daily quizzes, weekly assessment, answer key, rubric |

## 5. Internal structure

```text
week-02-two-pointers-sliding-window-binary-search/
├── README.md
├── lessons/          (empty — content pending)
├── examples/         (empty)
├── exercises/        (empty)
├── problems/         (empty)
├── interview-prep/   (empty)
├── revision/         (empty)
└── assessments/      (empty)
```

Week 2 does not carry its own `curriculum/`, `progress/`, `weekly-assessment.md`-style files yet;
they are added when this week's content is generated, so that the folder contains nothing it does
not need.

## 6. Exit criteria

- [ ] Both pointer directions and both window types implemented from memory.
- [ ] Binary search written without off-by-one errors on first try, including the "no answer" case.
- [ ] Every own problem solved unaided at least once, weakest re-solved.
- [ ] Pattern chosen and justified in one sentence for each new statement encountered.
- [ ] Weekly assessment passed according to its rubric.

## 7. Related documents

- [../docs/course-overview.md](../docs/course-overview.md) — where Week 2 sits in the sequence.
- [../docs/learning-method.md](../docs/learning-method.md) — the daily 4-hour block.
- [../docs/problem-solving-framework.md](../docs/problem-solving-framework.md) — the routine to reuse.
- [../week-01-foundations/README.md](../week-01-foundations/README.md) — the prerequisite week.
