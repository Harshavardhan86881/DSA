"""Demonstrate common list operations and their costs.

Run: python3 array_operations.py
"""

nums = [10, 20, 30, 40, 50]

print("indexing:", nums[2])          # O(1)
nums.append(60)                      # amortised O(1)
print("after append:", nums)
print("pop last:", nums.pop())       # O(1)
nums.insert(1, 99)                  # O(n) shift
print("after insert:", nums)
print("membership:", 30 in nums)     # O(n) scan
print("slice:", nums[1:4])           # O(k) copy
print("min/max/sum:", min(nums), max(nums), sum(nums))  # O(n) each
