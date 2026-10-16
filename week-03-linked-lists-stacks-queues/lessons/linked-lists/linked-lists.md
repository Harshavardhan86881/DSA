# Linked Lists

| | |
| --- | --- |
| **Week** | 3 — Linked lists, stacks, queues |
| **Topic** | Linked lists |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Week 1 arrays and complexity |
| **Deliverable** | `exercises/starter-code/reverse_linked_list.py` attempted |

## 1. Learning objectives

After this lesson you can:

1. Define a node with a value and a next reference.
2. Insert, delete, and traverse a singly linked list.
3. Reverse a linked list iteratively and recursively.
4. Detect a cycle with fast and slow pointers.
5. Explain linked-list versus Python list trade-offs.

## 2. Prerequisites check

1. Can you use Python classes? (If no, review classes.)
2. Do you understand references? (If no, read section 3.)

## 3. Why this matters

Linked lists test pointer manipulation. They appear in stacks, queues, graphs, and interview questions about references.

## 4. Concept explanation

### 4.1 Node and reference

A node stores a value and a reference to the next node. The list is reached through its head. An empty list has `head = None`.

### 4.2 Singly linked list operations

- Prepend: O(1).
- Append: O(n) without tail, O(1) with tail.
- Delete by value: O(n).
- Traverse: O(n).

### 4.3 Doubly linked list

Each node has `prev` and `next`, enabling O(1) deletion given the node.

### 4.4 Reversal

Iterative reversal uses prev/current/next. Recursive reversal reverses the tail first, then fixes pointers.

### 4.5 Cycle detection

Fast and slow pointers: if they meet, a cycle exists. To find the start, reset one pointer to head and move both one step.

## 5. Worked examples

### Example 1 — Reverse iteratively

```python
def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
```

### Example 2 — Cycle detection

```python
def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## 6. Dry-run table

Reverse `1 -> 2 -> 3`:

| Step | prev | current | nxt | Resulting links |
| --- | --- | --- | --- | --- |
| 0 | None | 1 | 2 | 1->2->3 |
| 1 | 1 | 2 | 3 | 1<-2->3 |
| 2 | 2 | 3 | None | 1<-2<-3 |
| 3 | 3 | None | - | 3->2->1 |

## 7. Complexity

| Operation | Time | Space |
| --- | --- | --- |
| Traverse | O(n) | O(1) |
| Reverse iterative | O(n) | O(1) |
| Reverse recursive | O(n) | O(n) |
| Cycle detection | O(n) | O(1) |

## 8. Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Losing next reference | Data loss | Save `nxt` first |
| Wrong fast condition | Crash | Check `fast` and `fast.next` |
| Mutating input unexpectedly | Side effects | Document behaviour |

## 9. Practice exercises

1. Reverse Linked List → `exercises/starter-code/reverse_linked_list.py`
2. Middle of Linked List → `exercises/starter-code/middle_of_linked_list.py`
3. Merge Two Sorted Lists → `exercises/starter-code/merge_two_sorted_lists.py`
4. Linked List Cycle → `exercises/starter-code/has_cycle.py`

## 10. Hints

<details><summary>Hint 1</summary>
Save the next pointer before overwriting it.
</details>
