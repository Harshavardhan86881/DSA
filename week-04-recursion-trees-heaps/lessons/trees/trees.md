# Trees and Traversals

A binary tree node has value, left, and right. Traversals: preorder, inorder, postorder, level order. BST invariant: left < root < right.

## Example
```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```
