"""Runnable example: greedy activity selection.

Lesson: ../../lessons/greedy/greedy.md
Interval semantics: an activity ending at t can be followed by one starting at t.
Complexity: O(n log n) time, O(1) extra space.
"""


def max_activities(intervals):
    """Return the maximum number of non-overlapping intervals."""
    ordered = sorted(intervals, key=lambda interval: interval[1])
    count = 0
    last_end = float("-inf")
    for start, end in ordered:
        if start >= last_end:
            count += 1
            last_end = end
    return count


if __name__ == "__main__":
    intervals = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
    print(max_activities(intervals))
    print("back-to-back allowed:", max_activities([(1, 2), (2, 3)]))
