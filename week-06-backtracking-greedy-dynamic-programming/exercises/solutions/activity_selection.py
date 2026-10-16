"""Solution: Activity Selection. O(n log n) time, O(1) extra space."""


def max_activities(intervals):
    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    count = 0
    last_end = float("-inf")
    for start, end in intervals_sorted:
        if start >= last_end:
            count += 1
            last_end = end
    return count
