# Binary Trees

| | |
| --- | --- |
| **Week** | 4 |
| **Topic** | Binary trees |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Recursion |
| **Deliverable** | `exercises/starter-code/invert_binary_tree.py` attempted |

## 1. Learning objectives

1. Define tree terms.
2. Implement a binary tree node.
3. Implement preorder, inorder, postorder, level order.
4. Compute depth and count nodes.
5. Explain traversal outputs.

## 2. Terminology

- Root: top node.
- Node: contains value and children.
- Edge: connection between nodes.
- Parent/child/sibling.
- Leaf: node with no children.
- Subtree: node and descendants.
- Depth: distance from root.
- Height: max distance to leaf.
- Size: number of nodes.

## 3. Node implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## 4. Example tree

```text
        1
       / \
      2   3
     / \
    4   5
```

## 5. Traversals

Preorder: root, left, right → `[1,2,4,5,3]`
Inorder: left, root, right → `[4,2,5,1,3]`
Postorder: left, right, root → `[4,5,2,3,1]`
Level order: by levels → `[[1],[2,3],[4,5]]`

## 6. Code

```python
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

from collections import deque
def level_order(root):
    if root is None:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result
```

## 7. Iterative DFS

```python
def preorder_iterative(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

## 8. Complexity

| Traversal | Time | Auxiliary space |
| --- | --- | --- |
| DFS recursive | O(n) | O(h) |
| DFS iterative | O(n) | O(h) |
| Level order | O(n) | O(n) worst case |

## 9. Common mistakes

- Forgetting None checks.
- Confusing traversal order.
- Using `pop(0)` instead of deque.
- Claiming level order is O(1) space.

## 10. Practice

### Guided exercise 1

Trace all four traversals on the example tree.

### Guided exercise 2

Compute height and size.

### Independent exercise 1

Implement `max_depth`.

### Independent exercise 2

Implement `invert_tree`.

### Debugging exercise

Fix:

```python
def bad_inorder(root):
    return bad_inorder(root.left) + [root.val] + bad_inorder(root.right)
```

### Prediction exercise

Inorder of BST gives sorted values. True/False?

Answer: True.

## 11. Active-recall questions

1. Preorder order?
2. Inorder order?
3. Postorder order?
4. Level order data structure?
5. DFS space?

Answers:
1. Root, left, right.
2. Left, root, right.
3. Left, right, root.
4. Queue.
5. O(h).

## 12. Interview questions

**Q:** Difference between DFS and BFS?  
**A:** DFS explores depth-first; BFS explores level by level.

Follow-up: Which finds shortest path in unweighted graph? BFS.

## 13. Spaced-repetition checklist

- Day 1: Draw tree and traversals.
- Day 3: Write inorder recursively.
- Day 7: Write level order iteratively.
- Day 14: Explain O(h) space.

## 14. Explain aloud

"Preorder visits the node first. Inorder visits left, then node, then right. Postorder visits children first."
