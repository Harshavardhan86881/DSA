# Invert Binary Tree

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | trees |
| **Target time** | 20 minutes |
| **Solution file** | [invert-binary-tree.py](invert-binary-tree.py) |

## 1. Problem statement

Invert a binary tree.

## 2. Constraints

- Reasonable tree/list sizes.

## 3. Examples

See solution file for example.

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion or a queue/heap as appropriate.
</details>

## 5. Optimised approach

```python
"""Solution for 'Invert Binary Tree'.
#Invert Binary Tree. O(n) time, O(h) space."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
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

- `../../exercises/starter-code/invert_binary_tree.py` — starter code.
