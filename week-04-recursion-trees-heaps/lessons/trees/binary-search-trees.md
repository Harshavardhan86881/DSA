# Binary Search Trees

| | |
| --- | --- |
| **Week** | 4 |
| **Topic** | Binary search trees |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Binary trees |
| **Deliverable** | `exercises/starter-code/validate_bst.py` attempted |

## 1. Learning objectives

1. State BST invariant.
2. Search and insert.
3. Delete leaf, one child, two children.
4. Validate using bounds.
5. Find kth smallest.

## 2. BST invariant

For every node, all values in the left subtree are less than the node, and all values in the right subtree are greater. (Duplicates need a consistent policy.)

## 3. Search

```python
def search(root, target):
    if root is None:
        return None
    if target == root.val:
        return root
    if target < root.val:
        return search(root.left, target)
    return search(root.right, target)
```

## 4. Insertion

```python
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root
```

## 5. Deletion

- Leaf: remove node.
- One child: replace node with child.
- Two children: replace with inorder successor (smallest in right subtree), then delete successor.

## 6. Inorder sorted output

Inorder traversal of a valid BST yields sorted values.

## 7. Validation

Do not only compare with children. Use lower/upper bounds:

```python
def is_valid_bst(root):
    def helper(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root, float("-inf"), float("inf"))
```

## 8. Kth smallest

Inorder traversal collects sorted values; return index k-1. Time O(n), space O(n). Can be optimized with augmented trees.

## 9. Balanced vs skewed

Average case O(log n) if balanced. Worst case O(n) if skewed. An ordinary BST does not guarantee balance.

## 10. Complexity

| Operation | Average | Worst |
| --- | --- | --- |
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

## 11. Common mistakes

- Comparing only immediate children.
- Forgetting duplicate policy.
- Claiming O(log n) for unbalanced BST.
- Wrong successor in deletion.

## 12. Practice

### Guided exercise 1

Validate BST with bounds.

### Guided exercise 2

Find kth smallest.

### Independent exercise 1

Implement BST search.

### Independent exercise 2

Implement BST insert.

### Debugging exercise

Fix:

```python
def bad_valid(root):
    if root is None:
        return True
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    return bad_valid(root.left) and bad_valid(root.right)
```

### Prediction exercise

Inorder of BST [2,1,3]?

Answer: [1,2,3].

## 13. Active-recall questions

1. BST invariant?
2. Why bounds validation?
3. Deletion with two children?
4. Average search complexity?
5. Worst-case complexity?

Answers:
1. Left < node < right.
2. Child comparison is insufficient.
3. Use inorder successor.
4. O(log n).
5. O(n).

## 14. Interview questions

**Q:** How do you validate a BST?  
**A:** Recursively check that each node lies within (low, high) bounds.

Follow-up: Why not just compare children? Because a node can be greater than its parent but still violate an ancestor bound.

## 15. Spaced-repetition checklist

- Day 1: Draw BST and bounds.
- Day 3: Write validation.
- Day 7: Explain deletion.
- Day 14: Compare with hash set.

## 16. Explain aloud

"A BST keeps smaller values left and larger values right, so inorder traversal is sorted."
