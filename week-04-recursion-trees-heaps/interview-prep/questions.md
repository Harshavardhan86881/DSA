# Week 4 Interview Questions

Q: What is a base case?
A: The stopping condition that prevents infinite recursion.

Q: How do you compute tree height?
A: 1 + max(left height, right height), with 0 for None.

Q: Difference between DFS and BFS?
A: DFS explores depth-first; BFS explores level by level.

Q: How do you validate a BST?
A: Recursively check that each node lies within (low, high) bounds.

Q: Why is heapify O(n)?
A: Most nodes are near the bottom and require little work; total is linear.

Q: Heap vs sorted array?
A: Heap gives O(log n) insert/remove and O(1) min; sorted array gives O(1) min but O(n) insert.
