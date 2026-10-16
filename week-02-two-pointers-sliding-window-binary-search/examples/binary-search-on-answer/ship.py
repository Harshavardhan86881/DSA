"""Binary search on answer: capacity to ship packages.

Run: python3 ship.py
"""


def ship_within_days(weights: list[int], days: int) -> int:
    def feasible(cap: int) -> bool:
        needed = 1
        current = 0
        for w in weights:
            if current + w > cap:
                needed += 1
                current = w
            else:
                current += w
        return needed <= days

    left, right = max(weights), sum(weights)
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
    print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # 15
    print(ship_within_days([3, 2, 2, 4, 1, 4], 3))  # 6
    print(ship_within_days([1, 2, 3, 1, 1], 4))  # 3


if __name__ == "__main__":
    main()
