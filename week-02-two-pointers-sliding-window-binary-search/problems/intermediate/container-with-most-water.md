# Container With Most Water

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | two pointers, greedy |
| **Target time** | 30 minutes |
| **Solution file** | [container-with-most-water.py](container-with-most-water.py) |

## 1. Problem statement

Given an array `height` where `height[i]` is the height of a vertical line at position `i`,
find two lines that together with the x-axis form a container holding the most water. Return
the maximum area.

## 2. Constraints

- `2 ≤ n ≤ 10^5`
- `0 ≤ height[i] ≤ 10^4`

## 3. Examples

**Example 1**

```text
Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
```

**Example 2**

```text
Input:  [1, 1]
Output: 1
```

**Example 3 — edge case**

```text
Input:  [1, 2, 1]
Output: 2
```

## 4. Hints

<details><summary>Hint 1 — orientation</summary>
n can be 10^5, so checking all pairs (O(n²)) is too slow.
</details>
<details><summary>Hint 2 — technique</summary>
Start with the widest container. Move the pointer at the shorter line.
</details>
<details><summary>Hint 3 — structure</summary>

```python
left, right = 0, len(height) - 1
best = 0
while left < right:
    best = max(best, min(height[left], height[right]) * (right - left))
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
```
</details>

## 5. Brute-force approach

Try every pair. O(n²) time, O(1) space.

```python
def max_area_brute(height):
    best = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            best = max(best, min(height[i], height[j]) * (j - i))
    return best
```

## 6. Optimised approach

Opposite-direction pointers. Invariant: the maximum area using the current left or right
boundary has been considered. Move the shorter side because the taller side cannot improve the
area (width shrinks and height is capped by the shorter).

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        if h * width > best:
            best = h * width
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

## 7. Line-by-line explanation

| Line | What happens | Why |
| --- | --- | --- |
| `left, right = 0, len(height) - 1` | Widest container | Start with maximum width |
| `width = right - left` | Current width | Shrinks each step |
| `h = min(...)` | Limiting height | Area capped by shorter line |
| `best = max(best, h * width)` | Track best area | Update if better |
| `if height[left] < height[right]: left += 1` | Move shorter side | Taller side cannot improve area |
| `else: right -= 1` | Move right side | Symmetric case |

## 8. Dry run

Input: `[1, 8, 6, 2, 5, 4, 8, 3, 7]`

| Step | `left` | `right` | `h` | `width` | `area` | `best` | Move |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 8 | 1 | 8 | 8 | 8 | left++ (1<7) |
| 1 | 1 | 8 | 7 | 7 | 49 | 49 | right-- (8>7) |
| ... | ... | ... | ... | ... | ... | 49 | ... |

Final best = 49.

## 9. Complexity analysis

| Approach | Time | Space | Reasoning |
| --- | --- | --- | --- |
| Brute force | O(n²) | O(1) | All pairs |
| Optimised | O(n) | O(1) | One pointer moves each step |

## 10. Edge cases and tests

| Case | Input | Expected | Why it matters |
| --- | --- | --- | --- |
| Minimum input | `[1, 1]` | `1` | Two lines |
| Increasing | `[1, 2, 3]` | `2` | Best uses last two |
| Decreasing | `[3, 2, 1]` | `2` | Best uses first two |
| Zeros | `[0, 2, 0]` | `0` | Zero height |
| Empty | `[]` | `0` | No container |

```python
def test_basic():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_two():
    assert max_area([1, 1]) == 1
```

## 11. Follow-up questions

1. What if you must return the indices of the two lines?
2. What if the array is not sorted? (Two pointers still work; no sorting needed.)
3. How does this differ from "trapping rain water"?

## 12. Related problems

- `../../exercises/starter-code/container_with_most_water.py` — starter code.
- `../../lessons/two-pointers/two-pointers.md` — greedy pointer movement.
