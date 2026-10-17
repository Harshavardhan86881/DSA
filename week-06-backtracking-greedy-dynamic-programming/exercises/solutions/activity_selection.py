"""Solution: Activity Selection. O(n log n) time, O(1) extra space.

Interval semantics: an activity ending at t can be followed by one starting at t.
"""


def max_activities(intervals):
    ordered = sorted(intervals, key=lambda interval: interval[1])
    count = 0
    last_end = float("-inf")
    for start, end in ordered:
        if start >= last_end:
            count += 1
            last_end = end
    return count


if __name__ == "__main__":
    print(max_activities([(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]))
