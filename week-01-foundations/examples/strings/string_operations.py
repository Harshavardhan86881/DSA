"""Demonstrate common string operations and their costs.

Run: python3 string_operations.py
"""

s = "hello"

print("index:", s[1])               # O(1)
print("slice:", s[1:4])             # O(k) copy
print("concat:", s + " world")      # O(n+m)
print("lower:", s.lower())          # O(n) new string
print("contains:", "ll" in s)       # O(n) substring search
print("length:", len(s))            # O(1)
print("reversed:", s[::-1])         # O(n) copy
parts = ["a", "b", "c"]
print("join:", "".join(parts))      # O(total length)
