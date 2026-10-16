# Next Greater Element I

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | stacks, monotonic stack |
| **Target time** | 20 minutes |
| **Solution file** | [next-greater-element.py](next-greater-element.py) |

## 1. Problem statement

For each element in nums1, find the next greater element in nums2. Return -1 if none.

## 2. Constraints

- `1 ≤ nums1.length ≤ nums2.length ≤ 1000`

## 3. Examples

**Example 1**

```text
Input: nums1=[4,1,2], nums2=[1,3,4,2]
Output: [-1,3,-1]
```

**Example 2 — edge case**

```text
nums1 empty -> []
```

## 4. Hints

<details><summary>Hint 1</summary>
Use a monotonic decreasing stack over nums2.
</details>
<details><summary>Hint 2</summary>
Map each value to its next greater.
</details>

## 5. Brute-force approach

A direct approach is possible; see the optimised solution.

## 6. Optimised approach

```python
"""Solution for 'Next Greater Element I'. O(n + m) time, O(n + m) space."""


def next_greater_element(nums1, nums2):
    greater = {}
    stack = []
    for value in nums2:
        while stack and stack[-1] < value:
            greater[stack.pop()] = value
        stack.append(value)
    for value in stack:
        greater[value] = -1
    return [greater.get(v, -1) for v in nums1]
```

## 7. Complexity analysis

O(n + m) time, O(n + m) space.

## 8. Edge cases and tests

See `../../exercises/test-cases/` for automated tests.

## 9. Follow-up questions

1. How would you change the approach for a very large input?
2. What is the space complexity and can it be reduced?
3. How would you test this function thoroughly?

## 10. Related problems

- `../../exercises/starter-code/next_greater_element.py` — starter code.
- `../../lessons/linked-lists/linked-lists.md` — lesson.
