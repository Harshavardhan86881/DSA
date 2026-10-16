# Week 3 — Linked lists, stacks, queues

**Status: all 7 days generated (linked lists, stacks, queues). Week 3 content complete.**
Scope is fixed here; lessons are generated week by week after Week 1 is complete.

## 1. Learning objectives

By the end of Week 3 you can:

1. Implement a singly linked list (node, insert, delete, traverse) and explain its complexity versus
   a Python list for each operation.
2. Reverse a linked list iteratively and recursively, and detect a cycle with the fast/slow pointer
   technique.
3. Use a stack (via a list or `collections.deque`) for LIFO problems: balanced brackets, undo-like
   behaviour, and monotonic-stack problems such as "next greater element".
4. Use a queue (`collections.deque`) for FIFO problems, and explain why `list.pop(0)` is the wrong
   tool.
5. Choose between list, `deque`, stack and queue by stating the required operations and their costs.
6. Explain pointer-based code aloud, describing what happens to each reference in a diagram.

## 2. Prerequisites

- Weeks 1–2 gates passed: complexity analysis, array operations, and pointer-style thinking.
- Comfort with Python classes and `None` as a sentinel value.

## 3. Planned topics

| # | Topic | Core idea |
| --- | --- | --- |
| 1 | Nodes and references | A node holds a value and a reference to the next node |
| 2 | Singly linked list operations | Insert at head/tail, delete by value, traverse, length |
| 3 | Doubly linked lists | Two references; insert/delete in O(1) given the node |
| 4 | Reversal and cycle detection | Iterative reversal; fast/slow pointers; finding the cycle start |
| 5 | Linked-list versus Python list | Costs of each operation; when an array is the better default |
| 6 | Stacks | LIFO, list-as-stack, balanced brackets, monotonic stack |
| 7 | Queues and deques | FIFO, `collections.deque`, queue-based simulations |
| 8 | Choosing a container | Decision rule based on the operations used most often |

## 4. Planned deliverables

| Folder | Planned contents |
| --- | --- |
| `lessons/` | Lessons for nodes, linked lists, reversal/cycle detection, stacks, queues, container choice |
| `examples/` | Runnable class-based implementations with `__repr__`, traversal demos, bracket matcher, next-greater-element, queue simulation |
| `exercises/` | Starter implementations with `NotImplementedError` bodies to complete, fixtures, and separated solutions |
| `problems/easy/`, `problems/intermediate/` | Full problems: reverse a linked list, middle of a linked list, merge two sorted lists, cycle detection, valid brackets, min-stack-style structure, queue using stacks |
| `interview-prep/` | Questions on pointers, memory diagrams, complexity differences, and why `pop(0)` is slow, with spoken answers and a mock interview |
| `revision/` | Flashcards on container operations, active recall, spaced-repetition schedule |
| `assessments/` | Daily quizzes, weekly assessment, answer key, rubric |

## 5. Internal structure

```text
week-03-linked-lists-stacks-queues/
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

- [ ] Linked list insert/delete/reverse written from scratch without reference.
- [ ] Cycle detection implemented and explained with a diagram.
- [ ] Stack and queue problems solved using the right container each time.
- [ ] Complexity stated for every operation of every structure implemented this week.
- [ ] Weekly assessment passed according to its rubric.

## 7. Related documents

- [../docs/course-overview.md](../docs/course-overview.md) — sequence and scope.
- [../docs/learning-method.md](../docs/learning-method.md) — daily routine.
- [../week-02-two-pointers-sliding-window-binary-search/README.md](../week-02-two-pointers-sliding-window-binary-search/README.md) — prerequisite week.
