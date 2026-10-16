"""Range sum queries using a prefix array.

Run: python3 range_sum.py
"""


class PrefixSum:
    def __init__(self, nums: list[int]):
        self.P = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self.P[i + 1] = self.P[i] + value

    def query(self, i: int, j: int) -> int:
        # sum of nums[i..j] inclusive
        return self.P[j + 1] - self.P[i]


def main() -> None:
    ps = PrefixSum([1, 2, 3, 4])
    print(ps.query(1, 3))   # 9
    print(ps.query(0, 0))   # 1
    print(ps.query(0, 3))   # 10


if __name__ == "__main__":
    main()
