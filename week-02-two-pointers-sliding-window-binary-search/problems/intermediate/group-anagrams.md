# Group Anagrams

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | sorting, hashing, strings |
| **Target time** | 25 minutes |
| **Solution file** | [group-anagrams.py](group-anagrams.py) |

## 1. Problem statement

Given an array of strings, group the anagrams together. Return the groups in any order.

## 2. Constraints

- `1 ≤ strs.length ≤ 10^4`
- `0 ≤ strs[i].length ≤ 100`
- `strs[i]` consists of lowercase English letters.

## 3. Examples

**Example 1**

```text
Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

**Example 2**

```text
Input:  [""]
Output: [[""]]
```

**Example 3 — edge case**

```text
Input:  ["a"]
Output: [["a"]]
```

## 4. Hints

<details><summary>Hint 1</summary>
Anagrams have the same sorted character sequence.
</details>
<details><summary>Hint 2</summary>
Use the sorted word as a key in a dictionary.
</details>

## 5. Brute-force approach

Compare every pair. O(n² * k log k) time.

## 6. Optimised approach

Sort each word to form a canonical key; group by key. O(n k log k) time, O(n k) space.

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    from collections import defaultdict
    groups: dict[str, list[str]] = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)
    return list(groups.values())
```

## 7. Complexity analysis

| Approach | Time | Space |
| --- | --- | --- |
| Brute force | O(n² k log k) | O(n k) |
| Optimised | O(n k log k) | O(n k) |

## 8. Edge cases and tests

| Case | Input | Expected |
| --- | --- | --- |
| Empty string | `[""]` | `[[""]]` |
| Single char | `["a"]` | `[["a"]]` |
| No anagrams | `["abc", "def"]` | `[["abc"], ["def"]]` |

```python
def test_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted([sorted(g) for g in result]) == sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
```

## 9. Follow-up questions

1. Can you use a character count tuple as the key instead of sorting? (O(n k) time.)
2. What if words contain Unicode? (Sorting still works.)
3. How would you handle case sensitivity?

## 10. Related problems

- `../../exercises/starter-code/group_anagrams.py` — starter code.
- `../../lessons/sorting-patterns/sorting-as-a-pattern.md` — the full lesson.
