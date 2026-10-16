"""Solution for 'Koko Eating Bananas'. O(n log max) time, O(1) space."""


def min_eating_speed(piles: list[int], h: int) -> int:
    def feasible(k: int) -> bool:
        hours = sum((p + k - 1) // k for p in piles)
        return hours <= h

    left, right = 1, max(piles)
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    print(min_eating_speed([3, 6, 7, 11], 8))  # 4
