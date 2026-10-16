# Singly Linked Lists

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Singly linked lists |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Nodes and references |
| **Deliverable** | `exercises/starter-code/reverse_linked_list.py` attempted |

## 1. Learning objectives

1. Insert at head and tail.
2. Delete a node by value.
3. Search for a value.
4. Compute length.
5. State complexity for each operation.

## 2. Why this matters

Singly linked lists are the simplest pointer structure. They teach how to update references safely.

## 3. Concept explanation

A singly linked list has nodes with one `next` reference. The head points to the first node. The last node points to `None`.

### Insert at head

Create a new node whose `next` is the current head, then move head to the new node.

```python
new_node = Node(value, head)
head = new_node
```

### Insert at tail

Traverse to the last node, then set its `next` to the new node. If the list is empty, the new node becomes head.

### Delete by value

Find the node before the target, then skip the target:

```python
prev.next = prev.next.next
```

If the target is the head, move head to head.next.

### Search

Traverse and compare values.

## 4. Visual examples

Insert 0 at head of `1 -> 2`:

Before:
```text
head -> [1] -> [2] -> None
```

After:
```text
head -> [0] -> [1] -> [2] -> None
```

Delete 1 from `0 -> 1 -> 2`:

Before:
```text
[0] -> [1] -> [2]
```

After:
```text
[0] -> [2]
```

## 5. Python implementation

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def delete_value(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is None:
            return False
        current.next = current.next.next
        return True

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
```

## 6. Dry run: delete value 2 from 1 -> 2 -> 3

| Step | current.value | current.next.value | Action |
| --- | --- | --- | --- |
| 1 | 1 | 2 | move current to 1 |
| 2 | 1 | 2 | target found at next |
| 3 | 1 | 3 | skip node 2 |

Result: `1 -> 3`.

## 7. Complexity

| Operation | Time | Space |
| --- | --- | --- |
| Prepend | O(1) | O(1) |
| Append without tail | O(n) | O(1) |
| Delete by value | O(n) | O(1) |
| Search | O(n) | O(1) |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Not handling empty list | Crash | Check `head is None` |
| Not handling head deletion | Wrong head | Update `head` first |
| Traversing past None | Crash | Stop at None |

## 9. Practice

### Guided exercise 1

Insert 0 at head of `1 -> 2`. Draw before and after.

### Guided exercise 2

Delete the tail from `1 -> 2 -> 3`.

### Independent exercise 1

Write `count_occurrences(head, value)`.

### Independent exercise 2

Write `insert_at_index(head, index, value)`.

### Debugging exercise

Fix:

```python
def bad_append(head, value):
    current = head
    while current is not None:
        current = current.next
    current.next = Node(value)
```

It crashes on empty list and on non-empty list. Explain why.

### Prediction exercise

What is the list after `prepend(5)` on `1 -> 2`?

Answer: `5 -> 1 -> 2`.

## 10. Active-recall questions

1. How do you insert at head?
2. How do you append without a tail pointer?
3. How do you delete the head?
4. What is append complexity without tail?
5. What is delete complexity?

Answers:
1. `Node(value, head); head = new_node`.
2. Traverse to last node, set next.
3. `head = head.next`.
4. O(n).
5. O(n).

## 11. Interview questions

**Q:** How do you insert at the head?  
**A:** Create a node pointing to the current head, then update head.

**Q:** Why is append O(n) without a tail?  
**A:** You must traverse to the last node.

Follow-up: How to make append O(1)? Keep a tail reference.

## 12. Spaced-repetition checklist

- Day 1: Draw insert/delete.
- Day 3: Write append from memory.
- Day 7: Explain head update.
- Day 14: Compare with Python list.

## 13. Explain aloud

"Insert at head is O(1) because you only change one reference. Delete needs the previous node so you can skip the target."
