"""Runnable example: greedy activity selection."""


def max_activities(intervals):
    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    count = 0
    last_end = float("-inf")
    for start, end in intervals_sorted:
        if start >= last_end:
            count += 1
            last_end = end
    return count


if __name__ == "__main__":
    print(max_activities([(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]))
