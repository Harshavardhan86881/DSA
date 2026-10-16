# Hashing with Dictionaries and Sets

| | |
| --- | --- |
| **Week** | 1 — Foundations |
| **Topic** | Hashing |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Python dicts and sets; Day 2 complexity; Day 3 arrays |
| **Deliverable** | `exercises/starter-code/character_frequency.py` attempted and tested |

## 1. Learning objectives

After this lesson you can:

1. Explain how a hash table maps a key to a value in average O(1).
2. Choose between dict (key→value) and set (keys only).
3. Count frequencies in one pass with a dict.
4. Detect duplicates in one pass with a set.
5. State the difference between average and worst-case hashing.
6. Solve Contains Duplicate and Majority Element with stated complexity.

## 2. Prerequisites check

1. Can you create, read and update a Python dict? (If no, review dicts.)
2. Can you state the complexity of `x in set`? (If no, read section 4.)
3. Have you completed Days 1–4? (If no, read those lessons first.)

## 3. Why this matters

Hashing is the single biggest complexity win in Week 1. It turns an O(n²) nested search into
an O(n) single pass, by remembering what you have already seen. Contains Duplicate, Two Sum,
Valid Anagram and Majority Element all become one-pass problems once you store values in a set or
dict. The cost is O(n) extra space, and the guarantee is average O(1), not worst-case O(1).

## 4. Concept explanation

### 4.1 What a hash table is

A hash table stores key→value pairs in an array of "buckets". To find a key, Python computes a
hash (an integer) from the key, maps it to a bucket index, and looks there. With a good hash
function and enough buckets, each lookup touches only one bucket, so it is **average O(1)**.
If many keys collide into the same bucket, lookup degrades to O(n) (scanning the bucket).

> **Mental model:** a hash table is a row of labelled drawers; the label is computed from the key.

### 4.2 dict versus set

- **dict:** maps keys to values. Use when you need to associate data with a key (counts,
  indices, complements).
- **set:** stores keys only. Use when you only need membership ("have I seen this?").

Both are hash tables. Both give average O(1) membership/insert/delete.

### 4.3 Keys must be hashable

Keys must be immutable: numbers, strings, tuples of hashable items. Lists and dicts are not
hashable and cannot be keys. Values can be anything.

### 4.4 Average versus worst case

- Average case assumes a good hash function and a load factor below ~2/3. Python resizes to
  keep this true.
- Worst case: all keys collide → O(n) per operation. This is rare for built-in types but can
  be triggered by adversarial input.
- In interviews, state "average O(1)" for hashing. Do not claim worst-case O(1).

### 4.5 Frequency counting pattern

```python
counts = {}
for value in data:
    counts[value] = counts.get(value, 0) + 1
```

One pass, O(n) time, O(k) space where k is the number of distinct values. This replaces
nested counting loops.

### 4.6 Duplicate detection pattern

```python
seen = set()
for value in data:
    if value in seen:
        return True
    seen.add(value)
return False
```

One pass, O(n) time average, O(n) space. The set remembers what has been seen.

### 4.7 collections helpers

- `collections.Counter(data)`: builds a frequency dict in O(n).
- `collections.defaultdict(int)`: auto-creates missing keys with 0.
- `collections.Counter.most_common(k)`: O(n log k).

These are convenience wrappers; the underlying pattern is the same.

## 5. Worked examples (simple → difficult)

### Example 1 — Frequency counting (simple)

```python
from collections import Counter

data = [1, 2, 2, 3, 3, 3]

# Manual counting
counts: dict[int, int] = {}
for value in data:
    counts[value] = counts.get(value, 0) + 1
print(counts)  # {1: 1, 2: 2, 3: 3}

# With Counter
print(Counter(data))  # Counter({3: 3, 2: 2, 1: 1})
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `counts[value] = counts.get(value, 0) + 1` | Increment or initialise | `get` avoids a KeyError |
| `Counter(data)` | Build frequency dict | Convenience wrapper, same O(n) |

### Example 2 — Contains Duplicate (moderate)

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for value in nums:
        if value in seen:       # O(1) average
            return True
        seen.add(value)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))  # True
    print(contains_duplicate([1, 2, 3]))      # False
    print(contains_duplicate([]))            # False
```

**Line-by-line explanation**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `seen: set[int] = set()` | Empty set | Membership is O(1) average |
| `if value in seen` | Seen before? | Early return on first duplicate |
| `seen.add(value)` | Record value | Future duplicates caught here |
| `return False` | No duplicate found | All values were distinct |

### Example 3 — Majority Element (harder)

```python
# Brute force: O(n^2) time, O(1) space.
def majority_brute(nums: list[int]) -> int | None:
    for candidate in nums:
        if nums.count(candidate) > len(nums) // 2:
            return candidate
    return None

# Optimised: O(n) time, O(n) space.
def majority_hash(nums: list[int]) -> int | None:
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    for value, count in counts.items():
        if count > len(nums) // 2:
            return value
    return None


if __name__ == "__main__":
    print(majority_hash([3, 2, 3]))        # 3
    print(majority_hash([2, 2, 1, 1, 1, 2, 2]))  # 2
```

**Line-by-line explanation (hash version)**

| Line | What happens | Why it is written that way |
| --- | --- | --- |
| `counts[value] = ...` | Increment count | One pass over the input |
| `for value, count in counts.items()` | Scan distinct values | At most n distinct values |
| `if count > len(nums) // 2` | Majority threshold | More than half |
| `return value` | Found the majority | Only one value can exceed n/2 |

## 6. Dry-run table

Trace `contains_duplicate` on `[1, 2, 3, 1]`.

| Step | `value` | `seen` before | `value in seen`? | Action |
| --- | --- | --- | --- | --- |
| 0 | — | {} | — | initial |
| 1 | 1 | {} | False | add → {1} |
| 2 | 2 | {1} | False | add → {1, 2} |
| 3 | 3 | {1, 2} | False | add → {1, 2, 3} |
| 4 | 1 | {1, 2, 3} | True | return True |

## 7. Complexity

| Version | Time | Space | Notes |
| --- | --- | --- | --- |
| Brute-force majority | O(n²) | O(1) | `count` scans the whole list per candidate |
| Hash-based majority | O(n) | O(n) | One pass to count, one pass over distinct values |
| Contains duplicate (set) | O(n) average | O(n) | Set stores up to n values |
| Frequency counting | O(n) | O(k) | k = number of distinct values |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Assuming dict lookup is worst-case O(1) | Overstated guarantee | State "average O(1)" |
| Using a list for membership in a loop | Hidden O(n²) | Use a set |
| Using an unhashable key (list/dict) | `TypeError: unhashable type` | Use a tuple or convert to a string |
| Forgetting the majority may not exist | Returns wrong value | Check the threshold and return None |
| Counting input as extra space | Over-reported space | Count only new containers |

## 9. Practice exercises

Do these before reading the hints. Files live in `exercises/starter-code/`.

1. **Contains Duplicate** — return True if any value appears at least twice → `exercises/starter-code/contains_duplicate.py`
2. **Majority Element** — return the element appearing more than n/2 times, or None → `exercises/starter-code/majority_element.py`
3. **Character Frequency** — return a dict of character counts → `exercises/starter-code/character_frequency.py`

## 10. Hints

<details>
<summary>Hint 1 — for exercise 1 (contains duplicate)</summary>

You only need to know whether you have seen a value before. A set is enough.

</details>

<details>
<summary>Hint 2 — for exercise 2 (majority element)</summary>

Count all values in one pass, then check which count exceeds n/2. Remember the majority may not
exist.

</details>

<details>
<summary>Hint 3 — for exercise 3 (character frequency)</summary>

One pass over the string; use `counts.get(ch, 0) + 1` or `collections.Counter`.

</details>

## 11. Solutions

- `exercises/solutions/contains_duplicate.py`
- `exercises/solutions/majority_element.py`
- `exercises/solutions/character_frequency.py`

Do not open these until you have attempted the starter code for at least 25 minutes.

## 12. Interview applications

- **Question form:** "Given an array, determine if any value appears at least twice."
- **Expected answer shape:** "I scan once, storing values in a set. Membership is O(1) on
  average, so the whole thing is O(n) time and O(n) space. On `[1, 2, 3, 1]` I return True as
  soon as I see the second 1."
- **Follow-up the interviewer may ask:** "Can you do it with O(1) space?" (Answer: sort first,
  O(n log n) time, O(1) space, or use the sign-flipping trick if values are bounded and mutable.)

## 13. Review questions

Answer without looking at the lesson. If you cannot, make a flashcard.

1. How does a hash table achieve average O(1) lookup?
2. When would you use a dict instead of a set?
3. What is the worst-case complexity of a dict lookup and when does it happen?
4. Write the frequency-counting pattern from memory.
5. State the complexity of Contains Duplicate and Majority Element.

## 14. Related lessons

- `../problem-solving/problem-solving-foundations.md` — the routine that uses this analysis.
- `../complexity/big-o-complexity.md` — average versus worst case.
- `../arrays/arrays-and-lists.md` — the nested-loop version this replaces.
- `../../docs/complexity-cheatsheet.md` — dict and set operation costs.
