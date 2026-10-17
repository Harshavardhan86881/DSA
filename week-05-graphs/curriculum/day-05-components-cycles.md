# Day 5 — Components and Cycles

| | |
| --- | --- |
| **Week** | 5 |
| **Theme** | Components and cycles |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 4 |
| **Deliverable** | `number-of-islands` and `count-connected-components` attempted |

## 1. Day objectives

1. Count connected components.
2. Traverse grids.
3. Detect cycles.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read components/cycles sections. |
| Diagrams and dry runs | 35 min | Trace grid DFS. |
| Guided implementation | 45 min | Re-type number_of_islands. |
| Independent problem solving | 70 min | Solve number-of-islands and count-connected-components. |
| Tests and debugging | 25 min | Test empty/all-water/all-land grids. |
| Active recall and spoken explanation | 25 min | Explain components. |

## 3. Exact file links

- Lesson: [graphs.md](../lessons/graphs/graphs.md)
- Starter: [number_of_islands.py](../exercises/starter-code/number_of_islands.py)
- Starter: [connected_components.py](../exercises/starter-code/connected_components.py)
- Solution: [number_of_islands.py](../exercises/solutions/number_of_islands.py)
- Solution: [connected_components.py](../exercises/solutions/connected_components.py)
- Problem: [number-of-islands.md](../problems/intermediate/number-of-islands.md)
- Problem: [count-connected-components.md](../problems/intermediate/count-connected-components.md)
- Problem code: [number-of-islands.py](../problems/intermediate/number-of-islands.py)
- Problem code: [count-connected-components.py](../problems/intermediate/count-connected-components.py)
- Tests: [test_number_of_islands.py](../exercises/test-cases/test_number_of_islands.py)
- Tests: [test_connected_components.py](../exercises/test-cases/test_connected_components.py)

## 4. Implementation tasks

1. Implement `count_components(n, edges)`.
2. Implement `num_islands(grid)`.
3. Detect a cycle in an undirected graph using parent tracking.

## 5. Edge cases

- Empty grid.
- All water.
- All land.
- Single cell.
- Rectangular grid.
- Disconnected graph with isolated vertices.
- Graph with a self-loop.

## 6. Complexity

- Connected components: O(V+E) time, O(V+E) space.
- Number of islands: O(m*n) time, O(m*n) space in worst case.

## 7. Common mistakes

- Mutating grid without documenting it.
- Forgetting bounds checks in grid DFS.
- Counting a component before traversal completes.
- Treating a visited parent as a cycle in undirected graphs.

## 8. Debugging advice

- Print grid before and after traversal.
- Test 1x1 grids.
- Test a graph with one node and no edges.
- Trace parent tracking on a triangle.

## 9. Exit criteria

- [ ] Components from memory.
- [ ] Grid and component tests pass.

## 10. Spoken explanation

"Components require an outer loop because one traversal only reaches one component. A grid is a graph where cells are vertices and adjacent land cells are edges. Cycle detection depends on whether the graph is directed or undirected."
