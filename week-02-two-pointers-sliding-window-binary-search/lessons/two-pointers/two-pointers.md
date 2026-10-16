# Two Pointers

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Topic** | Two pointers |
| **Estimated time** | Concepts 45 min + implementation 40 min |
| **Prerequisites** | Week 1: arrays, complexity, hashing |
| **Deliverable** | `exercises/starter-code/two_sum_sorted.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Explain the opposite-direction two-pointer technique on a sorted array.
2. Prove (informally) that the pointers never need to move backwards.
3. Solve a pair-sum problem in O(n) time and O(1) space.
4. Implement same-direction read/write pointers for in-place compaction.
5. Solve Container With Most Water with a stated invariant.
6. Choose two pointers versus hashing and justify the choice.

## 2. Prerequisites check

1. Can you index and traverse a list? (If no, review Week 1 arrays.)
2. Do you know what "sorted" means and why it helps? (If no, read section 4.1.)
3. Can you state the complexity of a single loop? (If no, review Week 1 Day 2.)

## 3. Why this matters

Two pointers turn an O(n²) nested search into an O(n) single pass by exploiting order. The
most common interview forms are: "find a pair in a sorted array", "remove duplicates in place",
and "container with most water". The key skill is not the code but the **invariant**: a sentence
that is true before and after every step and that guarantees correctness. Interviewers ask
"why does the pointer never move back?" — this lesson answers that.

## 4. Concept explanation

### 4.1 Opposite-direction pointers (sorted array)

Given a sorted array, place one pointer at the left end and one at the right end. At each step,
compare the sum (or product, or difference) of the two pointed elements with the target:

- If the sum is too small, move the **left** pointer right (increase the sum).
- If the sum is too large, move the **right** pointer left (decrease the sum).
- If equal, record the answer.

> **Mental model:** the two pointers squeeze inward, discarding the side that cannot contain
> the answer.

### 4.2 Why the pointers never move back (monotonicity)

Suppose the array is sorted ascending and we want `nums[i] + nums[j] == target`. If
`nums[i] + nums[j] < target`, then for this `i`, every `j' < j` gives an even smaller sum
(because the array is sorted). So no solution uses this `i` with any `j' <= j`. We can safely
discard `i` and move left forward. The symmetric argument holds when the sum is too large.
Each pointer moves at most n steps, so the whole algorithm is O(n).

### 4.3 Same-direction (read/write) pointers

When you must modify an array in place (remove duplicates, move zeros), use two pointers moving
in the same direction:

- `read` scans every element.
- `write` marks where the next kept element goes.

Invariant: `nums[0..write-1]` contains the kept elements in order, and `nums[write..read-1]`
are slots that may be overwritten. Each element is read once and written at most once → O(n).

### 4.4 Container With Most Water

Given heights, find two lines that form the container with the most water. Area =
`min(height[left], height[right]) * (right - left)`. Start with the widest container (left=0,
right=n-1). Move the pointer at the **shorter** line inward: moving the taller line cannot
increase the area because the width shrinks and the height is capped by the shorter line. This
greedy choice is safe.

### 4.5 Invariants

- Pair sum: "all pairs with left index < i or right index > j have been ruled out."
- Compaction: "nums[0..write-1] are the kept elements in original order."
- Container: "the maximum area using the current left or right boundary has been considered."

State the invariant in your complexity sentence and your spoken answer.

### 4.6 Two pointers versus hashing

- Sorted input + O(1) space requirement → two pointers.
- Unsorted input or O(n) space allowed → hash map (Week 1 Two Sum).
- Two pointers need sorted data; sorting first costs O(n log n), which may erase the benefit.

## 5. Worked examples (simple → difficult)

### Example 1 — Pair sum in a sorted array (simple)

```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
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


if __name__ == "__main__":
    print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # [1, 3]  (2+4)
    print(two_sum_sorted([1, 2, 3, 4, 6], 10)) # [3, 4]  (4+6)
    print(two_sum_sorted([1, 2, 3, 4, 6], 100))# [-1, -1]
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `left, right = 0, len(nums) - 1` | Widest possible pair | Sorted array, so extremes first |
| `s = nums[left] + nums[right]` | Current sum | Compared with target |
| `if s == target` | Found it | Return indices |
| `if s < target: left += 1` | Sum too small | Increase the smaller side |
| `else: right -= 1` | Sum too large | Decrease the larger side |

### Example 2 — Remove duplicates in place (moderate)

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    data = [1, 1, 2, 2, 3]
    k = remove_duplicates(data)
    print(k, data[:k])  # 3 [1, 2, 3]
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `write = 1` | First element always kept | write points at the next slot to fill |
| `for read in range(1, len(nums))` | Scan from index 1 | read visits every element once |
| `if nums[read] != nums[write - 1]` | New value? | Compare with last kept value |
| `nums[write] = nums[read]` | Keep it | Write into the next free slot |
| `write += 1` | Advance write | Next kept element goes after |
| `return write` | New length | Elements after write are stale |

### Example 3 — Container With Most Water (harder)

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        best = max(best, h * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))                          # 1
    print(max_area([]))                             # 0
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `left, right = 0, len(height) - 1` | Widest container | Start with maximum width |
| `width = right - left` | Current width | Shrinks each step |
| `h = min(...)` | Limiting height | Area capped by shorter line |
| `best = max(best, h * width)` | Track best area | Update if better |
| `if height[left] < height[right]: left += 1` | Move shorter side | Taller side cannot improve area |
| `else: right -= 1` | Move right side | Symmetric case |

## 6. Dry-run table

Trace `two_sum_sorted` on `[1, 2, 3, 4, 6]`, target 6.

| Step | `left` | `right` | `nums[left]` | `nums[right]` | `s` | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 4 | 1 | 6 | 7 | too large → right-- |
| 1 | 0 | 3 | 1 | 4 | 5 | too small → left++ |
| 2 | 1 | 3 | 2 | 4 | 6 | match → return [1, 3] |

Trace `remove_duplicates` on `[1, 1, 2]`.

| Step | `read` | `nums[read]` | `nums[write-1]` | Action | `write` |
| --- | --- | --- | --- | --- | --- |
| 0 | — | — | — | init | 1 |
| 1 | 1 | 1 | 1 | equal, skip | 1 |
| 2 | 2 | 2 | 1 | keep → nums[1]=2 | 2 |

## 7. Complexity

| Variant | Time | Space | Notes |
| --- | --- | --- | --- |
| Pair sum (two pointers) | O(n) | O(1) | Each pointer moves at most n steps |
| Pair sum (hash map) | O(n) average | O(n) | Week 1 version |
| Remove duplicates in place | O(n) | O(1) | read and write each advance at most n |
| Container With Most Water | O(n) | O(1) | One pointer moves each step |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Unsorted input with opposite pointers | Wrong answer | Sort first or use hashing |
| `while left <= right` | Double-counts or index error | Use `while left < right` |
| Moving the taller side in container | Wrong maximum area | Move the shorter side |
| Forgetting duplicates in compaction | Stale trailing values | Return `write`, not `len(nums)` |
| Off-by-one in write index | IndexError or lost element | Keep `write` as "next free slot" |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Two sum sorted** — pair sum in a sorted array → `exercises/starter-code/two_sum_sorted.py`
2. **Remove duplicates** — in-place compaction → `exercises/starter-code/remove_duplicates.py`
3. **Container with most water** — maximum area → `exercises/starter-code/container_with_most_water.py`

## 10. Hints

<details><summary>Hint 1 — for exercise 1</summary>
Start at both ends. If the sum is too small, move left up; if too large, move right down.
</details>
<details><summary>Hint 2 — for exercise 2</summary>
Keep a write index. Only write when the current value differs from the last kept value.
</details>
<details><summary>Hint 3 — for exercise 3</summary>
Move the pointer at the shorter line; the taller line cannot improve the area.
</details>

## 11. Solutions

- `exercises/solutions/two_sum_sorted.py`
- `exercises/solutions/remove_duplicates.py`
- `exercises/solutions/container_with_most_water.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Given a sorted array, find two numbers that sum to a target."
- **Expected answer shape:** "I use two pointers at both ends. Because the array is sorted, if the
  sum is too small I move the left pointer up and if too large I move the right pointer down. Each
  pointer moves at most n steps, so it is O(n) time and O(1) space."
- **Follow-up:** "What if the array is not sorted?" (Answer: sort first, O(n log n), or use a
  hash map, O(n) time and O(n) space.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. State the monotonicity argument in one sentence.
2. Why does Container With Most Water move the shorter side?
3. What is the invariant for in-place compaction?
4. When would you choose hashing over two pointers?
5. State the complexity of all three variants.

## 14. Related lessons

- `../sliding-window/sliding-window.md` — the next pattern.
- `../../week-01-foundations/lessons/arrays/arrays-and-lists.md` — list operations.
- `../../docs/problem-solving-framework.md` — the routine to reuse.
