"""Sorting basics: sorted vs sort, keys, stability.

Run: python3 sort_basics.py
"""

data = [3, 1, 4, 1, 5]
print("sorted (new list):", sorted(data))
print("original unchanged:", data)
data.sort()
print("after .sort():", data)

# custom key
words = ["banana", "pie", "apple", "fig"]
print("by length:", sorted(words, key=len))
print("reverse:", sorted(words, reverse=True))

# tuples
pairs = [(2, "b"), (1, "a"), (2, "a")]
print("tuple sort:", sorted(pairs))

# stable sort
records = [("a", 2), ("b", 1), ("a", 1)]
print("stable:", sorted(records, key=lambda x: x[0]))
