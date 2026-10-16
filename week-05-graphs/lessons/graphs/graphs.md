# Graphs

| | |
| --- | --- |
| **Week** | 5 — Graphs |
| **Topic** | Graphs |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Week 4 trees and queues |
| **Deliverable** | `exercises/starter-code/number_of_islands.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Define graph vocabulary.
2. Choose adjacency list vs matrix.
3. Build graphs from edge lists.
4. Implement BFS and DFS.
5. Count connected components.
6. Detect cycles in directed and undirected graphs.
7. Topologically sort a DAG.
8. Find shortest paths in unweighted graphs.

## 2. Prerequisites check

1. Can you use a dict mapping a key to a list?
2. Can you use `collections.deque`?
3. Can you write a recursive function with a visited set?

## 3. Why this matters

Graphs model connections: cities and roads, courses and prerequisites, grid cells and neighbors. Interview questions often hide a graph inside a grid, a prerequisite list, or a social network. The two core traversals, BFS and DFS, appear in almost every graph problem.

## 4. Build intuition

A graph is a set of vertices and edges. Think of vertices as rooms and edges as doors. BFS opens all doors one level at a time, so it finds the fewest doors to a target. DFS follows one corridor as far as possible before backtracking, so it is good for exploring every room.

Mental model: BFS is a queue of frontier rooms; DFS is a stack of corridors to explore.

## 5. Diagrams

Example directed graph:

```text
0 -> 1 -> 3
 \-> 2 -> 3
```

Adjacency list:

```text
0: [1, 2]
1: [3]
2: [3]
3: []
```

Grid as graph:

```text
1 1 0
1 0 0
0 0 1
```

Each land cell is connected to up/down/left/right land neighbors.

## 6. Graph fundamentals

A graph is a set of vertices and edges. Vertices are nodes; edges connect them.

- Directed: edges have direction.
- Undirected: edges are bidirectional.
- Weighted: edges have costs.
- Unweighted: all edges cost one.
- Connected: a path exists between every pair.
- Disconnected: at least one unreachable vertex.
- Cycle: a path that starts and ends at the same vertex.
- Degree: number of incident edges.
- Reachability: whether a path exists.

Examples:

- Cities and roads.
- Course prerequisites.
- Grid cells connected to neighbors.

Sparse graphs have few edges; dense graphs have many. Adjacency list is usually better for sparse graphs.

## 7. Representation

### Adjacency list

```python
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
```

Space O(V+E). Good for sparse graphs.

### Adjacency matrix

```python
matrix = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]
```

Space O(V^2). Good for dense graphs or fast edge lookup.

### Edge list

```python
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
```

## 8. Building a graph

```python
def build_adjacency_list(num_nodes, edges, directed=False):
    graph = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph
```

Handle isolated vertices by initializing all nodes. For undirected graphs, add both directions. For duplicate edges, either allow duplicates or use a set; document the policy. Self-loops add the node to its own neighbor list.

## 9. BFS

BFS uses a FIFO queue and explores level by level.

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```

Mark visited when enqueuing to avoid duplicate queue entries. BFS finds shortest paths in unweighted graphs.

Dry run for BFS on graph `0 -> 1,2; 1 -> 3; 2 -> 3`:

| Step | Queue before pop | Popped | Neighbors added | Visited |
| --- | --- | --- | --- | --- |
| 1 | [0] | 0 | 1, 2 | {0,1,2} |
| 2 | [1,2] | 1 | 3 | {0,1,2,3} |
| 3 | [2,3] | 2 | none | {0,1,2,3} |
| 4 | [3] | 3 | none | {0,1,2,3} |

### Shortest path reconstruction

```python
from collections import deque

def shortest_path(graph, start, target):
    if start == target:
        return [start]
    parent = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                if neighbor == target:
                    path = []
                    cur = target
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    path.reverse()
                    return path
                queue.append(neighbor)
    return None
```

## 10. DFS

Recursive DFS:

```python
def dfs(graph, start):
    visited = set()
    result = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return result
```

Iterative DFS:

```python
def dfs_iterative(graph, start):
    visited = set()
    result = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return result
```

Traversal order depends on neighbor order. Use iterative DFS when graphs are deep to avoid recursion limits.

Dry run for recursive DFS on graph `0 -> 1,2; 1 -> 3; 2 -> 3`:

| Call | Node | Action | Result so far |
| --- | --- | --- | --- |
| visit(0) | 0 | mark 0, recurse to 1 | [0] |
| visit(1) | 1 | mark 1, recurse to 3 | [0,1] |
| visit(3) | 3 | mark 3, no neighbors | [0,1,3] |
| return | 1 | done | [0,1,3] |
| visit(0) | 0 | recurse to 2 | [0,1,3] |
| visit(2) | 2 | mark 2, neighbor 3 visited | [0,1,3,2] |

## 11. Connected components

One traversal may not reach every vertex. Use an outer loop:

```python
def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()

    def dfs(node):
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    stack.append(neighbor)

    count = 0
    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)
    return count
```

## 12. Grid traversal

Number of islands uses DFS/BFS over a grid:

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
```

Each land cell is processed at most once. Empty, single-cell, all-water, all-land, and rectangular grids must be tested. The grid is modified in place; document this.

## 13. Cycle detection

Undirected cycle detection: DFS with parent tracking. A neighbor that is visited and not the parent indicates a cycle.

Directed cycle detection: use DFS coloring (white/gray/black) or recursion stack. A back edge to a gray node indicates a cycle.

Kahn's algorithm can also detect directed cycles: if processed count < number of nodes, a cycle exists.

## 14. Topological sorting

A topological order exists only for DAGs.

Kahn's algorithm:

1. Compute indegree.
2. Initialize queue with indegree 0 nodes.
3. Pop, append to order, decrement neighbors.
4. If neighbor indegree becomes 0, enqueue.
5. If order length != node count, cycle exists.

```python
from collections import deque

def topological_sort(num_nodes, edges):
    graph = {i: [] for i in range(num_nodes)}
    indegree = [0] * num_nodes
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != num_nodes:
        return None
    return order
```

Dry run for Kahn's algorithm on edges `(0,1),(0,2),(1,3),(2,3)`:

| Step | Queue | Popped | Indegree after update | Order |
| --- | --- | --- | --- | --- |
| 1 | [0] | 0 | [0,0,0,2] | [0] |
| 2 | [1,2] | 1 | [0,0,0,1] | [0,1] |
| 3 | [2] | 2 | [0,0,0,0] | [0,1,2] |
| 4 | [3] | 3 | [0,0,0,0] | [0,1,2,3] |

Multiple valid orders may exist.

## 15. Shortest paths and algorithm selection

BFS gives shortest paths only when edges have equal cost. For weighted graphs, Dijkstra's algorithm is needed; ordinary BFS is not correct for arbitrary weights.

Decision guide:

- Need shortest unweighted path: BFS.
- Need full exploration: DFS.
- Need components: traversal over all vertices.
- Need cycle detection: DFS state or Kahn's.
- Need ordering of dependencies: topological sort.

## 16. Complexity

| Algorithm | Time | Space |
| --- | --- | --- |
| BFS/DFS | O(V+E) | O(V) |
| Topological sort | O(V+E) | O(V+E) |
| Matrix traversal | O(V^2) | O(V^2) |

## 17. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Marking visited on pop | duplicate queue entries | mark on enqueue |
| Forgetting disconnected components | missing vertices | outer loop over all vertices |
| Using list.pop(0) | O(V) per pop | use deque |
| Claiming BFS works for weighted shortest paths | wrong distance | use Dijkstra for weights |
| Topological sort on cyclic graph | incomplete order | return None when count mismatch |
| Recursion depth on deep graphs | RecursionError | use iterative DFS |

## 18. Practice

### Guided exercise 1

Build adjacency list from edges.

### Guided exercise 2

Trace BFS on a 4-node graph.

### Independent exercise 1

Implement connected components.

### Independent exercise 2

Implement topological sort.

### Debugging exercise

Fix:

```python
def bad_bfs(graph, start):
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Prediction exercise

BFS on unweighted graph gives shortest path? Yes.

## 19. Active-recall questions

1. BFS data structure?
2. DFS data structure?
3. Visited mark when?
4. Topological sort validity?
5. Shortest unweighted path?

Answers:

1. Queue.
2. Stack/recursion.
3. On enqueue.
4. DAG only.
5. BFS.

## 20. Interview questions

**Q:** BFS vs DFS?
**A:** BFS finds shortest unweighted paths; DFS explores fully.

**Q:** Adjacency list vs matrix?
**A:** List O(V+E), matrix O(V^2).

Follow-up: When use matrix? Dense graphs or fast edge lookup.

## 21. Spaced-repetition checklist

- Day 1: Draw graph and BFS.
- Day 3: Write DFS.
- Day 7: Explain components.
- Day 14: Solve topological sort.

## 22. Explain aloud

"A graph is nodes and edges. BFS explores level by level with a queue. DFS goes deep with a stack."
