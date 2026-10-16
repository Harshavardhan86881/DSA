# Doubly Linked Lists

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Doubly linked lists |
| **Estimated time** | Concepts 40 min + implementation 40 min |
| **Prerequisites** | Singly linked lists |
| **Deliverable** | Explain insertion/deletion pointer updates |

## 1. Learning objectives

1. Use `prev` and `next`.
2. Insert a node.
3. Delete a node given its reference.
4. Maintain pointer consistency.

## 2. Concept explanation

A doubly linked list node has `prev` and `next`. This allows O(1) deletion if you have the node, and backward traversal.

Insertion after a node:
- new.next = node.next
- new.prev = node
- if node.next: node.next.prev = new
- node.next = new

Deletion:
- node.prev.next = node.next
- if node.next: node.next.prev = node.prev

## 3. Visual example

Insert X after A in `A <-> B`:

Before:
```text
A <-> B
```

After:
```text
A <-> X <-> B
```

## 4. Python implementation

```python
class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def insert_after(node, value):
    new_node = DNode(value, prev=node, next=node.next)
    if node.next is not None:
        node.next.prev = new_node
    node.next = new_node
    return new_node

def delete_node(node):
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
```

## 5. Dry run: delete B from A <-> B <-> C

| Step | A.next | C.prev | Result |
| --- | --- | --- | --- |
| 1 | C | A | A <-> C |
| 2 | C | A | done |

## 6. Complexity

| Operation | Time | Space |
| --- | --- | --- |
| Insert after node | O(1) | O(1) |
| Delete given node | O(1) | O(1) |
| Search | O(n) | O(1) |

## 7. Common mistakes

- Forgetting to update both neighbors.
- Forgetting head/tail updates.
- Updating in wrong order and losing references.

## 8. Practice

### Guided exercise 1

Insert X before B in `A <-> B`.

### Guided exercise 2

Delete tail node.

### Independent exercise 1

Implement `prepend` and `append`.

### Independent exercise 2

Implement `remove_value`.

### Debugging exercise

Fix:

```python
def bad_delete(node):
    node.prev.next = node.next
    node.next.prev = node.prev
```

It crashes when node is head or tail.

### Prediction exercise

After deleting the only node, what is head?

Answer: None.

## 9. Active-recall questions

1. What extra reference does a doubly node have?
2. Why is deletion O(1) given the node?
3. What must be updated on both sides?
4. What is search complexity?
5. When is doubly list useful?

Answers:
1. prev.
2. No traversal needed.
3. prev.next and next.prev.
4. O(n).
5. When backward traversal or O(1) deletion needed.

## 10. Interview questions

**Q:** Difference between singly and doubly linked list?  
**A:** Doubly has prev and next; enables backward traversal and O(1) deletion given node, but uses more memory.

Follow-up: When is singly preferred? When memory matters and only forward traversal needed.

## 11. Spaced-repetition checklist

- Day 1: Draw pointer updates.
- Day 3: Write insert_after.
- Day 7: Explain deletion.
- Day 14: Compare with singly.

## 12. Explain aloud

"Update the new node first, then its neighbors, so no reference is lost."
