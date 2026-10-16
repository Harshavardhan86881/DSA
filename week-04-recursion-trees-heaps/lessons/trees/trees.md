# Trees and Traversals

| | |
| --- | --- |
| **Week** | 4 |
| **Topic** | Trees |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Recursion |
| **Deliverable** | `invert_binary_tree.py` attempted |

## 1. Learning objectives

1. Define a binary tree node.
2. Implement preorder, inorder, postorder, level order.
3. Explain height and depth.
4. Validate a BST.

## 2. Concept explanation

A binary tree node has value, left, right. Traversal order:
- Preorder: root, left, right.
- Inorder: left, root, right.
- Postorder: left, right, root.
- Level order: BFS by levels.

BST invariant: left subtree values < root < right subtree values.

## 3. Worked examples

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

## 4. Dry run

Tree 1(2,3):
- Preorder: [1,2,3]
- Inorder: [2,1,3]
- Postorder: [2,3,1]
- Level: [1,2,3]

## 5. Complexity

| Traversal | Time | Space |
| --- | --- | --- |
| DFS recursive | O(n) | O(h) |
| Level order | O(n) | O(n) |

## 6. Common mistakes

- Forgetting None checks.
- Confusing traversal orders.
- BST bounds not updated.

## 7. Practice

1. Invert binary tree.
2. Level order traversal.
3. Validate BST.
