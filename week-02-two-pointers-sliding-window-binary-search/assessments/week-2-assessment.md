# Week 2 Cumulative Assessment

**Time limit:** 90–120 minutes. **No notes, no internet.** Write solutions in Python 3.

## Instructions

1. Read all questions first (3 minutes).
2. Solve in order; point values are shown.
3. Write at least one test per coding question.
4. State time and space complexity for each solution.
5. Self-grade with the rubric and record your score.

## Section A — Pattern identification (20 pts, 2 pts each)

For each problem, name the likely pattern and justify in one sentence.

1. Given a sorted array, find two numbers summing to a target.
2. Find the longest substring with at most K distinct characters.
3. Find the minimum capacity to ship packages in D days.
4. Find the first occurrence of a target in a sorted array.
5. Group anagrams.
6. Find the maximum sum of any contiguous subarray of size K.
7. Find the minimum eating speed for Koko.
8. Merge overlapping intervals.
9. Find the minimum size subarray with sum ≥ target.
10. Find the insertion position of a target in a sorted array.

## Section B — Tracing (10 pts)

Trace binary search on `[1, 3, 5, 7, 9]` for target 7. Show left, right, mid, and action each step.

## Section C — Complexity (10 pts)

State and justify the complexity of:
1. Sliding window (variable).
2. Binary search.
3. Binary search on answer (Koko).
4. Sorting + scan.
5. Two pointers after sorting.

## Section D — Debugging (10 pts)

The following binary search has a bug. Identify it and fix it.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid          # BUG
        else:
            right = mid - 1
    return -1
```

## Section E — Coding (40 pts, 10 each)

1. Implement `two_sum_sorted(nums, target)` returning indices (0-based) of the pair.
2. Implement `longest_unique_substring(s)` returning the length of the longest substring with all unique characters.
3. Implement `binary_search(nums, target)` returning the index or -1.
4. Implement `min_eating_speed(piles, h)` returning the minimum speed.

## Rubric (per coding question, 10 pts)

| Criterion | Points |
| --- | --- |
| Correct on examples | 3 |
| Edge cases handled | 3 |
| Complexity stated correctly | 2 |
| Clean, readable code | 2 |

Section A: 2 pts each (1 pt pattern, 1 pt justification).
Section B: 10 pts (2 per step).
Section C: 2 pts each.
Section D: 10 pts (5 identify, 5 fix).

## Passing score

70 / 90 or higher. Below 70, repeat weak topics with R1 reviews.

## Answer key

See `answer-key.md` in this folder. Do not open until finished and self-graded.
