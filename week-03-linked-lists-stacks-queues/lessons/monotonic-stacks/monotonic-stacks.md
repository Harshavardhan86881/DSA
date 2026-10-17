# Monotonic Stacks

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Monotonic stacks |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Stacks |
| **Deliverable** | `next_greater_element.py` attempted |

## 1. Learning objectives

1. Solve next greater element.
2. Explain why elements are popped.
3. Derive O(n) time.

## 2. Concept explanation

A monotonic stack maintains values in increasing or decreasing order. For next greater element, use a decreasing stack of indices. When a larger value arrives, pop all smaller values; the larger value is their next greater.

Each element is pushed once and popped at most once, so total time is O(n).

## 3. Visual example

nums = [2,1,2,4,3]

Stack indices:
- i=0: stack [0] (value 2)
- i=1: stack [0,1] (values 2,1)
- i=2: value 2 pops index 1 (value 1), stack [0,2]
- i=3: value 4 pops indices 2,0, stack [3]
- i=4: stack [3,4]

Result: [4,2,4,-1,-1].

## 4. Code

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            idx = stack.pop()
            result[idx] = value
        stack.append(i)
    return result
```

## 5. Dry run table

| i | value | stack before | popped | result update | stack after |
| --- | --- | --- | --- | --- | --- |
| 0 | 2 | [] | none | - | [0] |
| 1 | 1 | [0] | none | - | [0,1] |
| 2 | 2 | [0,1] | 1 | result[1]=2 | [0,2] |
| 3 | 4 | [0,2] | 2,0 | result[2]=4,result[0]=4 | [3] |
| 4 | 3 | [3] | none | - | [3,4] |

## 6. Correctness and complexity

Precondition: input list.

Result: result[i] is next greater element or -1.

Time: O(n), each index pushed/popped once.
Space: O(n).

## 7. Common mistakes

- Comparing indices instead of values.
- Using strict vs non-strict inequality incorrectly.
- Forgetting remaining stack gets -1.

## 8. Practice

### Guided exercise 1

Trace next greater on [3,2,1].

### Guided exercise 2

What is popped when value 5 arrives to stack values [4,2]?

### Independent exercise 1

Implement next greater element.

### Independent exercise 2

Implement next smaller element.

### Debugging exercise

Fix:

```python
def bad(nums):
    stack = []
    for i, value in enumerate(nums):
        while stack and stack[-1] < value:
            result[stack.pop()] = value
        stack.append(value)
    return result
```

### Prediction exercise

For [1,2,3], result?

Answer: [2,3,-1].

## 9. Active-recall questions

1. What does the stack store?
2. Why pop smaller values?
3. Why O(n)?
4. What happens to unpopped indices?
5. Strict or non-strict?

Answers:
1. Indices.
2. They have found their next greater.
3. Each pushed/popped once.
4. They get -1.
5. Use `<` for next greater.

## 10. Interview questions

**Q:** How do you find next greater element in O(n)?  
**A:** Monotonic decreasing stack; pop when a larger value arrives.

Follow-up: What if duplicates? Decide strictness.

## 11. Spaced-repetition checklist

- Day 1: Draw stack.
- Day 3: Write from memory.
- Day 7: Explain O(n) bound.
- Day 14: Solve next smaller.

## 12. Explain aloud

"Keep a stack of values waiting for a bigger number. When a bigger number arrives, it is the answer for all smaller waiting values."
