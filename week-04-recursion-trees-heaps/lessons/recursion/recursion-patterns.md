# Recursion Patterns

| | |
| --- | --- |
| **Week** | 4 |
| **Topic** | Recursion patterns |
| **Estimated time** | Concepts 40 min + implementation 40 min |
| **Prerequisites** | Recursion |
| **Deliverable** | Re-implement max depth from memory |

## 1. Learning objectives

1. Recognize common recursion patterns.
2. Apply recursion to lists and trees.
3. Explain divide-and-conquer.
4. Convert recursion to iteration.

## 2. Patterns

### Accumulation

```python
def sum_list(nums):
    if not nums:
        return 0
    return nums[0] + sum_list(nums[1:])
```

### Divide and conquer

```python
def max_value(nums):
    if len(nums) == 1:
        return nums[0]
    mid = len(nums) // 2
    return max(max_value(nums[:mid]), max_value(nums[mid:]))
```

### Tree recursion

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

## 3. Dry run: max_depth

Tree: root with left leaf and right leaf.

- max_depth(root) = 1 + max(max_depth(left), max_depth(right))
- max_depth(left) = 1
- max_depth(right) = 1
- result = 2.

## 4. Complexity

Tree recursion visits each node once: O(n) time, O(h) auxiliary space.

## 5. Common mistakes

- Forgetting None check.
- Using O(n) slicing in list recursion.
- Not combining results correctly.

## 6. Practice

### Guided exercise 1

Trace max_depth on a single node.

### Independent exercise 1

Write `count_nodes(root)`.

### Debugging exercise

Fix:

```python
def bad_depth(root):
    return 1 + max(bad_depth(root.left), bad_depth(root.right))
```

### Prediction exercise

max_depth(None)?

Answer: 0.

## 7. Active-recall questions

1. What is accumulation?
2. What is divide and conquer?
3. Why tree recursion is O(n)?
4. Why space is O(h)?
5. How to convert to iteration?

Answers:
1. Combine first with rest.
2. Split, solve, combine.
3. Each node visited once.
4. Stack depth equals height.
5. Use explicit stack.

## 8. Interview questions

**Q:** How do you compute tree height?  
**A:** 1 + max(left height, right height), base case 0 for None.

Follow-up: Iterative version? Use BFS levels.

## 9. Spaced-repetition checklist

- Day 1: Write max_depth.
- Day 3: Write count_nodes.
- Day 7: Explain O(h) space.
- Day 14: Convert to iterative.

## 10. Explain aloud

"Tree recursion handles the current node, then delegates to children."
