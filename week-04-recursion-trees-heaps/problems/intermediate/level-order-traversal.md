# Binary Tree Level Order Traversal

| | |
| --- | --- |
| **Difficulty** | intermediate |
| **Topics** | trees, queues |
| **Target time** | 20 minutes |
| **Solution file** | [level-order-traversal.py](level-order-traversal.py) |

## 1. Problem statement

Return level order traversal of a binary tree.

## 2. Constraints

- Reasonable input sizes (see solution).

## 3. Examples

```text
[[3], [9, 20], [15, 7]]
```

## 4. Hints

<details><summary>Hint 1</summary>
Use recursion or a queue/heap as appropriate.
</details>

## 5. Optimised approach

```python
"""Solution for 'Level Order Traversal'.
#Binary Tree Level Order Traversal. O(n) time, O(n) space."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
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

- `../../exercises/starter-code/level_order_traversal.py` — starter code.
