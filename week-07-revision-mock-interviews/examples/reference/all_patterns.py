"""Compact reference implementations for self-check."""


def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bfs(graph, start):
    from collections import deque
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        for nb in graph.get(node, []):
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
    return visited


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4], 3))
    print(bfs({0: [1], 1: [2], 2: []}, 0))
