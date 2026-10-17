# Sliding Window

| | |
| --- | --- |
| **Week** | 2 — Two pointers, sliding window, binary search, sorting patterns |
| **Topic** | Sliding window |
| **Estimated time** | Concepts 45 min + implementation 40 min |
| **Prerequisites** | Week 1 arrays and hashing; Day 1 two pointers |
| **Deliverable** | `exercises/starter-code/max_sum_subarray_k.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Recognise a fixed-size window and maintain a running aggregate in O(n).
2. Recognise a variable-size window and shrink while a condition is violated.
3. Solve Maximum Sum Subarray of Size K and Longest Substring Without Repeating Characters.
4. State the invariant of each window.
5. Explain why sliding window is O(n) despite two pointers.
6. Handle edge cases: empty input, window larger than input, all equal.

## 2. Prerequisites check

1. Can you maintain a running sum in a loop? (If no, review Week 1.)
2. Can you use a set for membership? (If no, review Week 1 hashing.)
3. Have you completed Day 1? (If no, read two-pointers.md first.)

## 3. Why this matters

Sliding window turns an O(nk) or O(n²) scan into O(n) by reusing work from the previous
position: when the window moves one step, only one element enters and one leaves. It is the
standard pattern for "longest/shortest subarray/substring with a condition". Interviewers test
whether you can identify the invariant and explain why each element is added and removed at most
once.

## 4. Concept explanation

### 4.1 Fixed-size window

A window of exactly `k` consecutive elements slides one step at a time. Maintain a running
aggregate (sum, count, max). When the window moves:

- Add the entering element (right).
- Remove the leaving element (left).
- Update the answer.

Each element is added once and removed once → O(n) total, not O(nk).

> **Mental model:** a frame of size k slides across the array; only the new and old edges change.

### 4.2 Variable-size window

Two pointers `left` and `right` define a window that grows and shrinks. The right edge always
advances; the left edge advances only while a condition is violated. Invariant: the window
`[left, right]` always satisfies the condition (or is empty). Because both pointers only move
forward, total work is O(n).

Pattern:

```python
left = 0
for right in range(n):
    # add nums[right] to the window state
    while condition_violated():
        # remove nums[left] from the window state
        left += 1
    # update answer with window [left, right]
```

### 4.3 Window state

The state depends on the problem: a running sum (fixed window), a set of characters (longest
substring without repeats), or a frequency map (at most K distinct). The state must support
O(1) add and remove.

### 4.4 Why it is O(n)

Each pointer moves at most n steps total. The inner `while` loop looks nested but each iteration
advances `left`, and `left` never decreases. Total iterations across the whole run ≤ n.

### 4.5 Fixed versus variable

- Fixed: window size is given (k). Simpler; no shrinking logic.
- Variable: window size is the answer or constrained by a condition. Needs a shrink loop.

## 5. Worked examples (simple → difficult)

### Example 1 — Fixed-size window sum (simple)

```python
def max_sum_subarray_k(nums: list[int], k: int) -> int:
    if not nums or k <= 0 or k > len(nums):
        return 0
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > best:
            best = window_sum
    return best


if __name__ == "__main__":
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))  # 9  (5+1+3)
    print(max_sum_subarray_k([1, 2, 3], 5))            # 0  (k > n)
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `if not nums or k <= 0 or k > len(nums)` | Guard | No valid window |
| `window_sum = sum(nums[:k])` | Initial window | First k elements |
| `best = window_sum` | Seed best | First window is a candidate |
| `for i in range(k, len(nums))` | Slide right edge | i is the entering index |
| `window_sum += nums[i] - nums[i - k]` | Update in O(1) | Add entering, remove leaving |
| `if window_sum > best` | Track best | Update if better |

### Example 2 — Longest substring without repeating (moderate)

```python
def longest_unique_substring(s: str) -> int:
    seen: set[str] = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    print(longest_unique_substring("abcabcbb"))  # 3  ("abc")
    print(longest_unique_substring("bbbbb"))     # 1
    print(longest_unique_substring(""))          # 0
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `seen: set[str] = set()` | Window state | O(1) membership |
| `left = 0` | Left edge | Shrinks when needed |
| `for right in range(len(s))` | Grow right edge | Every character enters once |
| `while s[right] in seen` | Condition violated | Duplicate in window |
| `seen.remove(s[left]); left += 1` | Shrink | Remove leftmost until valid |
| `seen.add(s[right])` | Add new char | Window now valid |
| `best = max(best, right - left + 1)` | Update answer | Window length |

### Example 3 — Minimum size subarray sum (harder)

```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    running = 0
    best = float("inf")
    for right in range(len(nums)):
        running += nums[right]
        while running >= target:
            best = min(best, right - left + 1)
            running -= nums[left]
            left += 1
    return 0 if best == float("inf") else best


if __name__ == "__main__":
    print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # 2  ([4, 3])
    print(min_subarray_len(100, [1, 2, 3]))           # 0
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `running += nums[right]` | Grow window | Add entering element |
| `while running >= target` | Condition met | Try to shrink |
| `best = min(best, right - left + 1)` | Update best | Record valid window length |
| `running -= nums[left]; left += 1` | Shrink | Remove leaving element |
| `return 0 if best == inf else best` | No valid window | Handle impossible case |

## 6. Dry-run table

Trace fixed window on `[2, 1, 5, 1, 3, 2]`, k = 3.

| Step | Window | `window_sum` | `best` | Note |
| --- | --- | --- | --- | --- |
| 0 | [2,1,5] | 8 | 8 | initial |
| 1 | [1,5,1] | 7 | 8 | +1 -2 |
| 2 | [5,1,3] | 9 | 9 | +3 -1 |
| 3 | [1,3,2] | 6 | 9 | +2 -5 |

Trace variable window on `"abcabcbb"`.

| Step | `right` | `s[right]` | `seen` before | Action | `left` | `best` |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | a | {} | add a | 0 | 1 |
| 1 | 1 | b | {a} | add b | 0 | 2 |
| 2 | 2 | c | {a,b} | add c | 0 | 3 |
| 3 | 3 | a | {a,b,c} | remove a, left=1; add a | 1 | 3 |
| 4 | 4 | b | {b,c,a} | remove b, left=2; add b | 2 | 3 |
| 5 | 5 | c | {c,a,b} | remove c, left=3; add c | 3 | 3 |
| 6 | 6 | b | {a,b,c} | remove a? s[3]=a not b; remove b? left=3 s[3]=a, remove a left=4; s[4]=b remove b left=5; add b | 5 | 3 |
| 7 | 7 | b | {c,a?...} | remove until b gone; add b | 6 | 3 |

## 7. Complexity

| Variant | Time | Space | Notes |
| --- | --- | --- | --- |
| Fixed-size window | O(n) | O(1) | Each element added/removed once |
| Longest unique substring | O(n) average | O(k) | k = alphabet size; set operations O(1) avg |
| Minimum size subarray sum | O(n) | O(1) | Both pointers advance at most n |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Recomputing window sum each step | O(nk), slow | Update with add-entering minus remove-leaving |
| Forgetting to remove leaving element | Wrong aggregate | Always subtract nums[i - k] |
| Shrinking when condition already holds | Wrong answer or O(n²) | Shrink only while violated |
| Off-by-one in window length | Wrong best | Use `right - left + 1` |
| Not handling k > n | IndexError or wrong answer | Guard at the top |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Maximum sum subarray of size K** → `exercises/starter-code/max_sum_subarray_k.py`
2. **Longest substring without repeating** → `exercises/starter-code/longest_substring_without_repeating.py`
3. **Minimum size subarray sum** → `exercises/starter-code/minimum_size_subarray_sum.py`

## 10. Hints

<details><summary>Hint 1 — for exercise 1</summary>
Seed the sum with the first k elements. Then slide: add the new element, subtract the one leaving.
</details>
<details><summary>Hint 2 — for exercise 2</summary>
Use a set for the current window. When a duplicate arrives, shrink from the left until it is gone.
</details>
<details><summary>Hint 3 — for exercise 3</summary>
Grow right until the sum reaches target, then shrink left as much as possible while still reaching target.
</details>

## 11. Solutions

- `exercises/solutions/max_sum_subarray_k.py`
- `exercises/solutions/longest_substring_without_repeating.py`
- `exercises/solutions/minimum_size_subarray_sum.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Find the longest substring without repeating characters."
- **Expected answer shape:** "I use a sliding window with a set. The right edge grows; when a
  duplicate is found, the left edge shrinks until the duplicate is removed. Each character is
  added and removed at most once, so it is O(n) time and O(k) space."
- **Follow-up:** "What if the alphabet is large (Unicode)?" (Answer: use a dict mapping char to
  its last index to jump left directly, still O(n).)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. State the fixed-window update rule.
2. State the variable-window shrink condition.
3. Why is sliding window O(n) despite nested loops?
4. When do you use fixed versus variable?
5. State the complexity of all three problems.

## 14. Related lessons

- `../two-pointers/two-pointers.md` — the foundation.
- `../../week-01-foundations/lessons/arrays/arrays-and-lists.md` — list operations.
- `../../week-01-foundations/lessons/hashing/hashing-dictionaries-sets.md` — sets and dicts for window state.
- `../../docs/problem-solving-framework.md` — the routine to reuse.
