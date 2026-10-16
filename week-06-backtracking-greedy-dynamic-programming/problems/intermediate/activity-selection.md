# Activity Selection

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | greedy |
| **Target time** | 20 minutes |
| **Solution file** | [activity-selection.py](activity-selection.py) |

## 1. Problem statement

Max number of non-overlapping activities.

## 2. Constraints

Reasonable input sizes.

## 3. Examples

See solution file.

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion/DP as appropriate.
</details>

## 5. Optimised approach

```python
"""Solution: Activity Selection. O(n log n) time, O(1) extra space."""


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

## 6. Complexity analysis

See solution docstring.

## 7. Edge cases and tests

See `../../exercises/test-cases/`.

## 8. Follow-up questions

1. Can you reduce space?
2. What is the time complexity?
3. How to handle duplicates?

## 9. Related problems

- `../../exercises/starter-code/activity_selection.py` — starter code.
