# Day 3 — Doubly Linked Lists

| | |
| --- | --- |
| **Week** | 3 |
| **Theme** | Doubly linked lists |
| **Estimated time** | 4 hours (40 + 35 + 45 + 70 + 25 + 25) |
| **Prerequisites** | Day 2 |
| **Deliverable** | Implement and test a doubly linked list |

## 1. Day objectives

1. Use `prev` and `next` references.
2. Insert at the head and tail.
3. Delete a node, including head, tail, and middle nodes.
4. Traverse forward and backward.
5. Maintain `prev`/`next` pointer consistency.
6. Compare singly and doubly linked lists.

## 2. Four-hour block

| Block | Time | Task |
| --- | --- | --- |
| Intuition and theory | 40 min | Read `lessons/doubly-linked-lists/doubly-linked-lists.md` and `lessons/linked-lists-vs-python-lists/linked-lists-vs-python-lists.md`. |
| Diagrams and dry runs | 35 min | Draw insert/delete pointer updates for head, tail, and middle nodes. |
| Guided implementation | 45 min | Implement `DNode`, `insert_after`, `delete_node`, `prepend`, and `append`. |
| Independent problem solving | 70 min | Implement a doubly linked list and test empty, single-node, head-deletion, tail-deletion, and middle-deletion cases. |
| Tests and debugging | 25 min | Test pointer consistency after every operation; debug missing `prev`/`next` updates. |
| Active recall and spoken explanation | 25 min | Explain O(1) deletion given a node and why both neighbors must be updated. |

## 3. Concepts to learn

- `prev` and `next` references.
- Head and tail maintenance.
- Insertion after/before a node.
- Deletion by node reference.
- Forward and backward traversal.
- Singly vs doubly linked list trade-offs.

## 4. Guided implementation

1. Define `DNode(value, prev=None, next=None)`.
2. Implement `prepend`, `append`, `insert_after`, and `delete_node`.
3. Update `prev` and `next` in the correct order.
4. Add `to_list_forward` and `to_list_backward`.

## 5. Practice exercises

Implement and test a doubly linked list with these cases:

1. Empty list: forward and backward traversal return `[]`.
2. Single node: delete the only node and verify both directions are empty.
3. Delete head: verify the new head has `prev is None`.
4. Delete tail: verify the new tail has `next is None`.
5. Delete middle node: verify the neighboring nodes point to each other.
6. Insert at head and tail: verify forward and backward order.
7. Insert after a middle node: verify both directions.

Keep `problems/intermediate/merge-two-sorted-lists.md` in the singly linked-list context from Day 1/Day 2; it is not the focus of this doubly linked-list day.

## 6. Common mistakes

- Updating only `next` and forgetting `prev`.
- Deleting head or tail without updating list endpoints.
- Losing a reference before reconnecting neighbors.
- Assuming deletion is O(1) without having the node reference.

## 7. Exit criteria

- [ ] Doubly linked list implemented from scratch.
- [ ] Insertion at head and tail works.
- [ ] Deletion works for empty, single, head, tail, and middle cases.
- [ ] Forward and backward traversal agree.
- [ ] `prev`/`next` consistency explained aloud.
