# Validate Binary Search Tree

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | BST |
| **Target time** | 25 minutes |
| **Solution file** | [validate-binary-search-tree.py](validate-binary-search-tree.py) |

## 1. Problem statement

Determine if a binary tree is a valid BST.

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
"""Solution for 'Validate Binary Search Tree'.
#Validate Binary Search Tree. O(n) time, O(h) space."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    def helper(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root, float("-inf"), float("inf"))
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

- `../../exercises/starter-code/validate_binary_search_tree.py` — starter code.
