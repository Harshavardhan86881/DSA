# Valid Palindrome II

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | two pointers, strings |
| **Target time** | 20 minutes |
| **Solution file** | [valid-palindrome-ii.py](valid-palindrome-ii.py) |

## 1. Problem statement

Given a string `s`, return `True` if it can become a palindrome by deleting at most one
character.

## 2. Constraints

- `1 ≤ s.length ≤ 10^5`
- `s` consists of lowercase English letters.

## 3. Examples

**Example 1**

```text
Input:  "aba"
Output: True
```

**Example 2**

```text
Input:  "abca"
Output: True
```

**Example 3 — edge case**

```text
Input:  "abc"
Output: False
```

## 4. Hints

<details><summary>Hint 1</summary>
Use two pointers from both ends.
</details>
<details><summary>Hint 2</summary>
On mismatch, try skipping either the left or the right character.
</details>

## 5. Brute-force approach

Try deleting each character and check palindrome. O(n²) time.

## 6. Optimised approach

Two pointers with at most one skip. O(n) time, O(1) space.

```python
def valid_palindrome_ii(s: str) -> bool:
    def is_pal(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_pal(left + 1, right) or is_pal(left, right - 1)
        left += 1
        right -= 1
    return True
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n²) | O(1) |
| Optimised | O(n) | O(1) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Empty | `""` | `True` |
| Single | `"a"` | `True` |
| Delete one | `"abca"` | `True` |
| No | `"abc"` | `False` |

```python
def test_basic():
    assert valid_palindrome_ii("aba") is True

def test_empty():
    assert valid_palindrome_ii("") is True
```

## 9. Follow-up questions

1. How would you solve Valid Palindrome (no deletions)?
2. What if you could delete up to k characters?
3. How does the helper avoid repeated work?

## 10. Related problems

- `../../exercises/starter-code/valid_palindrome_ii.py` — starter code.
- `../../lessons/two-pointers/two-pointers.md` — two pointers lesson.
