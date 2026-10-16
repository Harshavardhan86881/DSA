# Maximum Depth of Binary Tree

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | trees, recursion |
| **Target time** | 20 minutes |
| **Solution file** | [max-depth-of-binary-tree.py](max-depth-of-binary-tree.py) |

## 1. Problem statement

Given root of binary tree, return its maximum depth.

## 2. Constraints

- Reasonable input sizes (see solution).

## 3. Examples

```text
See solution file.
```

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion or a queue/heap as appropriate.
</details>

## 5. Optimised approach

```python
"""Solution for 'Max Depth Of Binary Tree'.
#Maximum Depth of Binary Tree. O(n) time, O(h) space."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

## 6. Complexity analysis

See solution docstring.

## 7. Edge cases and tests

See `../../exercises/test-cases/`.

## 8. Follow-up questions

1. Can you do it iteratively?
2. What is the space complexity?
3. How does input shape affect performance?

## 9. Related problems

- `../../exercises/starter-code/max_depth_of_binary_tree.py` — starter code.
