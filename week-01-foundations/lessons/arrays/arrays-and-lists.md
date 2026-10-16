# Python Lists as Dynamic Arrays

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Topic** | Arrays |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Python lists, loops, functions; Day 1 routine; Day 2 complexity |
| **Deliverable** | `exercises/starter-code/array_stats.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Explain how a Python list stores elements and why indexing is O(1).
2. State the complexity of append, pop, insert, deletion, slicing and membership.
3. Choose between mutating in place and building a new list, with a stated trade-off.
4. Traverse an array by index, by value, and with `enumerate`.
5. Recognise when `insert(0, x)` or slicing in a loop makes code quadratic.
6. Write the edge-case matrix for an array problem.

## 2. Prerequisites check

1. Can you create, index and append to a Python list? (If no, review lists.)
2. Can you state the complexity of `x in list`? (If no, read section 7.)
3. Have you completed Days 1–2? (If no, read those lessons first.)

## 3. Why this matters

Almost every problem in Weeks 1–3 starts with a list. Knowing which operations are cheap and
which are expensive is what separates an O(n) solution from an accidental O(n²) one. The
constraint-to-complexity link from Day 1 only helps if you can count the cost of the operations
your plan uses. Python lists are dynamic arrays: they give O(1) indexing like a C array, but
with automatic resizing and convenient methods that have hidden costs.

## 4. Concept explanation

### 4.1 What a Python list really is

A Python list is a **dynamic array**: a contiguous block of memory holding references to objects,
plus a count of how many slots are used and how many are allocated. When you append and the block
is full, Python allocates a larger block (roughly 1.125× the size) and copies the references
over. That occasional copy is why append is **amortised O(1)**: most appends are cheap, and the
rare expensive one is paid for by the many cheap ones before it.

> **Mental model:** a list is a resizable row of boxes; indexing is "go straight to box i".

### 4.2 Indexing and assignment

`lst[i]` and `lst[i] = x` are O(1): Python computes the memory address directly from the base
address and the index. Negative indices (`lst[-1]`) are converted to `len(lst) - 1` first, still
O(1). Out-of-range indices raise `IndexError`.

### 4.3 Append and pop at the end

- `lst.append(x)`: amortised O(1).
- `lst.pop()` (no argument): O(1), removes and returns the last element.

These are the cheap building blocks. Prefer appending to the end and popping from the end.

### 4.4 Insert and delete in the middle

- `lst.insert(i, x)`: O(n) — every element from `i` onward shifts one slot.
- `lst.pop(i)`: O(n) — same shifting cost.
- `lst.remove(x)`: O(n) — scans to find `x`, then shifts.

`lst.insert(0, x)` is the worst case: it shifts the whole list. Doing it in a loop makes the
whole algorithm O(n²). If you need queue-like behaviour at the front, use `collections.deque`.

### 4.5 Membership and search

- `x in lst`, `lst.index(x)`, `lst.count(x)`: O(n) — linear scan, no hashing.
- `min(lst)`, `max(lst)`, `sum(lst)`: O(n).

Calling any of these inside a loop over the same list is usually a bug.

### 4.6 Slicing

`lst[a:b]` creates a **new list** containing copies of the references: O(b - a) time and space.
Slicing with a step (`lst[::2]`) is also O(k) where k is the result length. Slicing is
convenient but allocates memory; avoid it in tight loops.

### 4.7 In-place versus new list

- **In place:** mutate the input (`nums.sort()`, swapping elements). Uses O(1) extra space but
  destroys the original order.
- **New list:** build a result (`sorted(nums)`, a reversed copy). Uses O(n) extra space but
  preserves the input.

State the choice in your complexity sentence: "O(n) time and O(1) extra space, modifying the
input" versus "O(n) time and O(n) extra space, leaving the input unchanged."

### 4.8 Traversal patterns

```python
# By value
for value in nums:
    ...

# By index
for i in range(len(nums)):
    nums[i] = nums[i] * 2

# By index and value
for i, value in enumerate(nums):
    ...
```

Use `enumerate` when you need both; use direct iteration when you only need values; use index
loops when you must write back into the list.

## 5. Worked examples (simple → difficult)

### Example 1 — Operation costs in one place (simple)

```python
nums = [10, 20, 30, 40, 50]

print(nums[2])          # 30   O(1) indexing
nums.append(60)         # O(1) amortised
print(nums.pop())       # 60   O(1)
nums.insert(1, 99)      # O(n) shift
print(nums)             # [10, 99, 20, 30, 40, 50]
print(30 in nums)       # True  O(n) scan
print(nums[1:4])        # [99, 20, 30]  O(k) copy
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `nums[2]` | Direct index | O(1), no scan |
| `nums.append(60)` | Add to the end | Amortised O(1) |
| `nums.pop()` | Remove last | O(1) |
| `nums.insert(1, 99)` | Insert at index 1 | Shifts 5 elements, O(n) |
| `30 in nums` | Linear search | O(n); use a set for repeated tests |
| `nums[1:4]` | Slice copy | O(k) time and space |

### Example 2 — In-place doubling versus new list (moderate)

```python
# In place: O(n) time, O(1) extra space, input is changed.
def double_in_place(nums: list[int]) -> None:
    for i in range(len(nums)):
        nums[i] *= 2


# New list: O(n) time, O(n) extra space, input preserved.
def double_new(nums: list[int]) -> list[int]:
    return [x * 2 for x in nums]


if __name__ == "__main__":
    a = [1, 2, 3]
    double_in_place(a)
    print(a)            # [2, 4, 6]
    b = [1, 2, 3]
    print(double_new(b))  # [2, 4, 6]
    print(b)            # [1, 2, 3] unchanged
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `for i in range(len(nums))` | Index loop | Needed because we write back into the list |
| `nums[i] *= 2` | In-place update | O(1) per element |
| `[x * 2 for x in nums]` | List comprehension | Builds a new list in one pass |

### Example 3 — The insert(0, x) trap (harder)

```python
# Bad: O(n^2) because each insert(0, x) shifts the whole list.
def prepend_bad(items: list[int], values: list[int]) -> list[int]:
    result: list[int] = []
    for v in values:
        result.insert(0, v)   # O(n) per call
    return result

# Good: O(n) because append is amortised O(1), then reverse once.
def prepend_good(items: list[int], values: list[int]) -> list[int]:
    result: list[int] = []
    for v in values:
        result.append(v)      # amortised O(1)
    result.reverse()          # O(n)
    return result


if __name__ == "__main__":
    print(prepend_bad([], [1, 2, 3, 4]))   # [4, 3, 2, 1]
    print(prepend_good([], [1, 2, 3, 4]))  # [4, 3, 2, 1]
```

**Line-by-line explanation (good version)**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `result.append(v)` | Add to the end | Amortised O(1) |
| `result.reverse()` | Reverse in place | Single O(n) pass at the end |
| Total | O(n) | n appends + one reverse |

## 6. Dry-run table

Trace `prepend_good` on `values = [1, 2, 3]`.

| Step | `v` | `result` after append | Note |
| --- | --- | --- | --- |
| 0 | — | [] | initial |
| 1 | 1 | [1] | append |
| 2 | 2 | [1, 2] | append |
| 3 | 3 | [1, 2, 3] | append |
| 4 | — | [3, 2, 1] | reverse in place |

## 7. Complexity

| Operation | Time | Space | Notes |
| --- | --- | --- | --- |
| `lst[i]`, `lst[i] = x` | O(1) | O(1) | Direct index |
| `lst.append(x)` | O(1) amortised | O(1) amortised | Occasional resize |
| `lst.pop()` (last) | O(1) | O(1) | |
| `lst.insert(i, x)`, `lst.pop(i)` | O(n) | O(1) extra | Shifting |
| `x in lst`, `lst.index(x)` | O(n) | O(1) | Linear scan |
| `lst[a:b]` | O(k) | O(k) | Copy |
| `lst.sort()` | O(n log n) | O(n) | Timsort |
| In-place doubling | O(n) | O(1) | Index loop |
| New-list doubling | O(n) | O(n) | Comprehension |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| `insert(0, x)` in a loop | Slow on large inputs | Append then reverse, or use deque |
| Slicing inside a loop | Hidden O(n²) | Track indices instead |
| `x in list` inside a loop | Hidden O(n²) | Use a set for membership |
| Forgetting `min`/`max`/`sum` are O(n) | Underestimated time | Count them as a pass |
| Mutating input unexpectedly | Caller's data changed | Copy first or document the contract |
| Counting input as extra space | Over-reported space | Count only new containers |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Array stats** — return `(min, max, sum)` in one pass without built-ins → `exercises/starter-code/array_stats.py`
2. **Two Sum** — find two indices whose values sum to target → `exercises/starter-code/two_sum.py`
3. **Best time to buy and sell stock** — maximum profit from one buy and one sell → `exercises/starter-code/best_time_to_buy_sell_stock.py`

## 10. Hints

<details>
<summary>Hint 1 — for exercise 1 (array stats)</summary>

Start `best_min`, `best_max` and `total` from the first element, then update all three in one loop.

</details>

<details>
<summary>Hint 2 — for exercise 2 (two sum)</summary>

For each value, the complement you need is `target - value`. Remember complements you have seen
in a dict so the lookup is O(1).

</details>

<details>
<summary>Hint 3 — for exercise 3 (buy and sell stock)</summary>

Track the cheapest price seen so far. At each day, the best profit ending that day is
`price - cheapest_so_far`. Keep the maximum.

</details>

## 11. Solutions

- `exercises/solutions/array_stats.py`
- `exercises/solutions/two_sum.py`
- `exercises/solutions/best_time_to_buy_sell_stock.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Given an array, find two numbers that sum to a target."
- **Expected answer shape:** "I scan once, storing each value's complement in a hash map. Each
  element is checked once and the map lookup is O(1) on average, so it is O(n) time and O(n)
  space. On `[2, 7, 11, 15]` with target 9, when I reach 7 the complement 2 is already stored."
- **Follow-up the interviewer may ask:** "What if the array is sorted?" (Answer: two pointers,
  O(n) time and O(1) space.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. Why is list append amortised O(1)?
2. What is the cost of `lst.insert(0, x)` and why?
3. When does slicing cost O(k) space?
4. Name three traversal patterns and when to use each.
5. State the complexity of in-place doubling versus new-list doubling.

## 14. Related lessons

- `../problem-solving/problem-solving-foundations.md` — the routine that uses this analysis.
- `../complexity/big-o-complexity.md` — loop counting and growth classes.
- `../../docs/complexity-cheatsheet.md` — the full Python operation cost reference.
