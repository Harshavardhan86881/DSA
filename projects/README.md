# Projects

Larger, multi-step practice projects that use the patterns from the weeks you have completed.
Projects are the bridge between "I can solve a 20-line exercise" and "I can build something",
which is what junior-developer interviews and take-home assignments often test.

Nothing is implemented yet. Each project is unlocked by the weeks it depends on, and is written
after those weeks' lessons exist.

## How projects are used

- A project is **optional** but highly recommended at the end of the listed weeks.
- A project must be finished with the same discipline as a problem: written plan first, tests, and a
  complexity/design note in the README of the project folder.
- Projects must not use third-party dependencies unless the project's own README justifies them.

## Planned projects

| # | Project | Depends on | Core skills practised |
| --- | --- | --- | --- |
| 1 | **Text statistics analyser** — read a text file, report the most common words, word counts, and per-character frequencies; detect duplicate lines | Week 1 | Reading files, dictionaries, sets, frequency counting, prefix sums for per-line cumulative counts, edge-case handling |
| 2 | **Log range-sum reporter** — given a list of daily values, answer many "sum between day A and day B" queries quickly | Week 1 | Prefix sums, range queries, complexity reasoning, input parsing |
| 3 | **Contact-book / inventory manager** — add, find, update, delete records with fast lookup and sorted listing | Week 2–3 | Hashing, sorting, two pointers on sorted lists, stacks for undo |
| 4 | **Task scheduler simulator** — process tasks with priorities and dependencies | Week 3–4 | Queues, heaps, trees |
| 5 | **Route finder on a small map** — shortest path between named places | Week 5 | Graph representation, BFS, path reconstruction |
| 6 | **Resume/typist check: change counter and coin-change planner** — compare greedy vs dynamic programming on real amounts | Week 6 | Greedy, DP, memoisation, testing |

Project 1 and 2 are written in the same syntax and style a Week 1 learner can already use; they do
not require any topic beyond Week 1.

## Project folder convention (when created)

```text
projects/<project-slug>/
├── README.md      # goal, requirements, sample input/output, how to run, design notes
├── starter.py     # incomplete but runnable skeleton
├── solution.py    # complete implementation
└── tests/         # pytest-style tests, standard library only
```

Each project README must state: the problem, the input/output contract, an example, the planned
approach, the complexity of the approach, and a short "what I learned" section written after
finishing — that last section is what turns a project into interview talking points.

## Related documents

- [README.md](../README.md) — course entry point.
- [docs/course-overview.md](../docs/course-overview.md) — weeks and their topics.
- [templates/coding-problem-template.md](../templates/coding-problem-template.md) — the lighter-weight
  template used for single problems.
