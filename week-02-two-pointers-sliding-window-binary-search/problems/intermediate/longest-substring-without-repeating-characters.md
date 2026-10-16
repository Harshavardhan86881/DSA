# Longest Substring Without Repeating Characters

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | sliding window, variable size, hashing |
| **Target time** | 30 minutes |
| **Solution file** | [longest-substring-without-repeating-characters.py](longest-substring-without-repeating-characters.py) |

## 1. Problem statement

Given a string `s`, find the length of the longest substring without repeating
characters.

## 2. Constraints

- `0 ≤ len(s) ≤ 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## 3. Examples

**Example 1**

```text
Input:  "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters.
```

**Example 2**

```text
Input:  "bbbbb"
Output: 1
```

**Example 3 — edge case**

```text
Input:  ""
Output: 0
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
n can be 5 * 10^4, so O(n²) is too slow. You need O(n).
</details>
<details><summary>Hint 2 — technique</summary>
Variable-size sliding window with a set of characters currently in the window.
</details>
<details><summary>Hint 3 — structure</summary>

```python
seen = set()
left = 0
best = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    best = max(best, right - left + 1)
```
</details>

## 5. Brute-force approach

Check every substring for uniqueness. O(n³) or O(n²) with a set. Correct but too slow.

```python
def longest_brute(s):
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best
```

## 6. Optimised approach

Variable-size sliding window. Invariant: the window `[left, right]` contains no duplicate
characters.

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
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `seen = set()` | Window state | O(1) membership |
| `left = 0` | Left edge | Shrinks when needed |
| `for right in range(len(s))` | Grow right edge | Each char enters once |
| `while s[right] in seen` | Condition violated | Duplicate in window |
| `seen.remove(s[left]); left += 1` | Shrink | Remove leftmost until valid |
| `seen.add(s[right])` | Add new char | Window now valid |
| `best = max(best, right - left + 1)` | Update answer | Window length |

## 8. Dry run

Input: `"abcabcbb"`

| Step | `right` | `s[right]` | `seen` before | Action | `left` | `best` |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | a | {} | add a | 0 | 1 |
| 1 | 1 | b | {a} | add b | 0 | 2 |
| 2 | 2 | c | {a,b} | add c | 0 | 3 |
| 3 | 3 | a | {a,b,c} | remove a, left=1; add a | 1 | 3 |
| 4 | 4 | b | {b,c,a} | remove b, left=2; add b | 2 | 3 |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n²) or O(n³) | O(k) | Nested substrings |
| Optimised | O(n) average | O(k) | Each char added/removed at most once |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `""` | `0` | No characters |
| Single | `"a"` | `1` | One character |
| All same | `"bbbbb"` | `1` | Only one unique |
| All distinct | `"abcd"` | `4` | Whole string |
| With spaces/symbols | `"a b c"` | `5` | Spaces count |

```python
def test_basic():
    assert longest_unique_substring("abcabcbb") == 3

def test_empty():
    assert longest_unique_substring("") == 0
```

## 11. Follow-up questions

1. What if you need the substring itself, not just its length? (Track start index.)
2. What if the alphabet is Unicode? (Use a dict mapping char to last index to jump left.)
3. What if at most K distinct characters are allowed? (Track counts in a dict.)

## 12. Related problems

- `../../exercises/starter-code/longest_substring_without_repeating.py` — starter code.
- `../../lessons/sliding-window/sliding-window.md` — variable window pattern.
