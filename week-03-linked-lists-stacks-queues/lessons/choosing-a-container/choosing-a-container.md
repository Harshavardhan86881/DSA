# Choosing the Right Container

| | |
| --- | --- |
| **Week** | 3 |
| **Topic** | Container choice |
| **Estimated time** | Concepts 35 min + practice 40 min |
| **Prerequisites** | Linked lists, stacks, queues |
| **Deliverable** | Choose container for 5 scenarios |

## 1. Learning objectives

1. Choose by required operations.
2. State operation costs.
3. Avoid wrong container.

## 2. Concept explanation

Choose based on the operations used most often.

| Need | Container |
| --- | --- |
| Random access | Python list |
| Stack | Python list |
| Queue | collections.deque |
| Frequent prepend | deque or linked list |
| Frequent deletion at known node | Doubly linked list |
| Next greater/smaller | Monotonic stack |

## 3. Decision process

1. List required operations.
2. Find their costs for each container.
3. Pick the container with acceptable total cost.
4. Consider simplicity and cache locality.

## 4. Practice

### Independent exercise 1

Container for "frequent insert front, rare index access."

### Independent exercise 2

Container for "binary search."

### Independent exercise 3

Container for "BFS."

### Debugging exercise

Why is `list.insert(0, x)` slow?

### Prediction exercise

Best container for undo? Stack.

## 5. Active-recall questions

1. Queue container?
2. Stack container?
3. Random access?
4. Frequent prepend?
5. Cache locality?

Answers:
1. deque.
2. list.
3. list.
4. deque/linked list.
5. list.

## 6. Interview questions

**Q:** How do you choose a container?  
**A:** By required operations and their costs.

Follow-up: In Python, deque often replaces linked lists.

## 7. Spaced-repetition checklist

- Day 1: Memorize table.
- Day 3: Choose for 3 scenarios.
- Day 7: Explain cache locality.
- Day 14: Review costs.

## 8. Explain aloud

"Choose the container whose expensive operations are the ones you rarely use."
