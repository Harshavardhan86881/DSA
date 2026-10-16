# Big-O Complexity

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Topic** | Time and space complexity |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Day 1 problem-solving routine; Python loops and lists |
| **Deliverable** | `exercises/starter-code/running_sum.py` attempted; complexity rewrites of Day 1 solutions |

## 1. Learning objectives

After this lesson you can:

1. Explain Big-O, Big-Theta and Big-Omega in one sentence each.
2. Classify growth as constant, logarithmic, linear, linearithmic, quadratic or exponential.
3. Distinguish best, average and worst cases.
4. Separate time complexity from space complexity.
5. Count loops correctly and drop constant factors.
6. Compare a brute-force and an improved version of the same task.
7. State the complexity of common Python operations.

## 2. Prerequisites check

1. Can you read a `for` loop and state how many times it runs? (If no, review loops.)
2. Can you state the complexity of `x in list`? (If no, read section 7 of this lesson.)
3. Have you completed Day 1? (If no, read `problem-solving-foundations.md` first.)

## 3. Why this matters

Complexity is how you predict whether code will finish in time. An O(n²) solution that works on
100 elements fails on 100,000 elements, and the only way to know before submitting is to count
the work. Interviews almost always ask "what is the complexity of your solution?" and expect the
answer in seconds. The constraint-to-complexity link from Day 1 turns the input size into a
target complexity, so you can reject a slow plan before writing it.

## 4. Concept explanation

### 4.1 What Big-O measures

Big-O describes how the work grows when the input grows. It ignores constant factors and
small-input behaviour. `O(2n + 5)` simplifies to `O(n)`. `O(n² + n)` simplifies to `O(n²)`
because the slowest term wins.

Big-O is an **upper bound**: the work never grows faster than this. It answers "in the worst
case, how bad can this get?"

> **Mental model:** Big-O is the speed limit of your algorithm as the input gets large.

### 4.2 Big-O, Big-Theta, Big-Omega

- **Big-O (O):** upper bound. The work is at most this much. Used most often in interviews.
- **Big-Omega (Ω):** lower bound. The work is at least this much.
- **Big-Theta (Θ):** tight bound. The work is both O and Ω of the same class, so it grows
  exactly like that class.

Example: linear search is O(n) (at most n comparisons), Ω(1) (at least one comparison), and
therefore not Θ(1) but Θ(n) in the worst case. In practice, when an interviewer asks for
complexity, they want the tightest Big-O you can state, usually the worst case.

### 4.3 Growth classes

From fastest to slowest:

| Class | Name | Typical source |
| --- | --- | --- |
| O(1) | Constant | Index lookup, hash lookup |
| O(log n) | Logarithmic | Binary search, balanced tree height |
| O(n) | Linear | One pass over the data |
| O(n log n) | Linearithmic | Sorting with `sorted()` |
| O(n²) | Quadratic | Nested loops over the same list |
| O(2ⁿ) | Exponential | Subset enumeration |

Assuming roughly 10⁷ simple operations per second:

| Complexity | n = 10 | n = 100 | n = 1,000 | n = 10⁶ |
| --- | --- | --- | --- | --- |
| O(1) | instant | instant | instant | instant |
| O(log n) | 3 steps | 7 | 10 | 20 |
| O(n) | 10 | 100 | 1,000 | 1,000,000 |
| O(n log n) | 33 | 664 | ~10⁴ | ~2·10⁷ |
| O(n²) | 100 | 10⁴ | 10⁶ (slow) | too slow |
| O(2ⁿ) | 1,024 | astronomically large | — | — |

Rule of thumb: **n up to ~10⁶ needs O(n) or O(n log n). n up to ~5,000 can afford O(n²).**

### 4.4 Best, average and worst case

These are different questions about the same algorithm.

- **Worst case:** the input that makes the algorithm do the most work. Interviews normally mean
  this when they ask "what is the complexity?".
- **Best case:** the input that makes it do the least work (often an early return).
- **Average case:** the expected work over typical inputs.

Hashing is the classic example: dict/set lookups are **average O(1)**, but worst case is O(n)
when many keys collide. Always state "average" for hashing so you are not claiming a guarantee
you do not have.

### 4.5 Time versus space complexity

- **Time:** how the number of operations grows with n.
- **Space:** how much **extra** memory the algorithm allocates. The input itself is not counted.

A hash map that stores up to n entries is O(n) space. Recursion costs O(depth) stack frames.
Slicing or copying a list of length n costs O(n) extra space — easy to forget. Interviewers
often accept trading space for time when the trade is stated: "this is O(n) time instead of
O(n²), at the cost of O(n) extra space."

### 4.6 Counting loops correctly

| Code shape | Complexity |
| --- | --- |
| One loop over n | O(n) |
| Two independent loops over n | O(n) (they add) |
| Loop inside a loop, both over n | O(n²) (they multiply) |
| Loop that halves its range each time | O(log n) |
| Loop over n with an inner loop over n/2 | O(n²) still — constants are dropped |
| Loop over n with an inner loop that runs a fixed number of times (e.g. 26 letters) | O(n) |
| Sorting inside a loop | O(n² log n) — a red flag |

Example of dropping constants:

```python
for i in range(n):          # n iterations
    for j in range(100):    # fixed 100 iterations
        pass
# Total work: 100n -> O(n), not O(n^2)
```

### 4.7 Python operation costs

**List (dynamic array)**

| Operation | Complexity | Note |
| --- | --- | --- |
| `lst[i]`, `lst[i] = x` | O(1) | Direct index |
| `lst.append(x)` | O(1) amortised | Occasional resize copies elements |
| `lst.pop()` (last) | O(1) | |
| `lst.pop(i)`, `lst.insert(i, x)` | O(n) | Every element after `i` shifts |
| `lst.insert(0, x)` | O(n) | Avoid in loops |
| `x in lst`, `lst.index(x)` | O(n) | Linear scan |
| `len(lst)` | O(1) | |
| `min`, `max`, `sum` | O(n) | |
| `lst[a:b]` (slice of length k) | O(k) time, O(k) space | Creates a copy |
| `lst.sort()`, `sorted(lst)` | O(n log n) | Timsort; stable |

**Strings** are immutable: any "change" builds a new string.

| Operation | Complexity | Note |
| --- | --- | --- |
| `s[i]` | O(1) | |
| `len(s)` | O(1) | |
| `s + t` | O(len(s) + len(t)) | In a loop this becomes O(n²) |
| `x in s` | O(len(s)) | Substring search |
| `s.lower()`, `s.upper()` | O(len(s)) | New string |
| `s.split(sep)`, `sep.join(parts)` | O(len(s)) | Preferred for building strings |

**Loop rule:** never build a result with `result = result + x` inside a loop. Collect parts in a
list and `"".join(parts)` once.

**dict and set (hash tables)** — average case assumes a good hash function.

| Operation | Average | Worst case |
| --- | --- | --- |
| `d[key]`, `d[key] = value` | O(1) | O(n) |
| `key in d`, `key in s` | O(1) | O(n) |
| `del d[key]` | O(1) | O(n) |
| iterate a dict or set | O(n) | O(n) |

Two consequences used constantly in Week 1:

- Counting with a dict is a single O(n) pass instead of O(n²) nested loops.
- Membership tests in a set turn "have I seen this?" from O(n) into O(1) on average.

### 4.8 Amortised complexity

Amortised complexity spreads the cost of occasional expensive operations. List `append` is
amortised O(1): most appends are cheap, but occasionally the underlying array reallocates and
copies all elements. Averaged over many appends, each costs O(1). Amortised is not the same as
average case: amortised guarantees the average over a sequence of operations, while average case
depends on input distribution.

## 5. Worked examples (simple → difficult)

### Example 1 — Classify the growth of small snippets (simple)

```python
# Snippet A: O(1)
def first_element(nums):
    return nums[0] if nums else None

# Snippet B: O(n)
def total(nums):
    s = 0
    for x in nums:
        s += x
    return s

# Snippet C: O(n^2)
def all_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            count += 1
    return count
```

**Line-by-line explanation**

| Snippet | What happens | Why that class |
| --- | --- | --- |
| A | Returns one element | No loop; work does not grow with n |
| B | One pass adding | One loop over n |
| C | Nested loops | n × n = n² |

### Example 2 — O(n²) versus O(n) for the same task (moderate)

```python
# Task: does the list contain a duplicate value?

# O(n^2) time, O(1) space: compare every pair.
def has_dup_slow(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# O(n) time average, O(n) space: remember what we have seen.
def has_dup_fast(nums: list[int]) -> bool:
    seen: set[int] = set()
    for value in nums:
        if value in seen:          # O(1) average
            return True
        seen.add(value)
    return False
```

**Line-by-line explanation (fast version)**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `seen: set[int] = set()` | Empty set | Set gives O(1) average membership |
| `for value in nums` | One pass | Keeps time linear |
| `if value in seen` | Seen before? | Early return on first duplicate |
| `seen.add(value)` | Record value | Future duplicates caught here |

The trade-off is explicit: O(n) time instead of O(n²), at the cost of O(n) extra space.

### Example 3 — Why string concatenation in a loop is quadratic (harder)

```python
# Bad: O(n^2) because each += copies the whole string so far.
def build_bad(chars: list[str]) -> str:
    result = ""
    for c in chars:
        result = result + c       # copies len(result) characters each time
    return result

# Good: O(n) because join copies once at the end.
def build_good(chars: list[str]) -> str:
    parts: list[str] = []
    for c in chars:
        parts.append(c)           # amortised O(1)
    return "".join(parts)         # one copy of total length
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `result = result + c` | Builds a new string each iteration | Strings are immutable, so this copies |
| `parts.append(c)` | Adds to a list | Amortised O(1), no copying of previous parts |
| `"".join(parts)` | One final string | Single pass over total length |

## 6. Dry-run table

Trace the growth of `build_bad` on input `['a', 'b', 'c']`.

| Step | `c` | `result` before | Characters copied this step | Cumulative copies |
| --- | --- | --- | --- | --- |
| 1 | 'a' | "" | 0 + 1 = 1 | 1 |
| 2 | 'b' | "a" | 1 + 1 = 2 | 3 |
| 3 | 'c' | "ab" | 2 + 1 = 3 | 6 |

For n characters the total copies are 1 + 2 + ... + n = n(n+1)/2, which is O(n²). `build_good`
copies n characters once: O(n).

## 7. Complexity

| Version | Time | Space | Notes |
| --- | --- | --- | --- |
| `has_dup_slow` | O(n²) | O(1) | Nested loops, no extra container |
| `has_dup_fast` | O(n) average | O(n) | Set stores up to n values |
| `build_bad` | O(n²) | O(n²) total allocations | Repeated copying |
| `build_good` | O(n) | O(n) | One final join |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Reporting code complexity instead of worst case | Wrong answer in interview | State worst case; mention early returns as best case |
| Counting input as extra space | Over-reported space | Count only containers you create |
| Calling `x in list` inside a loop and claiming O(n) | Hidden O(n²) | Use a set for membership |
| Forgetting `sorted()` is O(n log n) | Underestimated time | Include sorting cost in the total |
| Assuming dict lookups are worst-case O(1) | Overstated guarantee | State "average O(1)" |
| Building strings with `+=` in a loop | Slow on large inputs | Collect in a list, then `join` |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Running sum of 1D array** — return prefix sums in O(n) → `exercises/starter-code/running_sum.py`
2. **Complexity rewrite** — rewrite the Day 1 reverse-array and second-largest solutions with explicit complexity comments and an O(1)-space variant where possible → `exercises/starter-code/complexity_rewrite.py`

## 10. Hints

<details>
<summary>Hint 1 — for exercise 1 (running sum)</summary>

Keep a running total and append it to the output list. Each element is visited once, so the whole
thing is O(n). State the space cost of the output list.

</details>

<details>
<summary>Hint 2 — for exercise 2 (complexity rewrite)</summary>

For reverse an array, compare the in-place two-pointer version (O(1) space) with a version that
builds a new list (O(n) space). For second largest, the single-pass tracker is already O(1) space.

</details>

## 11. Solutions

- `exercises/solutions/running_sum.py`
- `exercises/solutions/complexity_rewrite.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "What is the time and space complexity of your solution?"
- **Expected answer shape:** "It runs in O(n) time because there is one pass over n elements, and
  uses O(n) extra space for the set. The worst case is the same as the average case here because
  there are no hash collisions assumed."
- **Follow-up the interviewer may ask:** "Can you reduce the space to O(1)?" (Answer: only if you
  are allowed to modify the input or sort it, which changes the time.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. Define Big-O, Big-Theta and Big-Omega in one sentence each.
2. Name the six growth classes in increasing order.
3. State the complexity of `x in list`, `x in set`, `lst.append`, `lst.insert(0, x)`.
4. Explain why `s = s + c` in a loop is quadratic.
5. Give the constraint-to-complexity link for n = 5,000.

## 14. Related lessons

- `../problem-solving/problem-solving-foundations.md` — the routine that uses this complexity analysis.
- `../../docs/complexity-cheatsheet.md` — the full Python operation cost reference.
- `../../docs/problem-solving-framework.md` — Step 7 of the routine.
