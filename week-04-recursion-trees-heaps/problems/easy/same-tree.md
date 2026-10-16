# Same Tree

| | |
| --- | --- |
| **Difficulty** | easy |
| **Topics** | trees |
| **Target time** | 15 minutes |
| **Solution file** | [same-tree.py](same-tree.py) |

## 1. Problem statement

Check if two binary trees are the same.

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
"""Solution for 'Same Tree'.
#Same Tree. O(n) time, O(h) space."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if p is None or q is None:
        return p is q
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
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

- `../../exercises/starter-code/same_tree.py` — starter code.
