# Week 1 — Foundations

**Status: Days 1-4 content generated (problem solving, Big-O, arrays, strings); Days 5-6 and Sunday revision pending.**
The folders below are reserved and empty on purpose. The next content-generation task fills them
following [../templates/lesson-template.md](../templates/lesson-template.md) and
[../templates/coding-problem-template.md](../templates/coding-problem-template.md), with the
content rules from [../CONTRIBUTING.md](../CONTRIBUTING.md).

## 1. Learning objectives

By the end of Week 1 you can:

1. Turn a problem statement into a written plan before writing code, using the seven-step routine in
   [../docs/problem-solving-framework.md](../docs/problem-solving-framework.md).
2. State the time and space complexity of your own code, and predict from the input size whether it
   will be fast enough.
3. Use Python lists and arrays correctly, including knowing which operations are O(1) and which are
   O(n).
4. Solve string problems while respecting that Python strings are immutable.
5. Replace O(n²) nested-search logic with dictionary/set-based O(n) logic.
6. Count frequencies and detect duplicates in one pass.
7. Compute range sums in O(1) per query using prefix sums.
8. Write a test set for any solution: empty, single element, duplicates, negatives, maximum size.
9. Debug systematically instead of editing randomly.
10. Explain a solution aloud in English in the three-part shape (idea, complexity, walkthrough).

## 2. Prerequisites

- Python: functions, `for`/`while` loops, lists, dictionaries, sets, `len()`, slicing, f-strings,
  writing and running a `.py` file, reading an error traceback.
- No previous DSA knowledge is required. Every concept used is defined in the lessons.
- Tools: Python 3.11+, any editor, and a terminal. No packages to install.

## 3. Planned topics

| # | Topic | Where it will live |
| --- | --- | --- |
| 1 | Problem-solving methodology (understand, restate, hand-trace, plan, code, test, explain) | `lessons/problem-solving/` |
| 2 | Time and space complexity (Big-O, growth rates, counting loops) | `lessons/complexity/` |
| 3 | Python lists and array operations (indexing, append, insert, slicing, in-place changes) | `lessons/arrays/` |
| 4 | Strings (immutability, slicing, `join`, character iteration, palindromes) | `lessons/strings/` |
| 5 | Dictionaries, sets and hashing (membership tests, key/value modelling, hashable types) | `lessons/hashing/` |
| 6 | Frequency counting and duplicate detection (one-pass counting patterns) | `lessons/hashing/` |
| 7 | Brute force versus optimised approaches (identify the repeated work, remove it) | `lessons/problem-solving/` + all problem files |
| 8 | Prefix sums and range-sum problems (build once, answer in O(1)) | `lessons/prefix-sums/` |
| 9 | Testing, debugging and edge cases (edge-case matrix, systematic debugging routine) | integrated in every lesson + `exercises/test-cases/` |
| 10 | Interview explanation techniques (spoken three-part answer, follow-up handling) | `interview-prep/` + every lesson's interview section |

## 4. Six-day schedule plus Sunday (about 4 hours per day)

Each learning day uses the same blocks: 45 min concepts, 45 min implementing examples, 90 min
problems, 30 min active recall. The full block rules are in
[../docs/learning-method.md](../docs/learning-method.md).

| Day | Theme | Concepts (45 min) | Implementation (45 min) | Problems (90 min) | Recall (30 min) |
| --- | --- | --- | --- | --- | --- |
| 1 | Problem solving (planned: `curriculum/day-01-problem-solving.md`) | The seven-step framework, restating problems, hand-tracing | Re-implement the framework's worked example from memory | Reverse an Array; Find the Second-Largest Distinct Element | Framework steps from memory; spoken restatement of a statement |
| 2 | Big-O (planned: `curriculum/day-02-big-o.md`) | Big-O, growth rates, counting loops, Python operation costs | Implement an O(n²) and an O(n) version of the same task and compare | Running Sum of 1D Array; complexity rewrites of Day 1 solutions | Complexity table; classify 10 snippets |
| 3 | Arrays (planned: `curriculum/day-03-arrays.md`) | Indexing, append vs insert, slicing cost, in-place vs copy | Array operation micro-experiments and timing sanity checks | Two Sum; Best Time to Buy and Sell Stock | Array operation complexities; dry run of Two Sum |
| 4 | Strings (planned: `curriculum/day-04-strings.md`) | Immutability, slicing, `join`, character loops, palindromes | Palindrome checker with a manual index loop, then the slicing version | Valid Palindrome; Valid Anagram | Immutability consequences; 5 string snippets |
| 5 | Hashing (planned: `curriculum/day-05-hashing.md`) | dict/set operations, hashable keys, counting patterns | Character Frequency Counter and a duplicate detector, both in one pass | Contains Duplicate; Majority Element | Hash operation complexities; when hashing beats sorting |
| 6 | Prefix sums + practice (planned: `curriculum/day-06-prefix-sums-practice.md`) | Prefix sum construction, range queries, brute force vs prefix sums | Build a prefix-sum class and time it against repeated summing | Prefix Sum Construction; Range Sum Query – Immutable; Maximum Subarray | Mixed Week 1 recall; identify brute force vs optimised |
| Sunday | Revision (planned: `curriculum/sunday-revision.md`) | — | — | Mistake review 60 min, re-solving 75 min, retention testing 60 min, cumulative assessment 45 min, planning 15 min | Whole-week flashcards and three spoken explanations |

## 5. Planned deliverables

The next task generates all of this inside the folders that already exist:

| Folder | Planned contents |
| --- | --- |
| `curriculum/` | 7 day files: day 01–06 plus `sunday-revision.md`, each with its 4-hour block, outcomes and checklist |
| `lessons/problem-solving/`, `complexity/`, `arrays/`, `strings/`, `hashing/`, `prefix-sums/` | One lesson file per topic (6+ files), each following the lesson template: objectives, prerequisites, explanation, simple→difficult worked examples, line-by-line tables, dry runs, complexity, common mistakes, exercises, separated hints and solutions, interview applications, review questions |
| `examples/` | Small runnable scripts used by the lessons, grouped by topic folder |
| `exercises/starter-code/`, `test-cases/`, `solutions/` | Incomplete-but-runnable starters, input/expected fixtures, and complete solutions kept apart from the starters |
| `problems/easy/`, `problems/intermediate/` | 13 full problems (list in section 6) with statement, constraints, examples, graded hints, brute force, optimised solution, dry run, complexity, edge cases, tests, follow-ups |
| `interview-prep/` | At least 25 Week 1 questions with detailed answers and short spoken answers, follow-up questions, and one mock interview script |
| `revision/` | Flashcards, active-recall questions, mistake-notebook starter, spaced-repetition plan (next day, 3, 7, 14) |
| `assessments/` | Daily quizzes for Days 1–6, weekly cumulative assessment, answer key, grading rubric |
| `progress/` | Daily study tracker, Week 1 problem log, completion checklist with the readiness gate |

## 6. Planned coding problems

Each problem will include the full structure from
[../templates/coding-problem-template.md](../templates/coding-problem-template.md).

**Easy (planned for `problems/easy/`)**

| Problem | Main pattern |
| --- | --- |
| Contains Duplicate | Set membership in one pass |
| Two Sum | Hash map of complements |
| Valid Anagram | Frequency counting / sorting comparison |
| Valid Palindrome | Two-pointer or filtered comparison on a string |
| Running Sum of 1D Array | Cumulative sum inside an output list |
| Reverse an Array | Index swapping, in-place vs new list |
| Find the Second-Largest Distinct Element | Single pass with two tracked values |
| Character Frequency Counter | One-pass dict counting |
| Prefix Sum Construction | Building the prefix array |

**Intermediate (planned for `problems/intermediate/`)**

| Problem | Main pattern |
| --- | --- |
| Best Time to Buy and Sell Stock | Track the running minimum, single pass |
| Maximum Subarray | Running-sum reasoning (Kadane-style) with brute force comparison |
| Majority Element | Counting and verification, brute force vs hash map |
| Range Sum Query – Immutable | Prefix sums with a class interface |

Rules for these problems: original explanations, original Python code, brute force before the
optimised version, and no copied editorial text.

## 7. Week 1 exit criteria

- [ ] All 6 lesson topics read, annotated and recalled without notes.
- [ ] Every exercise attempted before its solution was opened.
- [ ] All 13 problems solved unaided at least once; the 4 intermediate ones re-solved once more.
- [ ] Complexity stated correctly for each solution you wrote.
- [ ] The mistake notebook has an entry for every bug that cost more than 10 minutes.
- [ ] Weeks 1 flashcards answered in under 2 seconds each.
- [ ] Three solutions explained aloud in English in under 3 minutes each.
- [ ] The Sunday cumulative assessment is passed according to its rubric.

## 8. Files and folders in this week

Present now (structure only):

```text
week-01-foundations/
├── README.md
├── curriculum/        (empty — day plans pending)
├── lessons/           (6 topic folders, empty)
├── examples/          (empty)
├── exercises/         (starter-code/, test-cases/, solutions/ — empty)
├── problems/          (easy/, intermediate/ — empty)
├── interview-prep/    (empty)
├── revision/          (empty)
├── assessments/       (empty)
└── progress/          (empty)
```

Nothing in this week is a stub file containing partial text: folders stay empty until real, complete
content is written for them, so the repository never claims work that does not exist.

## 9. Related documents

- [../README.md](../README.md) — how to use the course.
- [../docs/course-overview.md](../docs/course-overview.md) — Week 1 in the 7-week scope.
- [../docs/problem-solving-framework.md](../docs/problem-solving-framework.md) — the routine used every day.
- [../docs/complexity-cheatsheet.md](../docs/complexity-cheatsheet.md) — Day 2 and Day 3 reference.
- [../docs/resources.md](../docs/resources.md) — verified free resources for these topics.
- [../docs/progress-guide.md](../docs/progress-guide.md) — tracking and grading.
