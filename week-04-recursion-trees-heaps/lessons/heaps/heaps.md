# Heaps and Priority Queues

| | |
| --- | --- |
| **Week** | 4 |
| **Topic** | Heaps |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Binary trees |
| **Deliverable** | `exercises/starter-code/merge_k_sorted_lists.py` attempted |

## 1. Learning objectives

1. Explain heap property.
2. Use heapq.
3. Solve top-k.
4. Merge k sorted lists.

## 2. Concept explanation

A heap is a complete binary tree with heap property. Python's heapq implements a min-heap. A heap is not fully sorted; only the root is guaranteed minimum.

## 3. Operations

- `heappush`: O(log n)
- `heappop`: O(log n)
- `heapify`: O(n)
- Peek: O(1)

## 4. Code

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappop(heap)
heapq.heapify(heap)
```

## 5. Top-k

Use a min-heap of size k for k largest. For k smallest, use max-heap (negate values) or nlargest/nsmallest.

## 6. Merge k sorted lists

Push first node of each list with (value, index, node). Pop smallest, push its next. Index avoids comparing nodes.

## 7. Complexity

| Operation | Time |
| --- | --- |
| Push/pop | O(log n) |
| Heapify | O(n) |
| Top-k | O(n log k) |
| Merge k lists | O(n log k) |

## 8. Common mistakes

- Forgetting heapq is min-heap.
- Comparing objects without tie-breaker.
- Claiming heapify is O(n log n).

## 9. Practice

### Guided exercise 1

Heapify [3,1,2] and pop all.

### Guided exercise 2

Find 2 largest in [3,2,1,5,6,4].

### Independent exercise 1

Implement kth largest.

### Independent exercise 2

Merge k sorted lists.

### Debugging exercise

Fix:

```python
heapq.heappush(heap, (node.val, node))
```

Node comparison may fail.

### Prediction exercise

heapq.heappop on min-heap returns? Smallest.

## 10. Active-recall questions

1. Heap property?
2. heapq type?
3. Push complexity?
4. Heapify complexity?
5. Top-k complexity?

Answers:
1. Parent <= children (min-heap).
2. Min-heap.
3. O(log n).
4. O(n).
5. O(n log k).

## 11. Interview questions

**Q:** Heap vs sorted array?
**A:** Heap gives O(log n) insert/remove and O(1) min; sorted array gives O(1) min but O(n) insert.

Follow-up: When use heap? Streaming top-k.

## 12. Spaced-repetition checklist

- Day 1: Draw heap.
- Day 3: Write top-k.
- Day 7: Explain heapify.
- Day 14: Compare with sorting.

## 13. Explain aloud

"A heap keeps the smallest at the top. It is not sorted, but it is efficient for repeated min extraction."
