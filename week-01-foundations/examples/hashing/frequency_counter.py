"""Frequency counting with a dict and Counter.

Run: python3 frequency_counter.py
"""
from collections import Counter

data = [1, 2, 2, 3, 3, 3]

# Manual counting
counts: dict[int, int] = {}
for value in data:
    counts[value] = counts.get(value, 0) + 1
print("manual:", counts)

# With Counter
print("counter:", Counter(data))
print("most common 2:", Counter(data).most_common(2))
