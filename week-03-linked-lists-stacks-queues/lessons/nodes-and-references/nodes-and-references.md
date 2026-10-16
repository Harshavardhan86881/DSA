# Nodes and References

| | |
| --- | --- |
| **Week** | 3 — Linked lists, stacks, queues |
| **Topic** | Nodes and references |
| **Estimated time** | Concepts 40 min + implementation 35 min |
| **Prerequisites** | Python variables, objects, `None` |
| **Deliverable** | Draw and explain a 3-node list from memory |

## 1. Learning objectives

After this lesson you can:

1. Explain what a node is in plain English.
2. Draw a node with a value and a reference.
3. Explain what `head`, `next`, and `None` mean.
4. Traverse a linked list without losing the head.
5. Explain why reassigning a reference does not delete an object immediately.

## 2. Prerequisites check

1. Can you create a Python class with `__init__`? (If no, review classes.)
2. Do you know that `None` means "no object"? (If no, review `None`.)
3. Can you follow an arrow in a diagram? (If no, practice with the diagrams below.)

## 3. Why this matters

Linked lists are built from nodes and references. Every later operation—insertion, deletion, reversal, cycle detection—depends on understanding how references move. If references are unclear, pointer code feels like magic.

## 4. Build intuition

A node is a small box that holds two things:

- a value, such as `5`
- a reference to the next node

A reference is not the next node itself. It is a pointer, arrow, or address that tells Python where the next node lives. `None` means "there is no next node."

A linked list is a chain of these boxes. You only need to remember where the first box is. That first reference is called `head`.

### 4.1 Plain-English picture

Imagine three train cars:

- Car A holds value `1` and points to car B.
- Car B holds value `2` and points to car C.
- Car C holds value `3` and points to nothing.

In Python:

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
```

```python
node_c = Node(3)
node_b = Node(2, node_c)
node_a = Node(1, node_b)
head = node_a
```

Diagram:

```text
head
 |
 v
+---+---+    +---+---+    +---+---+
| 1 | o-+--->| 2 | o-+--->| 3 | / |
+---+---+    +---+---+    +---+---+
```

The `o` is the `next` reference. The `/` means `None`.

### 4.2 What `head` really is

`head` is a variable that stores a reference. It does not store the whole list. If you do:

```python
current = head
```

then `current` and `head` point to the same first node. Changing `current` to `current.next` moves your cursor, not the list.

### 4.3 Traversal

To visit every value, start at `head` and follow `next` until `None`:

```python
current = head
while current is not None:
    print(current.value)
    current = current.next
```

Why `is not None`? Because `None` is the end marker. Using `while current:` would also stop at falsy values, but node objects are truthy; still, `is not None` is clearer for linked lists.

### 4.4 Length

```python
def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count
```

Each node is visited once, so time is O(n) and auxiliary space is O(1).

## 5. Visual explanations

### Empty list

```text
head -> None
```

### One node

```text
head -> [5 | /]
```

### Two nodes

```text
head -> [5 | o] -> [7 | /]
```

### Traversal state

Input: `1 -> 2 -> 3 -> None`

| Step | current.value | current after step |
| --- | --- | --- |
| 1 | 1 | node 2 |
| 2 | 2 | node 3 |
| 3 | 3 | None |
| 4 | loop ends | None |

## 6. Python implementation

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"Node({self.value})"


def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    print_list(head)
    print("length:", length(head))
```

Expected output:

```text
1 -> 2 -> 3 -> None
length: 3
```

### Line-by-line explanation

- `class Node`: defines the box.
- `__init__`: stores `value` and `next`.
- `next_node=None`: an empty reference by default.
- `print_list`: uses `current` as a cursor so `head` is not lost.
- `current = current.next`: follows the arrow.
- `length`: counts nodes until `None`.

## 7. Correctness and complexity

Precondition: `head` is either `None` or a valid node chain ending in `None`.

Result: traversal visits each node exactly once in order.

Time: O(n), because each node is visited once.
Auxiliary space: O(1), because only `current` and `count` are used. The list itself is input space.

## 8. Debugging and edge cases

| Case | Input | Expected |
| --- | --- | --- |
| Empty | `None` | prints `None`, length 0 |
| One node | `Node(5)` | prints `5 -> None`, length 1 |
| Duplicate values | `1 -> 1 -> 1` | prints all three |

Common bug:

```python
# Wrong: loses head
head = head.next
while head is not None:
    print(head.value)
    head = head.next
```

This mutates the caller's head reference if `head` is a local variable? Actually reassigning local `head` does not change the caller's variable, but it still loses the starting point for this function. Use `current` instead.

## 9. Practice

### Guided exercise 1

Draw `head -> 4 -> 9 -> 2 -> None`. Label each `next`.

### Guided exercise 2

Predict the output:

```python
head = Node(10, Node(20))
current = head
current = current.next
print(current.value)
```

### Independent exercise 1

Write `sum_list(head)` returning the sum of all values.

Example: `1 -> 2 -> 3` → `6`.

### Independent exercise 2

Write `contains(head, target)` returning `True` if target appears.

Example: `1 -> 2 -> 3`, target `2` → `True`.

### Debugging exercise

Fix this function:

```python
def bad_length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count
```

It works, but explain why using `head` as the cursor is poor style and how to improve it.

### Prediction exercise

What is printed?

```python
a = Node(1)
b = Node(2, a)
print(b.next.value)
```

Answer: `1`.

## 10. Active-recall questions

1. What does `None` represent in a linked list?
2. What is `head`?
3. Why use `current` instead of moving `head`?
4. What is the time complexity of traversal?
5. What is the auxiliary space of traversal?

Answers:
1. No next node.
2. Reference to the first node.
3. To preserve the start of the list.
4. O(n).
5. O(1).

## 11. Interview questions

**Q:** What is a linked list node?  
**A:** An object containing a value and a reference to the next node. The list is accessed through its head.

**Q:** Why is traversal O(n)?  
**A:** Each node is visited once, and each step follows one reference.

**Q:** What happens if `head` is `None`?  
**A:** The list is empty; traversal does nothing.

Follow-up: How would you represent an empty list? `head = None`.

## 12. Spaced-repetition checklist

- Day 1: Draw a 3-node list and traverse it.
- Day 3: Re-explain `head` and `next` aloud.
- Day 7: Write traversal from memory.
- Day 14: Explain references in an interview.

## 13. Explain aloud in simple English

"A node is a box with a value and an arrow to the next box. The head is the first arrow. To read the list, follow arrows until there is no arrow."

