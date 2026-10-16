"""Runnable example: top-k with heapq."""


import heapq


def top_k_largest(nums, k):
    return heapq.nlargest(k, nums)


def kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    print(top_k_largest([3, 2, 1, 5, 6, 4], 2))
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))
