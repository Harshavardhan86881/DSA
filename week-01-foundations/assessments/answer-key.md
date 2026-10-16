# Week 1 Cumulative Assessment — Answer Key

Do not open until you have finished and self-graded.

## Q1 — Reverse an Array

```python
def reverse_in_place(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

Complexity: O(n) time, O(1) space.

## Q2 — Second-Largest Distinct

```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    largest = second = None
    for value in nums:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value
    return second
```

Complexity: O(n) time, O(1) space.

## Q3 — Two Sum

```python
def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
```

Complexity: O(n) time average, O(n) space.

## Q4 — Valid Palindrome

```python
def is_valid_palindrome(s):
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

Complexity: O(n) time, O(1) space.

## Q5 — Maximum Subarray

```python
def max_subarray(nums):
    if not nums:
        return 0
    best = running = nums[0]
    for value in nums[1:]:
        running = max(value, running + value)
        best = max(best, running)
    return best
```

Complexity: O(n) time, O(1) space.

## Q6 — Explanations

See the interview-application sections of the relevant lessons for the three-part answer shape.
