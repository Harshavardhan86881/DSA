# Backtracking

| | |
| --- | --- |
| **Week** | 6 |
| **Topic** | Backtracking |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Recursion |
| **Deliverable** | `subsets.py` attempted |

## 1. Learning objectives

1. Use choose/explore/un-choose.
2. Generate subsets and permutations.
3. Prune search.
4. Handle duplicates.

## 2. Concept explanation

Backtracking builds candidates incrementally. At each step, choose a value, recurse, then undo. Pruning rejects invalid partial solutions early.

## 3. Worked example

```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return result
```

## 4. Dry run

nums=[1,2]:
- path [] -> [1] -> [1,2] -> backtrack -> [2].

## 5. Complexity

| Problem | Time | Space |
| --- | --- | --- |
| Subsets | O(n 2^n) | O(n) |
| Permutations | O(n n!) | O(n) |

## 6. Common mistakes

- Forgetting to copy path (`path[:]`).
- Forgetting to un-choose (`path.pop()`).
- Duplicate results without skip.

## 7. Practice

1. Subsets.
2. Permutations.
3. Combination sum.
