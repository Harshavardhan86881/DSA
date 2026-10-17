# Strings and Immutability

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Topic** | Strings |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Python strings, slicing, loops; Day 3 arrays |
| **Deliverable** | `exercises/starter-code/count_vowels.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Explain why Python strings are immutable and what that costs.
2. State the complexity of indexing, slicing, concatenation, case conversion and join.
3. Build strings efficiently with a list and `"".join`.
4. Traverse and compare strings with indices and two pointers.
5. Normalise case and whitespace for comparison.
6. Solve Valid Palindrome and Valid Anagram with stated complexity.

## 2. Prerequisites check

1. Can you index and slice a Python string? (If no, review strings.)
2. Can you state why `s = s + c` in a loop is slow? (If no, read section 4.3.)
3. Have you completed Days 1–3? (If no, read those lessons first.)

## 3. Why this matters

Strings are immutable in Python: every operation that "changes" a string builds a new one.
This single fact explains most performance bugs in beginner string code. Interviews often test
whether you know to collect parts in a list and join once. String problems also exercise two
pointers and frequency counting, two patterns that recur in Weeks 2–6. Valid Palindrome and
Valid Anagram are the canonical introductions.

## 4. Concept explanation

### 4.1 What immutability means

A string cannot be changed in place. `s[0] = 'X'` raises `TypeError`. Any "modification"
(`s.lower()`, `s + t`, `s.replace(...)`) allocates a new string and copies characters. The
original is untouched. This makes strings safe to share and hashable (usable as dict keys), but
it makes repeated concatenation expensive.

> **Mental model:** a string is a sealed envelope; to change a letter you copy the whole envelope.

### 4.2 Indexing and length

- `s[i]`: O(1).
- `len(s)`: O(1) (Python stores the length).
- Negative indices work like lists.

### 4.3 Concatenation: the trap

`s + t` costs O(len(s) + len(t)) because it copies both. Doing it in a loop:

```python
result = ""
for c in chars:
    result = result + c   # copies len(result) each time -> O(n^2)
```

For n characters the total copies are 1 + 2 + ... + n = O(n²). This is the single most common
hidden quadratic in beginner code.

### 4.4 The fix: collect, then join

```python
parts = []
for c in chars:
    parts.append(c)       # amortised O(1)
result = "".join(parts)   # one pass over total length, O(n)
```

`"".join(parts)` allocates the final string once. Use this pattern whenever you build a string
in a loop.

### 4.5 Slicing

`s[a:b]` creates a new string of length `b - a`: O(k) time and space. Slicing with a step
(`s[::-1]`) is also O(k). Reversing a string with `s[::-1]` is O(n) and allocates O(n) space.

### 4.6 Case, whitespace and character tests

- `s.lower()`, `s.upper()`: O(n), new string.
- `s.strip()`: O(n).
- `s.split(sep)`: O(n), returns a list.
- `c.isalnum()`, `c.isalpha()`, `c.isdigit()`: O(1) per character.
- `c in s` (substring): O(len(s)).

### 4.7 Traversal and two pointers

Strings support the same traversal patterns as lists. For palindromes, two pointers starting at
both ends move inward, comparing characters. The invariant: all characters outside `[left,
right]` have already been matched.

### 4.8 Frequency counting for anagrams

Two strings are anagrams iff their character counts match. Count characters in a dict (or a
fixed-size array of 26 for lowercase letters) in O(n), then compare counts. This beats sorting
(O(n log n)) and is the standard approach.

## 5. Worked examples (simple → difficult)

### Example 1 — Operation costs (simple)

```python
s = "hello"

print(s[1])            # 'e'   O(1)
print(s[1:4])          # 'ell' O(k) copy
print(s + " world")    # O(n+m) copy
print(s.lower())       # O(n) new string
print("ll" in s)       # True  O(n) substring search
print(len(s))          # 5     O(1)
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `s[1]` | Direct index | O(1) |
| `s[1:4]` | Slice copy | O(k) time and space |
| `s + " world"` | Concatenation | Copies both strings |
| `s.lower()` | New lowercased string | O(n) |
| `"ll" in s` | Substring search | O(n) |
| `len(s)` | Stored length | O(1) |

### Example 2 — Two-pointer palindrome (moderate)

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False
    print(is_palindrome(""))         # True
    print(is_palindrome("a"))        # True
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `left, right = 0, len(s) - 1` | Pointers at both ends | Covers every symmetric pair |
| `while left < right` | Loop while a pair remains | `<` skips the middle for odd lengths |
| `if s[left] != s[right]` | Compare the pair | Early return on first mismatch |
| `left += 1; right -= 1` | Move inward | Shrinks the unprocessed middle |
| `return True` | All pairs matched | Empty and single strings are palindromes |

### Example 3 — Frequency counting for anagrams (harder)

```python
from collections import Counter

# O(n log n) time, O(n) space: sort and compare.
def anagram_sort(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)

# O(n) time, O(k) space: count characters.
def anagram_count(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    counts: dict[str, int] = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True


if __name__ == "__main__":
    print(anagram_sort("listen", "silent"))   # True
    print(anagram_count("listen", "silent"))  # True
    print(anagram_count("hello", "world"))    # False
```

**Line-by-line explanation (count version)**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `if len(a) != len(b)` | Length check | Anagrams must have equal length |
| `counts[ch] = ...` | Increment count for `ch` | One pass over `a` |
| `if counts.get(ch, 0) == 0` | No remaining `ch` | `b` has a character `a` lacks |
| `counts[ch] -= 1` | Consume one occurrence | Tracks remaining counts |
| `return True` | All consumed | Counts matched exactly |

## 6. Dry-run table

Trace the two-pointer palindrome on `"abba"`.

| Step | `left` | `right` | `s[left]` | `s[right]` | Decision |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 3 | 'a' | 'a' | match, move inward |
| 1 | 1 | 2 | 'b' | 'b' | match, move inward |
| 2 | 2 | 1 | — | — | left >= right, stop, return True |

Trace `build_bad` versus `build_good` on `['a', 'b', 'c']` is in the complexity cheatsheet;
the same O(n²) versus O(n) reasoning applies to strings.

## 7. Complexity

| Operation | Time | Space | Notes |
| --- | --- | --- | --- |
| `s[i]` | O(1) | O(1) | Direct index |
| `len(s)` | O(1) | O(1) | Stored length |
| `s[a:b]` | O(k) | O(k) | Copy |
| `s + t` | O(len(s)+len(t)) | O(len(s)+len(t)) | Copy |
| `s.lower()`, `s.upper()` | O(n) | O(n) | New string |
| `s.split(sep)` | O(n) | O(n) | List of parts |
| `sep.join(parts)` | O(total length) | O(total length) | One pass |
| `c in s` (substring) | O(n) | O(1) | |
| Two-pointer palindrome | O(n) | O(1) | In-place comparison |
| Anagram by sorting | O(n log n) | O(n) | Sorting dominates |
| Anagram by counting | O(n) | O(k) | k = alphabet size |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| `s = s + c` in a loop | Slow on long strings | Collect in a list, then join |
| Forgetting strings are immutable | `TypeError: str object does not support item assignment` | Build a new string or use a list |
| Comparing without normalising case | "Racecar" fails | Call `.lower()` first |
| Ignoring spaces and punctuation | Palindrome check wrong | Filter with `isalnum()` |
| Off-by-one in two pointers | Skips or repeats the middle | Use `while left < right` |
| Assuming anagram sorting is O(n) | Underestimated time | Sorting is O(n log n) |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Valid palindrome** — check if a string reads the same forwards and backwards, ignoring case and non-alphanumeric characters → `exercises/starter-code/valid_palindrome.py`
2. **Valid anagram** — check if two strings are anagrams of each other → `exercises/starter-code/valid_anagram.py`
3. **Count vowels** — count vowels in a string in one pass → `exercises/starter-code/count_vowels.py`

## 10. Hints

<details>
<summary>Hint 1 — for exercise 1 (valid palindrome)</summary>

Use two pointers. Skip characters that are not alphanumeric. Compare lowercased characters.

</details>

<details>
<summary>Hint 2 — for exercise 2 (valid anagram)</summary>

Anagrams have equal length and equal character counts. Count characters in one string and
decrement using the other.

</details>

<details>
<summary>Hint 3 — for exercise 3 (count vowels)</summary>

Define a set of vowels for O(1) membership, then one pass counting matches.

</details>

## 11. Solutions

- `exercises/solutions/valid_palindrome.py`
- `exercises/solutions/valid_anagram.py`
- `exercises/solutions/count_vowels.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Given a string, determine if it is a palindrome, considering only
  alphanumeric characters and ignoring case."
- **Expected answer shape:** "I use two pointers from both ends, skipping non-alphanumeric
  characters and comparing lowercased characters. Each character is visited at most once, so it
  is O(n) time and O(1) extra space. On 'A man, a plan, a canal: Panama' the pointers meet in
  the middle after matching all pairs."
- **Follow-up the interviewer may ask:** "Can you do it without extra string allocation?" (Answer:
  compare in place with index arithmetic, as above.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. Why are strings immutable in Python?
2. Why is `s = s + c` in a loop quadratic?
3. What is the complexity of slicing and of join?
4. State the two-pointer palindrome invariant.
5. When does frequency counting beat sorting for anagrams?

## 14. Related lessons

- `../problem-solving/problem-solving-foundations.md` — the routine that uses this analysis.
- `../complexity/big-o-complexity.md` — growth classes and loop counting.
- `../arrays/arrays-and-lists.md` — lists and the join pattern.
- `../../docs/complexity-cheatsheet.md` — the full Python operation cost reference.
