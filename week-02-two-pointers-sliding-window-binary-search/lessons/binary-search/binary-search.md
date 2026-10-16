# Binary Search

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Topic** | Binary search |
| **Estimated time** | Concepts 45 min + implementation 40 min |
| **Prerequisites** | Week 1 arrays and complexity; Week 2 Days 1–2 |
| **Deliverable** | `exercises/starter-code/binary_search.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Explain why binary search requires an ordered search space.
2. Implement standard binary search with correct bounds and termination.
3. Implement first/last occurrence, lower/upper bound, and insertion position.
4. State and justify the loop invariant.
5. Prove (informally) that the target is never discarded.
6. State O(log n) time and O(1) space and justify.

## 2. Prerequisites check

1. Can you index and traverse a list? (If no, review Week 1 arrays.)
2. Do you know what "sorted" means? (If no, read section 4.1.)
3. Can you state the complexity of a single loop? (If no, review Week 1 Day 2.)

## 3. Why this matters

Binary search is the first algorithm that beats O(n) for searching by exploiting structure. It
appears in interviews constantly, both as a standalone question and as a subroutine (lower/upper
bound, binary search on answer). The hard part is not the idea (halve the space) but the
**bounds**: off-by-one errors are the #1 bug. This lesson teaches the invariant that makes the
bounds correct, so you can derive them instead of memorising templates.

## 4. Concept explanation

### 4.1 Searching: linear vs binary

- **Linear search:** check every element left to right. O(n). Works on any array.
- **Binary search:** requires an ordered search space. Compare the middle element with the
  target and discard half. O(log n).

Binary search is only valid when the search space is **monotonic**: a predicate that is false
for a while and then true (or vice versa), or a sorted array where all elements left of the
target are smaller and all right are larger.

> **Mental model:** binary search is like looking up a word in a dictionary — you open the
> middle and decide which half contains the word.

### 4.2 Indexes, intervals, and loop conditions

Two common conventions:

- **Inclusive interval `[left, right]`:** both ends are candidates. Loop condition
  `left <= right`. Midpoint `mid = left + (right - left) // 2`.
- **Half-open interval `[left, right)`:** right is exclusive. Loop condition `left < right`.
  Midpoint `mid = left + (right - left) // 2`.

This lesson uses the **inclusive** convention for standard search and the variations, because it
is the most common in interviews and makes the "not found" case explicit.

### 4.3 Midpoint formula

`mid = left + (right - left) // 2` avoids overflow in languages with fixed-width integers.
In Python, integers are arbitrary precision, so `mid = (left + right) // 2` is also safe, but
the safe form is a good habit and is what interviewers expect.

### 4.4 Boundary updates

- If `nums[mid] == target`: found (or record and continue for first/last).
- If `nums[mid] < target`: target must be to the right → `left = mid + 1`.
- If `nums[mid] > target`: target must be to the left → `right = mid - 1`.

The `+1` / `-1` is essential: it excludes `mid` from the next interval, guaranteeing progress
and termination.

### 4.5 Termination

Each iteration strictly shrinks the interval (either left increases or right decreases). Since
the interval is finite, the loop terminates. When `left > right`, the interval is empty and the
target is not present.

### 4.6 Why off-by-one errors occur

They come from mismatching the interval convention with the boundary update. Rule: pick one
convention and apply it consistently. If you use `[left, right]` inclusive, update with `mid+1`
and `mid-1`, and loop while `left <= right`.

## 5. Worked examples (simple → difficult)

### Example 1 — Standard search, value present (simple)

```python
def binary_search(nums: list[int], target: int) -> int:
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


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 5))   # 2
    print(binary_search([1, 3, 5, 7, 9], 1))   # 0
    print(binary_search([1, 3, 5, 7, 9], 9))   # 4
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `left, right = 0, len(nums) - 1` | Full inclusive interval | Both ends are candidates |
| `while left <= right` | Loop while non-empty | Empty interval means not found |
| `mid = left + (right - left) // 2` | Safe midpoint | Avoids overflow; integer division |
| `if nums[mid] == target: return mid` | Found | Any matching index is fine |
| `if nums[mid] < target: left = mid + 1` | Target to the right | Discard mid and everything left |
| `else: right = mid - 1` | Target to the left | Discard mid and everything right |
| `return -1` | Not found | Interval exhausted |

### Example 2 — Value not present (moderate)

```python
print(binary_search([1, 3, 5, 7, 9], 4))  # -1
```

Trace: interval shrinks until empty; return -1.

### Example 3 — Empty and single-element arrays (edge)

```python
print(binary_search([], 5))   # -1
print(binary_search([7], 7))  # 0
print(binary_search([7], 3))  # -1
```

### Example 4 — Duplicates: first occurrence (harder)

```python
def first_occurrence(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid          # record, but keep searching left
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == "__main__":
    print(first_occurrence([1, 2, 2, 2, 3], 2))  # 1
```

### Example 5 — Last occurrence (harder)

```python
def last_occurrence(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1       # keep searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

### Example 6 — Lower bound and upper bound (harder)

```python
def lower_bound(nums: list[int], target: int) -> int:
    # first index where nums[i] >= target
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(nums: list[int], target: int) -> int:
    # first index where nums[i] > target
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
```

- Count of target = `upper_bound - lower_bound`.
- Insertion position = `lower_bound`.

## 6. Dry-run table

Trace standard binary search on `[1, 3, 5, 7, 9]`, target 7.

| Step | `left` | `right` | `mid` | `nums[mid]` | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 4 | 2 | 5 | 5 < 7 → left = 3 |
| 1 | 3 | 4 | 3 | 7 | match → return 3 |

Trace first_occurrence on `[1, 2, 2, 2, 3]`, target 2.

| Step | `left` | `right` | `mid` | `nums[mid]` | Action |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 4 | 2 | 2 | record 2; right = 1 |
| 1 | 0 | 1 | 0 | 1 | 1 < 2 → left = 1 |
| 2 | 1 | 1 | 1 | 2 | record 1; right = 0 |
| 3 | 1 | 0 | — | — | loop ends; result = 1 |

## 7. Correctness and loop invariants

**Invariant (standard search, inclusive interval):** if `target` is in `nums`, then it lies in
`nums[left..right]` (inclusive). Initially the whole array is the interval, so the invariant
holds. Each update discards only elements that cannot equal the target:

- If `nums[mid] < target`, then all elements at indices ≤ mid are < target (sorted), so the
  target cannot be there; setting `left = mid + 1` preserves the invariant.
- If `nums[mid] > target`, symmetrically set `right = mid - 1`.
- If equal, we return immediately.

Termination: each iteration reduces `right - left` by at least 1, so the interval eventually
becomes empty. When empty, the invariant says the target is not in the (empty) interval, so
returning -1 is correct.

## 8. Complexity

- Iterative binary search: O(log n) time, O(1) auxiliary space.
- Recursive binary search: O(log n) time, O(log n) call-stack space.
- Linear search: O(n) time, O(1) space.
- If the input is unsorted, sorting first costs O(n log n), which may dominate.

Derivation: each step halves the interval size n → n/2 → n/4 → ... → 1, taking log₂ n steps.

## 9. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| `while left < right` with `mid+1`/`mid-1` updates | Skips the last element or infinite loop | Match convention: inclusive uses `<=` |
| `mid = (left + right) // 2` in fixed-width languages | Overflow | Use `left + (right - left) // 2` |
| Forgetting `+1`/`-1` | Infinite loop | Always exclude `mid` |
| Returning `mid` for first occurrence | Returns any match, not the first | Record and continue left |
| Off-by-one in insertion position | Wrong index | Use half-open lower_bound |
| Not handling empty input | IndexError | Guard or let loop handle it |

## 10. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Binary search** — standard search → `exercises/starter-code/binary_search.py`
2. **Search insert position** — insertion index → `exercises/starter-code/search_insert_position.py`
3. **First and last position** — both boundaries → `exercises/starter-code/first_last_occurrence.py`

## 11. Hints

<details><summary>Hint 1 — for exercise 1</summary>
Use inclusive bounds. Update with mid+1 and mid-1. Loop while left <= right.
</details>
<details><summary>Hint 2 — for exercise 2</summary>
The insertion position is the lower bound: first index where nums[i] >= target.
</details>
<details><summary>Hint 3 — for exercise 3</summary>
Run binary search twice: once to find the first occurrence (keep searching left), once for the last (keep searching right).
</details>

## 12. Solutions

- `exercises/solutions/binary_search.py`
- `exercises/solutions/search_insert_position.py`
- `exercises/solutions/first_last_occurrence.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 13. Interview applications

- **Question form:** "Implement binary search on a sorted array."
- **Expected answer shape:** "I maintain an inclusive interval [left, right]. I compute the midpoint safely, compare, and discard the half that cannot contain the target. Each step halves the interval, so it is O(log n) time and O(1) space."
- **Follow-up:** "How would you find the first occurrence?" (Answer: record the match and continue searching left.)

## 14. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. Why does binary search require sorted data?
2. State the loop invariant for standard binary search.
3. What is the difference between lower bound and upper bound?
4. How do you count occurrences using bounds?
5. State the complexity and justify.

## 15. Related lessons

- `../binary-search-on-answer/binary-search-on-answer.md` — the next pattern.
- `../../week-01-foundations/lessons/arrays/arrays-and-lists.md` — list operations.
- `../../docs/problem-solving-framework.md` — the routine to reuse.
