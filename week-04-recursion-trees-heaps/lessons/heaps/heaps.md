# Heaps and Priority Queues

| | |
| --- | --- |
| **Week** | 4 |
| **Topic** | Heaps |
| **Estimated time** | Concepts 45 min + implementation 45 min |
| **Prerequisites** | Trees |
| **Deliverable** | `merge_k_sorted_lists.py` attempted |

## 1. Learning objectives

1. Explain heap property.
2. Use heapq for min-heap.
3. Solve top-k problems.
4. Merge k sorted lists.

## 2. Concept explanation

A heap is a complete binary tree with heap property. Python's heapq implements a min-heap. Push/pop are O(log n). Use heaps for priority queues and top-k.

## 3. Worked examples

```python
import heapq
heap = []
heapq.heappush(heap, 5)
heapq.heappop(heap)
```

## 4. Complexity

| Operation | Time | Space |
| --- | --- | --- |
| Push/pop | O(log n) | O(n) |
| Heapify | O(n) | O(1) extra |
| Top-k | O(n log k) | O(k) |

## 5. Common mistakes

- Forgetting heapq is min-heap.
- Comparing objects without tie-breaker.
- Using sort when heap suffices.

## 6. Practice

1. Kth smallest in BST.
2. Merge k sorted lists.
