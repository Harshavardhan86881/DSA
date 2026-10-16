# Day 6 — Topological Sort and Shortest Paths

| | |
| --- | --- |
| **Week** | 5 |
| **Theme** | Topological sort and shortest paths |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 5 |
| **Deliverable** | `course-schedule` and `topological-sort` attempted |

## 1. Day objectives

1. Implement Kahn's algorithm.
2. Detect cycles via topological sort.
3. Explain BFS shortest paths.
4. Select graph algorithm.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read topological/shortest path sections. |
| Diagrams and dry runs | 35 min | Trace Kahn's algorithm. |
| Guided implementation | 45 min | Run `../examples/graphs/topological_sort.py`. |
| Independent problem solving | 70 min | Solve course-schedule and topological-sort. |
| Tests and debugging | 25 min | Test cyclic graph. |
| Active recall and spoken explanation | 25 min | Explain topological sort. |

## 3. Exact file links

- Lesson: [graphs.md](../lessons/graphs/graphs.md)
- Example: [topological_sort.py](../examples/graphs/topological_sort.py)
- Starter: [topological_sort.py](../exercises/starter-code/topological_sort.py)
- Starter: [course_schedule.py](../exercises/starter-code/course_schedule.py)
- Solution: [topological_sort.py](../exercises/solutions/topological_sort.py)
- Solution: [course_schedule.py](../exercises/solutions/course_schedule.py)
- Problem: [topological-sort.md](../problems/intermediate/topological-sort.md)
- Problem: [course-schedule.md](../problems/intermediate/course-schedule.md)
- Problem code: [topological-sort.py](../problems/intermediate/topological-sort.py)
- Problem code: [course-schedule.py](../problems/intermediate/course-schedule.py)
- Tests: [test_topological_sort.py](../exercises/test-cases/test_topological_sort.py)
- Tests: [test_course_schedule.py](../exercises/test-cases/test_course_schedule.py)

## 4. Implementation tasks

1. Implement `topological_sort(num_nodes, edges)` with Kahn's algorithm.
2. Implement `can_finish(num_courses, prerequisites)`.
3. Return `None` or `False` when a cycle exists.

## 5. Edge cases

- Empty graph.
- Single node.
- Disconnected DAG.
- Cyclic graph.
- Multiple valid topological orders.

## 6. Complexity

- Topological sort: O(V+E) time, O(V+E) space.
- Course schedule: O(V+E) time, O(V+E) space.

## 7. Common mistakes

- Building edges in the wrong direction for prerequisites.
- Forgetting to initialize indegree for all nodes.
- Assuming topological sort works on cyclic graphs.
- Using BFS for weighted shortest paths.

## 8. Debugging advice

- Print indegree array after construction.
- Print queue and order during Kahn's algorithm.
- Test a simple cycle: `0 -> 1 -> 0`.

## 9. Exit criteria

- [ ] Topological sort from memory.
- [ ] Cycle detection tests pass.

## 10. Spoken explanation

"Topological sort orders vertices so every edge goes from earlier to later. Kahn's algorithm repeatedly removes indegree-zero vertices. If some vertices remain, the graph has a cycle."
