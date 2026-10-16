# Valid Anagram

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | strings, frequency counting |
| **Target time** | 20 minutes |
| **Solution file** | [valid-anagram.py](valid-anagram.py) |

## 1. Problem statement

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False`
otherwise. An anagram is a rearrangement of the letters of one word to form another.

## 2. Constraints

- `0 ≤ len(s), len(t) ≤ 5 * 10^4`
- `s` and `t` consist of lowercase English letters (in this instance).

## 3. Examples

**Example 1**

```text
Input:  s = "anagram", t = "nagaram"
Output: True
```

**Example 2**

```text
Input:  s = "rat", t = "car"
Output: False
```

**Example 3 — edge case**

```text
Input:  s = "", t = ""
Output: True
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

Anagrams must have the same length. If the lengths differ, return False immediately.

</details>

<details>
<summary>Hint 2 — technique</summary>

Count characters in one string and decrement using the other. If any count goes negative, it is
not an anagram.

</details>

<details>
<summary>Hint 3 — structure</summary>

```python
if len(s) != len(t):
    return False
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
for ch in t:
    if counts.get(ch, 0) == 0:
        return False
    counts[ch] -= 1
return True
```

</details>

## 5. Brute-force approach

Sort both strings and compare. Correct and simple, but O(n log n) time due to sorting. It is the
natural first idea and shows why counting is better.

```python
def is_anagram_brute(s, t):
    return sorted(s) == sorted(t)
```

## 6. Optimised approach

Frequency counting in O(n) time. The invariant: after processing `s`, `counts` holds the exact
multiset of characters in `s`; processing `t` consumes them. If any character in `t` cannot be
consumed, the strings are not anagrams.

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `if len(s) != len(t)` | Length check | Anagrams must have equal length |
| `counts = {}` | Empty counter | Will hold character counts |
| `for ch in s` | Count characters of `s` | One pass |
| `counts[ch] = counts.get(ch, 0) + 1` | Increment count | Handles first occurrence |
| `for ch in t` | Consume characters of `t` | One pass |
| `if counts.get(ch, 0) == 0` | No remaining `ch` | `t` has a char `s` lacks |
| `counts[ch] -= 1` | Consume one occurrence | Tracks remaining counts |
| `return True` | All consumed | Counts matched exactly |

## 8. Dry run

Input: `s = "anagram"`, `t = "nagaram"`

| Step (s) | `ch` | `counts` after |
| --- | --- | --- |
| 1 | 'a' | {'a': 1} |
| 2 | 'n' | {'a': 1, 'n': 1} |
| ... | ... | ... |
| final | — | {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1} |

Then processing `t` decrements each count to zero. No count goes negative, so return True.

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force (sort) | O(n log n) | O(n) | Sorting dominates |
| Optimised (counting) | O(n) | O(k) | k = alphabet size (26 here) |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty both | `("", "")` | `True` | Trivially anagrams |
| Different lengths | `("a", "ab")` | `False` | Early length check |
| Same chars different counts | `("aabb", "ab")` | `False` | Length check catches it |
| Repeated chars | `("aabb", "bbaa")` | `True` | Counts handle repeats |
| Not anagrams | `("rat", "car")` | `False` | Different multisets |

```python
def test_basic():
    assert is_anagram("anagram", "nagaram") is True

def test_not_anagram():
    assert is_anagram("rat", "car") is False
```

## 11. Follow-up questions

1. What if the alphabet is Unicode (not just lowercase letters)? (Use a dict instead of a fixed
   array; same O(n) time.)
2. Can you do it with O(1) extra space? (Only if you may sort in place, which is O(n log n).)
3. What if you must handle case and whitespace? (Normalise both strings first.)

## 12. Related problems

- `../../exercises/starter-code/valid_anagram.py` — starter code.
- `../../lessons/strings/strings-and-immutability.md` — frequency counting.
