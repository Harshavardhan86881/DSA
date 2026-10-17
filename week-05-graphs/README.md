# Week 5 — Graphs

**Status: deep teaching content complete for all required Week 5 topics.**

## 1. Learning objectives

By the end of Week 5 you can:

1. Choose between an adjacency list and an adjacency matrix for a given graph size and density, and
   justify the choice with complexity.
2. Implement BFS with a queue and DFS with recursion or a stack, and explain when each is the right
   tool (shortest unweighted path vs full exploration).
3. Find connected components in an undirected graph and count them.
4. Detect cycles in undirected and directed graphs.
5. Produce a topological order for a DAG and explain why it is only defined for a DAG.
6. Compute shortest paths in unweighted graphs with BFS (and know that weighted graphs need
   Dijkstra, covered as a preview).
7. Avoid the classic graph bugs: revisiting nodes, missing the "visited" mark on enqueue, and
   recursion limits on deep graphs.
8. Explain a graph traversal aloud while drawing the graph and its frontier.

## 2. Prerequisites

- Weeks 1–4 gates passed: complexity, hashing (adjacency lists are dicts), queues, recursion.
- Ability to write comfortably with dicts of lists and sets of tuples.

## 3. Planned topics

| # | Topic | Core idea |
| --- | --- | --- |
| 1 | Graph vocabulary and representation | Nodes/edges, directed vs undirected, weighted vs unweighted, adjacency list vs matrix |
| 2 | Building graphs from input | Edge lists into adjacency structures; isolated nodes; duplicate edges |
| 3 | BFS | Queue, levels, shortest path in unweighted graphs, path reconstruction via parent pointers |
| 4 | DFS | Recursion, iterative stack variant, traversal order, forest of trees |
| 5 | Connected components | Component counting and labelling; union-find mentioned as an alternative |
| 6 | Cycle detection | Undirected (parent tracking) and directed (recursion stack / colouring) |
| 7 | Topological sort | DFS-based and Kahn's algorithm with in-degrees |
| 8 | Grids as graphs | 4-directional neighbour loops, visited marking, island-counting style problems |

## 4. Planned deliverables

| Folder | Planned contents |
| --- | --- |
| `lessons/` | Representation, BFS, DFS, components and cycles, topological sort, grid traversal |
| `examples/` | Runnable graph builders, BFS with level printing, DFS with entry/exit order, Kahn's algorithm demo, grid neighbour helper |
| `exercises/` | Complete BFS/DFS skeletons, component counter, cycle detector, topological order, fixtures and solutions |
| `problems/easy/`, `problems/intermediate/` | Full problems: number of islands, flood fill, connected components count, has-a-path, cycle detection in a directed graph, course-schedule-style topological order, shortest path in an unweighted graph |
| `interview-prep/` | Questions on BFS vs DFS, complexity in terms of V and E, visited-marking mistakes, topological sort validity, with spoken answers and a mock interview |
| `revision/` | Flashcards on traversal order and complexity, active recall, spaced-repetition schedule |
| `assessments/` | Daily quizzes, weekly assessment, answer key, rubric |

## 5. Internal structure

```text
week-05-graphs/
├── README.md
├── lessons/
├── examples/
├── exercises/
├── problems/
├── interview-prep/
├── revision/
└── assessments/
```

## 5.5 Actual files

| Area | Files |
| --- | --- |
| Lesson | [lessons/graphs/graphs.md](lessons/graphs/graphs.md) |
| Examples | [examples/graphs/bfs.py](examples/graphs/bfs.py), [examples/graphs/dfs.py](examples/graphs/dfs.py), [examples/graphs/topological_sort.py](examples/graphs/topological_sort.py) |
| Starter code | [exercises/starter-code/has_path.py](exercises/starter-code/has_path.py), [exercises/starter-code/shortest_path_unweighted.py](exercises/starter-code/shortest_path_unweighted.py), [exercises/starter-code/number_of_islands.py](exercises/starter-code/number_of_islands.py), [exercises/starter-code/connected_components.py](exercises/starter-code/connected_components.py), [exercises/starter-code/topological_sort.py](exercises/starter-code/topological_sort.py), [exercises/starter-code/course_schedule.py](exercises/starter-code/course_schedule.py) |
| Solutions | [exercises/solutions/](exercises/solutions/) |
| Tests | [exercises/test-cases/](exercises/test-cases/) |
| Problems | [problems/easy/](problems/easy/), [problems/intermediate/](problems/intermediate/) |
| Day plans | [curriculum/](curriculum/) |
| Interview prep | [interview-prep/questions.md](interview-prep/questions.md) |
| Revision | [revision/](revision/) |
| Assessment | [assessments/week-5-assessment.md](assessments/week-5-assessment.md), [assessments/answer-key.md](assessments/answer-key.md) |

## 6. Exit criteria

- [ ] BFS and DFS written from memory, both with correct visited handling.
- [ ] Complexity stated as O(V + E) for list-based traversal and O(V²) for matrix-based traversal.
- [ ] Grid and adjacency-list problems solved by converting the input first, not by ad-hoc loops.
- [ ] Topological sort implemented with both approaches, and the DAG requirement explained.
- [ ] Weekly assessment passed according to its rubric.

## 7. Related documents

- [../docs/course-overview.md](../docs/course-overview.md) — sequence and scope.
- [../docs/resources.md](../docs/resources.md) — includes cp-algorithms and VisuAlgo for graph topics.
- [../week-04-recursion-trees-heaps/README.md](../week-04-recursion-trees-heaps/README.md) — prerequisite week.
