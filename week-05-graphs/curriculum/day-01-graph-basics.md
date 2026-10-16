# Day 1 — Graph Basics

| | |
| --- | --- |
| **Week** | 5 |
| **Theme** | Graph basics |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Weeks 1–4 |
| **Deliverable** | Build an adjacency list |

## 1. Day objectives

1. Define graph vocabulary.
2. Compare directed/undirected and weighted/unweighted.
3. Build adjacency list/matrix/edge list.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read `../lessons/graphs/graphs.md` sections 1–8. |
| Diagrams and dry runs | 35 min | Draw graphs and adjacency lists. |
| Guided implementation | 45 min | Run `../examples/graphs/bfs.py`. |
| Independent problem solving | 70 min | Build graphs from edge lists. |
| Tests and debugging | 25 min | Test isolated vertices and duplicates. |
| Active recall and spoken explanation | 25 min | Explain representations. |

## 3. Exact file links

- Lesson: [graphs.md](../lessons/graphs/graphs.md)
- Example: [bfs.py](../examples/graphs/bfs.py)
- Starter: [has_path.py](../exercises/starter-code/has_path.py)
- Solution: [has_path.py](../exercises/solutions/has_path.py)
- Problem: [has-path-in-undirected-graph.md](../problems/easy/has-path-in-undirected-graph.md)
- Tests: [test_has_path.py](../exercises/test-cases/test_has_path.py)

## 4. Implementation tasks

1. Implement `build_adjacency_list(num_nodes, edges, directed=False)`.
2. Print adjacency list and matrix for the example graph.
3. Add isolated vertices and a self-loop, then inspect the output.

## 5. Edge cases

- Empty edge list.
- Isolated vertices.
- Duplicate edges.
- Self-loop.
- Directed vs undirected interpretation.

## 6. Complexity

- Building adjacency list: O(V+E) time, O(V+E) space.
- Building adjacency matrix: O(V^2) time and space.

## 7. Common mistakes

- Forgetting to initialize all vertices.
- Adding an edge only one way in an undirected graph.
- Confusing node count with edge count.

## 8. Debugging advice

- Print `graph` after building it.
- Check that every vertex from `0` to `num_nodes - 1` exists as a key.
- Test with `num_nodes=1` and no edges.

## 9. Exit criteria

- [ ] Build adjacency list.
- [ ] Explain sparse vs dense.

## 10. Spoken explanation

"A graph has vertices and edges. An adjacency list stores neighbors for each vertex and uses O(V+E) space, so it is best for sparse graphs. An adjacency matrix uses O(V^2) space and is best for dense graphs or fast edge lookup."
