# Week 4 — Recursion, trees, heaps

**Status: all 7 days generated (recursion, trees, heaps). Week 4 content complete.**
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

## 4. Planned deliverables

| Folder | Planned contents |
| --- | --- |
| `lessons/` | Recursion fundamentals, recursion patterns, trees and traversals, BST operations, heaps and priority queues |
| `examples/` | Runnable recursion demos with printed call order, tree class with traversals, heap-based top-k demo |
| `exercises/` | Write recursion from a description; complete tree traversal functions; heap builder; fixtures and separated solutions |
| `problems/easy/`, `problems/intermediate/` | Full problems: maximum depth of a binary tree, same-tree comparison, invert a binary tree, level-order traversal, validate a BST, kth largest element, merge-k-sorted-lists style heap problem |
| `interview-prep/` | Questions on base cases, stack overflow, recursion vs iteration, tree height bounds, heap vs sort, with spoken answers and a mock interview |
| `revision/` | Flashcards on traversal orders and complexity, active recall, spaced-repetition schedule |
| `assessments/` | Daily quizzes, weekly assessment, answer key, rubric |

## 5. Internal structure

```text
week-04-recursion-trees-heaps/
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
