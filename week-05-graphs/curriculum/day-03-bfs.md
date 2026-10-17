# Day 3 — BFS

| | |
| --- | --- |
| **Week** | 5 |
| **Theme** | BFS |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 2 |
| **Deliverable** | `shortest-path-in-unweighted-graph.md` attempted |

## 1. Day objectives

1. Implement BFS with deque.
2. Mark visited on enqueue.
3. Reconstruct shortest path.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read BFS section. |
| Diagrams and dry runs | 35 min | Trace queue and visited set. |
| Guided implementation | 45 min | Run `../examples/graphs/bfs.py`. |
| Independent problem solving | 70 min | Solve shortest-path-in-unweighted-graph. |
| Tests and debugging | 25 min | Test unreachable target. |
| Active recall and spoken explanation | 25 min | Explain BFS shortest path. |

## 3. Exact file links

- Lesson: [graphs.md](../lessons/graphs/graphs.md)
- Example: [bfs.py](../examples/graphs/bfs.py)
- Starter: [shortest_path_unweighted.py](../exercises/starter-code/shortest_path_unweighted.py)
- Solution: [shortest_path_unweighted.py](../exercises/solutions/shortest_path_unweighted.py)
- Problem: [shortest-path-in-unweighted-graph.md](../problems/intermediate/shortest-path-in-unweighted-graph.md)
- Problem code: [shortest-path-in-unweighted-graph.py](../problems/intermediate/shortest-path-in-unweighted-graph.py)
- Tests: [test_shortest_path_unweighted.py](../exercises/test-cases/test_shortest_path_unweighted.py)

## 4. Implementation tasks

1. Implement `bfs(graph, start)` returning reachable vertices.
2. Implement `shortest_path(graph, start, target)` returning distance or path.
3. Reconstruct the path using parent pointers.

## 5. Edge cases

- Start equals target.
- Unreachable target.
- Disconnected graph.
- Empty graph.
- Duplicate edges in adjacency list.

## 6. Complexity

- BFS traversal: O(V+E) time, O(V) space.
- Shortest path with parent map: O(V+E) time, O(V) space.

## 7. Common mistakes

- Marking visited when popping.
- Using `list.pop(0)` instead of `deque.popleft`.
- Claiming BFS gives shortest weighted paths.

## 8. Debugging advice

- Print queue contents after each pop.
- Verify visited is updated before appending.
- Test a graph where target is unreachable.

## 9. Exit criteria

- [ ] BFS from memory.
- [ ] Shortest path tests pass.

## 10. Spoken explanation

"BFS uses a queue and marks visited on enqueue. Because it explores level by level, the first time it reaches a node in an unweighted graph is along a shortest path."
