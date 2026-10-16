# Kth Smallest Element in a BST

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | BST |
| **Target time** | 20 minutes |
| **Solution file** | [kth-smallest-element-in-a-bst.py](kth-smallest-element-in-a-bst.py) |

## 1. Problem statement

Return the kth smallest element in a BST.

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
"""Solution for 'Kth Smallest Element In A Bst'.
#Kth Smallest Element in a BST. O(n) time, O(h) space."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    result = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result[k - 1]
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

- `../../exercises/starter-code/kth_smallest_element_in_a_bst.py` — starter code.
