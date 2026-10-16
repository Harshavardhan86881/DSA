# Course overview — 7-week Python DSA roadmap

This document defines the **scope and sequence** of the whole course: what each week covers,
why the weeks are in this order, and what "finished" means for each week.

It is a scope definition. Detailed lesson content is generated one week at a time, starting with
Week 1. Weeks 2–7 currently contain only their folder structure and scope.

## 1. Purpose

The course turns an intermediate Python programmer into someone who can:

1. Read a problem statement and turn it into a correct algorithm without help.
2. Reason about time and space complexity before writing code.
3. Implement the standard DSA patterns in clean Python.
4. Debug their own code with a repeatable routine.
5. Explain a solution out loud in simple English during an interview.

The course deliberately avoids rushing to "tricky" problems. Accuracy and explanation quality
come before speed, because that is what interviews actually measure.

## 2. Learner profile the course is designed for

| Aspect | Assumption |
| --- | --- |
| Python level | Intermediate |
| DSA level | Beginner to intermediate |
| Daily time | About 4 hours |
| Weekly rhythm | 6 learning days + 1 revision day (Sunday) |
| Budget | Free resources only |
| Main difficulties | Implementing logic independently, remembering concepts, debugging, explaining in English |

Consequences for the material:

- Every lesson assumes Python basics are known and never re-teaches them.
- Every solution is written twice: a clear brute-force version first, an optimised version second.
- Hints are always separated from solutions, so the logic is attempted before it is read.
- Dry-run tables are included, because "trace the code by hand" is the skill that fixes weak
  independent implementation.
- Every topic ends with a spoken-answer drill, because written skill does not automatically
  become interview skill.

## 3. The seven weeks

| Week | Theme | Core topics | Main deliverables |
| --- | --- | --- | --- |
| 1 | Foundations | Problem-solving method, Big-O, lists and arrays, strings, dictionaries/sets/hashing, frequency counting, brute force vs optimisation, prefix sums, testing and debugging, interview explanation technique | 6 lesson groups, runnable examples, 13 coding problems with tests, interviews and revision material, Sunday cumulative assessment |
| 2 | Two pointers, sliding window, binary search, sorting patterns | Sorted-array two pointers, fast/slow pointers, fixed and variable windows, binary search on answer, sorting as a tool | Lessons per pattern, runnable examples, problem set with tests, weekly assessment |
| 3 | Linked lists, stacks, queues | Singly/doubly linked lists, reversal, cycle detection, stacks, monotonic stack, queues and deques, applications | Lessons, implementations, problem set, weekly assessment |
| 4 | Recursion, trees, heaps | Recursion and call stack, tree traversals, binary search trees, height/balance, heaps and priority queues | Lessons, implementations, problem set, weekly assessment |
| 5 | Graphs | Adjacency lists and matrices, BFS, DFS, connected components, cycle detection, topological order, shortest path basics | Lessons, implementations, problem set, weekly assessment |
| 6 | Backtracking, greedy, dynamic programming | Choice-explore-undo, pruning, greedy vs optimal, memoisation, tabulation, classic 1-D DP | Lessons, implementations, problem set, weekly assessment |
| 7 | Revision, mock interviews, final assessment | Mixed topic practice, spaced repetition of Weeks 1–6, full mock interviews, final assessment | Revision packs, 3 mock interviews, final assessment and answer key |

Status of content:

| Week | Structure | Lesson content |
| --- | --- | --- |
| 1 | Created | Not generated yet — planned in `week-01-foundations/README.md` |
| 2–7 | Created | Not generated — topics are scoped in each week's README |

## 4. Why the weeks are in this order

Each week depends on the one before it:

- Week 1 builds the vocabulary (complexity, arrays, strings, hashing) that every later week uses.
  Two pointers and sliding window in Week 2 are only meaningful once array indexing and complexity
  are automatic.
- Weeks 3–5 are structural: linked lists, stacks, queues, trees, heaps and graphs are different
  shapes of the same idea, "organise data so the operation you repeat becomes cheap". They come
  after Week 2 because they need pointer-style thinking that two pointers introduces.
- Week 6 is the reasoning week. Backtracking, greedy and DP are hard to learn before recursion
  (Week 4) and graph traversal (Week 5) have made "explore options and undo" familiar.
- Week 7 assumes everything above and only revises, mixes and simulates.

A week should not be started until the previous week's readiness checklist passes. Partial
understanding compounds badly in DSA.

## 5. What "finished" means for a week

A week is complete when all of the following are true:

1. Every lesson's review questions are answered without notes.
2. Every exercise's starter code was attempted before reading the solution.
3. Every problem in that week's `problems/` folder was solved at least once unaided, and the
   strongest problems were re-solved a second time.
4. The mistake notebook has entries for every bug that cost more than 10 minutes.
5. The week's flashcards are answerable in under 2 seconds each.
6. The week's assessment is passed at the level described in that week's rubric.
7. At least three solutions can be explained out loud in English in under 3 minutes each.

## 6. Time structure

The four-hour day and the Sunday revision block are defined once in
[learning-method.md](learning-method.md). A week is designed as 6 learning days plus Sunday.

## 7. What this course is not

- It is not a Python tutorial. Python syntax is assumed.
- It is not a competitive-programming course. No heavy mathematics or contest tricks.
- It is not a collection of solution links. Every problem has an original explanation, a dry run
  and independently written Python code.
- It is not a seven-week plan that must be completed quickly. Depth beats speed, and repeating a
  week is expected when the readiness checklist fails.

## 8. Related documents

- [learning-method.md](learning-method.md) — how to study, recall and revise.
- [problem-solving-framework.md](problem-solving-framework.md) — the 7-step routine used for every problem.
- [complexity-cheatsheet.md](complexity-cheatsheet.md) — Big-O reference tables for Python operations.
- [resources.md](resources.md) — free, verified learning resources.
- [progress-guide.md](progress-guide.md) — how progress, readiness and grading are measured.
- [../week-01-foundations/README.md](../week-01-foundations/README.md) — Week 1 plan.
- [../templates/lesson-template.md](../templates/lesson-template.md) — the shape every lesson follows.
