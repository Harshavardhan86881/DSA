# Valid Palindrome

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | strings, two pointers |
| **Target time** | 25 minutes |
| **Solution file** | [valid-palindrome.py](valid-palindrome.py) |

## 1. Problem statement

Given a string `s`, return `True` if it is a palindrome, considering only alphanumeric
characters and ignoring case. A palindrome reads the same forwards and backwards.

## 2. Constraints

- `0 ≤ len(s) ≤ 2 * 10^5`
- `s` consists of printable ASCII characters.

## 3. Examples

**Example 1**

```text
Input:  "A man, a plan, a canal: Panama"
Output: True
```

**Example 2**

```text
Input:  "race a car"
Output: False
```

**Example 3 — edge case**

```text
Input:  ""
Output: True
```

## 4. Hints (read only after 10 minutes of thinking)

<details>
<summary>Hint 1 — orientation</summary>

n can be 2 * 10^5, so building a filtered copy (O(n) space) is acceptable, but an in-place
two-pointer check uses O(1) extra space.

</details>

<details>
<summary>Hint 2 — technique</summary>

Two pointers from both ends. Skip non-alphanumeric characters. Compare lowercased characters.

</details>

<details>
<summary>Hint 3 — structure</summary>

```python
left, right = 0, len(s) - 1
while left < right:
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1
    if s[left].lower() != s[right].lower():
        return False
    left += 1
    right -= 1
return True
```

</details>

## 5. Brute-force approach

Filter the string to alphanumeric characters, lowercase it, and compare with its reverse. Correct
and simple, but uses O(n) extra space for the filtered copy and the reversed copy.

```python
def is_valid_palindrome_brute(s):
    filtered = "".join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]
```

## 6. Optimised approach

Two pointers moving inward, skipping non-alphanumeric characters and comparing lowercased pairs.
The invariant: all characters outside `[left, right]` have already been matched.

```python
def is_valid_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `left, right = 0, len(s) - 1` | Pointers at both ends | Covers every symmetric pair |
| `while left < right and not s[left].isalnum()` | Skip non-alphanumeric on the left | Only letters and digits matter |
| `while left < right and not s[right].isalnum()` | Skip non-alphanumeric on the right | Same reason |
| `if s[left].lower() != s[right].lower()` | Compare the pair | Case is ignored |
| `return False` | Mismatch found | Early exit |
| `left += 1; right -= 1` | Move inward | Shrinks the unprocessed middle |
| `return True` | All pairs matched | Empty and single strings are palindromes |

## 8. Dry run

Input: `"A man, a plan, a canal: Panama"` (simplified to `"AmanaplanacanalPanama"` mentally)

| Step | `left` | `right` | chars compared | Decision |
| --- | --- | --- | --- | --- |
| 0 | 0 | last | 'A' vs 'a' | match (case-insensitive) |
| 1 | 1 | last-1 | 'm' vs 'm' | match |
| ... | ... | ... | ... | continue |
| final | mid | mid | — | left >= right, return True |

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force (filter + reverse) | O(n) | O(n) | Filtered copy and reversed copy |
| Optimised (two pointers) | O(n) | O(1) | In-place comparison, early exit |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Empty | `""` | `True` | Loop does not run |
| Single char | `"a"` | `True` | Trivially a palindrome |
| Mixed case | `"RaceCar"` | `True` | Case must be ignored |
| Spaces/punctuation | `"A man, a plan, a canal: Panama"` | `True` | Non-alphanumeric skipped |
| Not a palindrome | `"race a car"` | `False` | First mismatch exits early |

```python
def test_basic():
    assert is_valid_palindrome("A man, a plan, a canal: Panama") is True

def test_not_palindrome():
    assert is_valid_palindrome("race a car") is False
```

## 11. Follow-up questions

1. What if you must handle Unicode letters? (`str.isalnum()` already covers Unicode.)
2. Can you do it with a single pass and no index arithmetic? (Use a filtered list, O(n) space.)
3. What changes if the string is a stream?

## 12. Related problems

- `../../exercises/starter-code/valid_palindrome.py` — starter code.
- `../../lessons/strings/strings-and-immutability.md` — two-pointer pattern.
