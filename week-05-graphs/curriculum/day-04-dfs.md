# Day 4 — DFS

| | |
| --- | --- |
| **Week** | 5 |
| **Theme** | DFS |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 3 |
| **Deliverable** | `has-path` attempted |

## 1. Day objectives

1. Implement recursive and iterative DFS.
2. Traverse disconnected graphs.
3. Explain recursion depth risks.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read DFS section. |
| Diagrams and dry runs | 35 min | Trace call stack. |
| Guided implementation | 45 min | Run `../examples/graphs/dfs.py`. |
| Independent problem solving | 70 min | Solve has-path. |
| Tests and debugging | 25 min | Test disconnected graph. |
| Active recall and spoken explanation | 25 min | Explain DFS vs BFS. |

## 3. Exact file links

- Lesson: [graphs.md](../lessons/graphs/graphs.md)
- Example: [dfs.py](../examples/graphs/dfs.py)
- Starter: [has_path.py](../exercises/starter-code/has_path.py)
- Solution: [has_path.py](../exercises/solutions/has_path.py)
- Problem: [has-path-in-undirected-graph.md](../problems/easy/has-path-in-undirected-graph.md)
- Problem code: [has-path-in-undirected-graph.py](../problems/easy/has-path-in-undirected-graph.py)
- Tests: [test_has_path.py](../exercises/test-cases/test_has_path.py)

## 4. Implementation tasks

1. Implement recursive DFS.
2. Implement iterative DFS with a stack.
3. Compare traversal order for the same graph.

## 5. Edge cases

- Disconnected graph.
- Deep graph causing recursion limit.
- Node with no neighbors.
- Cycle in graph.

## 6. Complexity

- Recursive DFS: O(V+E) time, O(V) auxiliary space.
- Iterative DFS: O(V+E) time, O(V) space.

## 7. Common mistakes

- Forgetting base/visited checks in recursion.
- Pushing neighbors in an order that changes expected output.
- Using recursion on very deep graphs without considering limits.

## 8. Debugging advice

- Trace the call stack on a 4-node graph.
- Add prints around visited updates.
- Switch to iterative DFS if `RecursionError` appears.

## 9. Exit criteria

- [ ] DFS from memory.
- [ ] Recursive and iterative versions tested.

## 10. Spoken explanation

"DFS explores as deep as possible before backtracking. Recursive DFS uses the call stack; iterative DFS uses an explicit stack. Both need visited handling to avoid cycles."
