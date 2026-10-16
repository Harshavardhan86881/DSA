"""Binary search on answer: Koko eating bananas.

Run: python3 koko.py
"""
import math


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


def main() -> None:
    print(min_eating_speed([3, 6, 7, 11], 8))  # 4
    print(min_eating_speed([30, 11, 23, 4, 20], 5))  # 30
    print(min_eating_speed([30, 11, 23, 4, 20], 6))  # 23


if __name__ == "__main__":
    main()
