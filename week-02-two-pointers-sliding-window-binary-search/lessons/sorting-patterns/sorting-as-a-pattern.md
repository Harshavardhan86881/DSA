# Sorting as a Problem-Solving Pattern

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Topic** | Sorting as a pattern |
| **Estimated time** | Concepts 45 min + implementation 40 min |
| **Prerequisites** | Week 1 arrays and complexity; Week 2 two pointers |
| **Deliverable** | `exercises/starter-code/sort_then_two_sum.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Explain why sorting can simplify a problem.
2. Use `sorted()` vs `.sort()` correctly.
3. Sort with `key`, `reverse`, tuples, and custom keys.
4. Detect duplicates after sorting.
5. Solve Two Sum via sorting + two pointers.
6. State the O(n log n) + O(n) complexity.

## 2. Prerequisites check

1. Can you sort a list in Python? (If no, review lists.)
2. Do you know what "stable sort" means? (If no, read section 4.3.)
3. Have you completed Week 2 Days 1–4? (If no, read those first.)

## 3. Why this matters

Sorting is not just "arrange numbers"; it is a preprocessing step that unlocks other patterns.
Once data is sorted, duplicates become adjacent, two pointers work, binary search applies, and
greedy choices become safe. The cost is O(n log n), so sorting is worth it when it reduces an
O(n²) or O(n³) algorithm to O(n log n) or O(n). The skill is deciding when sorting helps and
when it wastes time.

## 4. Concept explanation

### 4.1 What sorting is

Sorting arranges elements in a defined order (ascending by default). Python uses Timsort, a
stable, adaptive, O(n log n) sort.

### 4.2 `sorted()` vs `.sort()`

- `sorted(iterable)` returns a **new** list; the original is unchanged. O(n) extra space.
- `list.sort()` sorts **in place**; returns `None`. O(1) extra space (apart from Timsort's
  temporary arrays).

Choose based on whether you need the original order.

### 4.3 Stable sorting

A stable sort preserves the relative order of equal elements. Python's sort is stable. This
matters when sorting records by one field while keeping a previous order for ties.

### 4.4 Custom keys

`key` is a function applied to each element to determine sort order. Common patterns:

- `key=len` — sort strings by length.
- `key=lambda x: x[1]` — sort by second element.
- `key=lambda x: (x[0], -x[1])` — sort by first ascending, second descending.
- Tuples sort lexicographically: `(a, b)` compares `a` first, then `b`.

### 4.5 Sorting enables

- **Duplicate detection:** after sorting, duplicates are adjacent → one pass.
- **Two pointers:** sorted array enables opposite-direction pointers.
- **Grouping:** equal elements become contiguous.
- **Interval processing:** sort by start time, then merge.
- **Greedy decisions:** sort to process in a beneficial order.

### 4.6 Complexity

- Sorting: O(n log n) time, O(n) space for `sorted()`, O(1) extra for `.sort()` (plus
  Timsort temporaries).
- Sort + linear scan: O(n log n) dominates.
- If you only need min/max, sorting is overkill (O(n) with a scan).

### 4.7 Preserving original order

If you need the original indices after sorting, sort pairs `(value, index)` or use
`sorted(range(n), key=lambda i: nums[i])`.

## 5. Worked examples (simple → difficult)

### Example 1 — Detect duplicates after sorting (simple)

```python
def has_duplicate_sorted(nums: list[int]) -> bool:
    nums_sorted = sorted(nums)
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1]:
            return True
    return False


if __name__ == "__main__":
    print(has_duplicate_sorted([1, 2, 3, 1]))  # True
    print(has_duplicate_sorted([1, 2, 3]))      # False
```

**Line-by-line explanation**

| Line | What happens | Why |
| --- | --- | --- |
| `sorted(nums)` | New sorted list | Original preserved |
| `for i in range(1, len(...))` | Scan adjacent pairs | Duplicates become adjacent |
| `if nums_sorted[i] == nums_sorted[i-1]` | Adjacent equal? | Duplicate found |

### Example 2 — Two Sum via sorting + two pointers (moderate)

```python
def two_sum_sorted_values(nums: list[int], target: int) -> bool:
    nums_sorted = sorted(nums)
    left, right = 0, len(nums_sorted) - 1
    while left < right:
        s = nums_sorted[left] + nums_sorted[right]
        if s == target:
            return True
        if s < target:
            left += 1
        else:
            right -= 1
    return False


if __name__ == "__main__":
    print(two_sum_sorted_values([3, 2, 4], 6))  # True
    print(two_sum_sorted_values([3, 2, 4], 10)) # False
```

Note: this returns whether a pair exists, not indices. If you need indices, sort pairs with
original indices.

### Example 3 — Group anagrams (moderate)

```python
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

### Example 4 — Merge intervals (harder)

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    merged = [intervals_sorted[0]]
    for start, end in intervals_sorted[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # [[1, 6], [8, 10], [15, 18]]
```

## 6. Dry-run table

Trace merge_intervals on `[[1,3],[2,6],[8,10],[15,18]]`.

| Step | Current interval | `merged` after | Note |
| --- | --- | --- | --- |
| 0 | — | [[1,3]] | seed |
| 1 | [2,6] | [[1,6]] | overlaps, extend |
| 2 | [8,10] | [[1,6],[8,10]] | no overlap, append |
| 3 | [15,18] | [[1,6],[8,10],[15,18]] | no overlap, append |

## 7. Complexity

| Operation | Time | Space | Notes |
| --- | --- | --- | --- |
| `sorted()` / `.sort()` | O(n log n) | O(n) / O(1) | Timsort |
| Sort + linear scan | O(n log n) | O(n) or O(1) | Sort dominates |
| Custom key sort | O(n log n * key cost) | O(n) | Key computed per element |
| Duplicate detection after sort | O(n log n) | O(n) or O(1) | Sort dominates |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Sorting when a linear scan suffices | Slower than needed | Check if min/max/scan works |
| Mutating input unexpectedly | Caller's data changed | Use `sorted()` or copy first |
| Assuming unstable sort | Wrong tie order | Python sort is stable |
| Forgetting sort cost in complexity | Underestimated time | State O(n log n) |
| Losing original indices | Cannot map back | Sort pairs with indices |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Sort then two sum** — check if any pair sums to target after sorting → `exercises/starter-code/sort_then_two_sum.py`
2. **Group anagrams** — group words that are anagrams → `exercises/starter-code/group_anagrams.py`
3. **Merge intervals** — merge overlapping intervals → `exercises/starter-code/merge_intervals.py`

## 10. Hints

<details><summary>Hint 1 — for exercise 1</summary>
Sort, then use two pointers. State whether you need indices or just existence.
</details>
<details><summary>Hint 2 — for exercise 2</summary>
The sorted characters of a word form a canonical key for its anagram group.
</details>
<details><summary>Hint 3 — for exercise 3</summary>
Sort by start time, then merge if the next start ≤ current end.
</details>

## 11. Solutions

- `exercises/solutions/sort_then_two_sum.py`
- `exercises/solutions/group_anagrams.py`
- `exercises/solutions/merge_intervals.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Given an array, determine if any two numbers sum to a target."
- **Expected answer shape:** "If the array is unsorted, I can sort first in O(n log n) and then use two pointers in O(n), giving O(n log n) total and O(1) extra space. Alternatively, a hash map gives O(n) time and O(n) space without sorting."
- **Follow-up:** "When would you not sort?" (Answer: when O(n) time is required and O(n) space is allowed, or when original order matters.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. When does sorting help?
2. What is the difference between `sorted()` and `.sort()`?
3. What is a stable sort and why does it matter?
4. State the complexity of sort + scan.
5. How do you preserve original indices after sorting?

## 14. Related lessons

- `../two-pointers/two-pointers.md` — two pointers after sorting.
- `../binary-search/binary-search.md` — binary search requires sorted data.
- `../../week-01-foundations/lessons/arrays/arrays-and-lists.md` — list operations.
