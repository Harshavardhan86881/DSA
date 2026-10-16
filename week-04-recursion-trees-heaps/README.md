# Week 4 — Recursion, trees, heaps

**Status: deep teaching content generated for all required Week 4 topics.**
Scope is fixed here; lessons are generated week by week after Week 1 is complete.

## 1. Learning objectives

By the end of Week 4 you can:

1. Write a recursive function with an explicit base case and a shrinking subproblem, and trace its
   call stack on paper.
2. Convert a simple recursion into an iterative version, and say which one you would choose and why.
3. Implement binary tree traversals (pre-order, in-order, post-order, level-order) both recursively
   and iteratively.
4. Insert, search and delete in a binary search tree, and explain when a BST degrades to O(n).
5. Explain heap properties, use `heapq` for min-heap operations, and solve "k largest/smallest"
   style problems with a heap instead of sorting.
6. State the complexity of tree operations in terms of both the number of nodes n and the height h.
7. Explain recursion and tree solutions aloud, including the recursion-tree shape.

## 2. Prerequisites

- Weeks 1–3 gates passed: complexity, arrays, hashing, stacks/queues, linked structures.
- Recursion is introduced from zero in this week, but comfort with functions and references is
  assumed.

## 3. Planned topics

| # | Topic | Core idea |
| --- | --- | --- |
| 1 | Recursion fundamentals | Base case, recursive case, call stack, stack depth and recursion limits |
| 2 | Recursion patterns | Factorial-style accumulation, divide and conquer, recursion on lists |
| 3 | Recursion to iteration | Manual stack replacement; tail-call style thoughts in Python |
| 4 | Binary trees | Node structure, height, depth, counting nodes |
| 5 | Traversals | Pre/in/post-order recursion, iterative traversals, level-order with a queue |
| 6 | Binary search trees | Ordering invariant, search/insert/delete, worst-case vs balanced |
| 7 | Heaps | Complete-tree shape, `heapq`, heaps as priority queues, top-k problems |
| 8 | Structure choice | When a tree or heap is the right answer instead of a dict or a sorted list |

## 4. Current deliverables

| Folder | Contents |
| --- | --- |
| `lessons/` | Recursion, recursion patterns, binary trees, binary search trees, and heaps |
| `examples/` | Runnable recursion, traversal, and heap demos |
| `exercises/` | Starter code, separated solutions, and automated tests |
| `problems/easy/`, `problems/intermediate/` | Problem statements with examples, hints, and separate solution files |
| `interview-prep/` | Week 4 interview questions and spoken answers |
| `revision/` | Revision guide, active recall, flashcards, and mistake log |
| `assessments/` | Week 4 assessment and separate answer key |
| `curriculum/` | Seven day plans, including Sunday revision and assessment |

## 5. Internal structure

```text
week-04-recursion-trees-heaps/
├── README.md
├── curriculum/
├── lessons/
│   ├── recursion/
│   └── trees/
├── examples/
├── exercises/
│   ├── starter-code/
│   ├── solutions/
│   └── test-cases/
├── problems/
│   ├── easy/
│   └── intermediate/
├── interview-prep/
├── revision/
└── assessments/
```

## 6. Exit criteria

- [ ] Every recursion written this week has an explicit base case and a stated shrinking subproblem.
- [ ] All four traversals produced from memory, recursively and (for one) iteratively.
- [ ] Tree complexity answered as both O(n) and O(height) where relevant.
- [ ] A heap solution used for at least one problem where sorting would also work, with the trade-off
      explained.
- [ ] Weekly assessment passed according to its rubric.

## 7. Related documents

- [../docs/course-overview.md](../docs/course-overview.md) — sequence and scope.
- [../docs/learning-method.md](../docs/learning-method.md) — daily routine.
- [../week-03-linked-lists-stacks-queues/README.md](../week-03-linked-lists-stacks-queues/README.md) — prerequisite week.
