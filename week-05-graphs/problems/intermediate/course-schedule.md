# Course Schedule

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | graphs, topological sort |
| **Target time** | 25 minutes |
| **Solution file** | [course-schedule.py](course-schedule.py) |

## 1. Problem statement

Determine if all courses can be finished.

## 2. Constraints

Reasonable graph sizes.

## 3. Examples

See solution file.

## 4. Hints

<details><summary>Hint 1</summary>
Use adjacency list and visited set.
</details>

## 5. Optimised approach

```python
"""Solution: Course Schedule. O(V + E) time, O(V + E) space."""


from collections import deque


def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    taken = 0
    while queue:
        node = queue.popleft()
        taken += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return taken == num_courses
```

## 6. Complexity analysis

See solution docstring.

## 7. Edge cases and tests

See `../../exercises/test-cases/`.

## 8. Follow-up questions

1. How to handle disconnected graphs?
2. What if graph is large?
3. How to reconstruct path?

## 9. Related problems

- `../../exercises/starter-code/course_schedule.py` — starter code.
