# Linked Lists vs Python Lists

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Container trade-offs |
| **Estimated time** | Concepts 35 min + implementation 30 min |
| **Prerequisites** | Linked lists, arrays |
| **Deliverable** | Choose container for a given problem |

## 1. Learning objectives

1. Compare operation costs.
2. Choose the right container.
3. Explain why Python list is usually better.

## 2. Concept explanation

Python list is a dynamic array. Linked list is nodes and references.

Costs:

| Operation | Python list | Singly linked list |
| --- | --- | --- |
| Index access | O(1) | O(n) |
| Append | O(1) amortized | O(n) without tail, O(1) with tail |
| Prepend | O(n) | O(1) |
| Delete by index | O(n) | O(n) to find, O(1) to delete |
| Search | O(n) | O(n) |

Python lists have better cache locality and simpler code. Linked lists are useful when prepend/deletion at known nodes matter or when implementing other structures.

## 3. Real-world analogy

Python list is like a row of lockers: you can open any locker quickly. Linked list is like a treasure hunt: each clue points to the next.

## 4. Decision rules

- Need random access: Python list.
- Need many prepends: linked list or deque.
- Need queue: deque.
- Need stack: list.
- Need frequent deletion of known node: doubly linked list.

## 5. Practice

### Independent exercise 1

Choose a container for "frequent insert at front, rare access by index."

### Independent exercise 2

Choose a container for "binary search."

### Debugging exercise

Why is `list.insert(0, x)` O(n)?

### Prediction exercise

Which is faster for `x in container`? Both O(n), but list has better cache locality.

## 6. Active-recall questions

1. Python list append complexity?
2. Linked list prepend complexity?
3. Python list prepend complexity?
4. When use linked list?
5. What is cache locality?

Answers:
1. O(1) amortized.
2. O(1).
3. O(n).
4. Frequent prepend/deletion at known nodes.
5. Nearby memory access is faster.

## 7. Interview questions

**Q:** When would you use a linked list over an array?  
**A:** When you need O(1) prepend or deletion at a known node and can afford O(n) access.

Follow-up: In Python, deque often replaces linked lists.

## 8. Spaced-repetition checklist

- Day 1: Memorize cost table.
- Day 3: Explain cache locality.
- Day 7: Choose container for 3 scenarios.
- Day 14: Explain trade-offs.

## 9. Explain aloud

"Python lists are arrays with fast indexing. Linked lists trade indexing for cheap insertion at the front."
