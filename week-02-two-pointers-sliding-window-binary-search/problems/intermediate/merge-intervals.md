# Merge Intervals

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | sorting, intervals |
| **Target time** | 30 minutes |
| **Solution file** | [merge-intervals.py](merge-intervals.py) |

## 1. Problem statement

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping
intervals and return the result.

## 2. Constraints

- `1 ≤ intervals.length ≤ 10^4`
- `intervals[i].length == 2`
- `0 ≤ start_i ≤ end_i ≤ 10^4`

## 3. Examples

**Example 1**

```text
Input:  [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
```

**Example 2**

```text
Input:  [[1, 4], [4, 5]]
Output: [[1, 5]]
```

**Example 3 — edge case**

```text
Input:  []
Output: []
```

## 4. Hints

<details><summary>Hint 1</summary>
Sort by start time first.
</details>
<details><summary>Hint 2</summary>
Merge if the next start ≤ current end; extend the end with max.
</details>

## 5. Brute-force approach

Compare every pair. O(n²) time.

## 6. Optimised approach

Sort by start, then merge in one pass. O(n log n) time, O(n) space.

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    merged = [intervals_sorted[0][:]]
    for start, end in intervals_sorted[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n²) | O(n) |
| Optimised | O(n log n) | O(n) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Empty | `[]` | `[]` |
| Single | `[[1, 2]]` | `[[1, 2]]` |
| Touching | `[[1, 4], [4, 5]]` | `[[1, 5]]` |
| Nested | `[[1, 10], [2, 3]]` | `[[1, 10]]` |

```python
def test_basic():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

def test_empty():
    assert merge_intervals([]) == []
```

## 9. Follow-up questions

1. What if intervals are given as (start, end) tuples?
2. How would you handle inserting a new interval into a sorted list?
3. What if you need to find the total covered length?

## 10. Related problems

- `../../exercises/starter-code/merge_intervals.py` — starter code.
- `../../lessons/sorting-patterns/sorting-as-a-pattern.md` — the full lesson.
