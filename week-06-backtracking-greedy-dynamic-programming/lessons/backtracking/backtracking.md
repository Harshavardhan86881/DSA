# Backtracking

Backtracking builds solutions incrementally and undoes choices. Template: choose, explore, un-choose. Use pruning to cut search.

## Example: subsets
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
