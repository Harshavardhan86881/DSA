# Day 2 — Building Graphs

| | |
| --- | --- |
| **Week** | 5 |
| **Theme** | Building graphs |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 1 |
| **Deliverable** | Build graphs from edge lists |

## 1. Day objectives

1. Build adjacency list/matrix/edge list.
2. Handle directed/undirected edges.
3. Handle isolated vertices and self-loops.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read representation section. |
| Diagrams and dry runs | 35 min | Draw graph and adjacency list. |
| Guided implementation | 45 min | Implement build_adjacency_list. |
| Independent problem solving | 70 min | Solve has-path. |
| Tests and debugging | 25 min | Test duplicates and isolated nodes. |
| Active recall and spoken explanation | 25 min | Explain representations. |

## 3. Exact file links

- Lesson: [graphs.md](../lessons/graphs/graphs.md)
- Starter: [has_path.py](../exercises/starter-code/has_path.py)
- Solution: [has_path.py](../exercises/solutions/has_path.py)
- Problem: [has-path-in-undirected-graph.md](../problems/easy/has-path-in-undirected-graph.md)
- Problem code: [has-path-in-undirected-graph.py](../problems/easy/has-path-in-undirected-graph.py)
- Tests: [test_has_path.py](../exercises/test-cases/test_has_path.py)

## 4. Implementation tasks

1. Write `build_adjacency_list` for directed and undirected graphs.
2. Solve `has_path` using DFS.
3. Add a test for an unreachable destination.

## 5. Edge cases

- Source equals destination.
- Disconnected graph.
- Empty graph with `n=0` or `n=1`.
- Duplicate edges.

## 6. Complexity

- Graph construction: O(V+E) time and space.
- DFS path search: O(V+E) time, O(V) space.

## 7. Common mistakes

- Marking visited after popping instead of before exploring.
- Not handling missing neighbors with `graph.get(node, [])`.
- Assuming every node appears in an edge.

## 8. Debugging advice

- Trace visited set on a small graph.
- Test `has_path(graph, 0, 0)` first.
- Print recursion or stack contents when stuck.

## 9. Exit criteria

- [ ] Build graph from edges.
- [ ] `has_path` passes tests.

## 10. Spoken explanation

"First convert edges into an adjacency list, initializing every vertex. Then DFS or BFS can explore reachable vertices. Visited handling prevents infinite loops."
