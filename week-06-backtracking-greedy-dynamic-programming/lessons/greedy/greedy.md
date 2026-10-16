# Greedy Algorithms

| | |
| --- | --- |
| **Week** | 6 |
| **Topic** | Greedy |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Sorting |
| **Deliverable** | `activity_selection.py` attempted |

## 1. Learning objectives

1. Make locally optimal choices.
2. Sort by end time for intervals.
3. Provide counterexamples.

## 2. Concept explanation

Greedy chooses the best local option. It works when greedy choice property and optimal substructure hold. Always test a counterexample.

## 3. Worked example

```python
def max_activities(intervals):
    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    count = 0
    last_end = float("-inf")
    for start, end in intervals_sorted:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```

## 4. Complexity

O(n log n) time, O(1) extra space.

## 5. Common mistakes

- Assuming greedy always works.
- Sorting by start instead of end.
- Not checking counterexamples.

## 6. Practice

1. Activity selection.
