# Longest Repeating Character Replacement

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | sliding window, strings |
| **Target time** | 25 minutes |
| **Solution file** | [longest-repeating-character-replacement.py](longest-repeating-character-replacement.py) |

## 1. Problem statement

Given a string `s` and an integer `k`, you may change at most `k` characters to any uppercase
letter. Return the length of the longest substring containing the same letter after the
changes.

## 2. Constraints

- `1 ≤ s.length ≤ 10^5`
- `s` consists of uppercase English letters.
- `0 ≤ k ≤ s.length`

## 3. Examples

**Example 1**

```text
Input:  s = "ABAB", k = 2
Output: 4
```

**Example 2**

```text
Input:  s = "AABABBA", k = 1
Output: 4
```

**Example 3 — edge case**

```text
Input:  s = "", k = 2
Output: 0
```

## 4. Hints

<details><summary>Hint 1</summary>
Track the count of each character in the window.
</details>
<details><summary>Hint 2</summary>
The window is valid if (window length - max count) ≤ k.
</details>

## 5. Brute-force approach

Try every substring and check feasibility. O(n²) or worse.

## 6. Optimised approach

Variable sliding window with a frequency map. O(n) time, O(1) space (26 letters).

```python
def character_replacement(s: str, k: int) -> int:
    counts = {}
    left = 0
    best = 0
    max_count = 0
    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        if counts[s[right]] > max_count:
            max_count = counts[s[right]]
        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n²) | O(1) |
| Optimised | O(n) | O(1) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Empty | `"", 2` | `0` |
| All same | `"AAAA", 0` | `4` |
| k large | `"ABAB", 4` | `4` |

```python
def test_basic():
    assert character_replacement("ABAB", 2) == 4

def test_empty():
    assert character_replacement("", 2) == 0
```

## 9. Follow-up questions

1. Why is it safe to not decrement max_count when shrinking?
2. How would you handle lowercase letters?
3. What changes if k is very large?

## 10. Related problems

- `../../exercises/starter-code/longest_repeating_char_replacement.py` — starter code.
- `../../lessons/sliding-window/sliding-window.md` — sliding window lesson.
