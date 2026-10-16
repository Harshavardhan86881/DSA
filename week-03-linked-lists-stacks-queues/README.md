# Week 3 — Linked lists, stacks, queues

**Status: deep teaching content generated for all required Week 3 topics.**
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

## 4. Current deliverables

| Folder | Contents |
| --- | --- |
| `lessons/` | Dedicated lessons for nodes, singly linked lists, iterative reversal, recursive reversal, fast/slow pointers, doubly linked lists, linked lists vs Python lists, stacks, monotonic stacks, queues, queue using two stacks, and container choice |
| `examples/` | Runnable implementations for singly linked lists, reversal, cycle detection, brackets, monotonic stack, and queues |
| `exercises/` | Starter code, separated solutions, and automated tests |
| `problems/easy/`, `problems/intermediate/` | Problem statements with examples, hints, and separate solution files |
| `interview-prep/` | Week 3 interview questions and spoken answers |
| `revision/` | Revision guide, active recall, flashcards, and mistake log |
| `assessments/` | Week 3 assessment and separate answer key |
| `curriculum/` | Seven day plans, including Sunday revision and assessment |

## 5. Internal structure

```text
week-03-linked-lists-stacks-queues/
├── README.md
├── curriculum/
├── lessons/
│   ├── nodes-and-references/
│   ├── singly-linked-lists/
│   ├── reversing-iteratively/
│   ├── reversing-recursively/
│   ├── fast-slow-pointers/
│   ├── doubly-linked-lists/
│   ├── linked-lists-vs-python-lists/
│   ├── stacks/
│   ├── monotonic-stacks/
│   ├── queues-and-deques/
│   ├── queue-using-two-stacks/
│   ├── choosing-a-container/
│   └── linked-lists/
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

- [ ] Linked list insert/delete/reverse written from scratch without reference.
- [ ] Cycle detection implemented and explained with a diagram.
- [ ] Stack and queue problems solved using the right container each time.
- [ ] Complexity stated for every operation of every structure implemented this week.
- [ ] Weekly assessment passed according to its rubric.

## 7. Related documents

- [../docs/course-overview.md](../docs/course-overview.md) — sequence and scope.
- [../docs/learning-method.md](../docs/learning-method.md) — daily routine.
- [../week-02-two-pointers-sliding-window-binary-search/README.md](../week-02-two-pointers-sliding-window-binary-search/README.md) — prerequisite week.
