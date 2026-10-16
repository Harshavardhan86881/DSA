# Week 2 Cumulative Assessment — Answer Key

Do not open until finished and self-graded.

## Section A — Pattern identification

1. Two pointers (sorted input, pair sum).
2. Sliding window (contiguous substring, variable size).
3. Binary search on answer (numeric answer, monotonic feasibility).
4. Binary search (sorted array, boundary).
5. Sorting (grouping by canonical key).
6. Sliding window (fixed size).
7. Binary search on answer (numeric answer, monotonic).
8. Sorting (sort by start, then merge).
9. Sliding window (contiguous subarray, variable size).
10. Binary search (sorted array, insertion position).

## Section B — Tracing binary search on [1,3,5,7,9], target 7

| Step | left | right | mid | nums[mid] | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 4 | 2 | 5 | 5 < 7 → left = 3 |
| 1 | 3 | 4 | 3 | 7 | match → return 3 |

## Section C — Complexity

1. Sliding window (variable): O(n) time, O(k) space.
2. Binary search: O(log n) time, O(1) space.
3. Binary search on answer (Koko): O(n log max_pile) time, O(1) space.
4. Sorting + scan: O(n log n) time, O(n) or O(1) space.
5. Two pointers after sorting: O(n) time (plus O(n log n) if sorting needed).

## Section D — Debugging

Bug: `left = mid` should be `left = mid + 1`. Otherwise, when `nums[mid] < target`, the
interval does not shrink (mid stays in range), causing an infinite loop.

Fixed:

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Section E — Coding

### Q1 — Two Sum Sorted

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

### Q2 — Longest Unique Substring

```python
def longest_unique_substring(s):
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best
```

### Q3 — Binary Search

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Q4 — Koko Eating Bananas

```python
def min_eating_speed(piles, h):
    def feasible(k):
        return sum((p + k - 1) // k for p in piles) <= h
    left, right = 1, max(piles)
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
```
