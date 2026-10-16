"""Solution: Range Sum Query - Immutable. O(n) precompute, O(1) query."""


class RangeSumQuery:
    def __init__(self, nums: list[int]):
        self.P = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self.P[i + 1] = self.P[i] + value

    def query(self, i: int, j: int) -> int:
        return self.P[j + 1] - self.P[i]


if __name__ == "__main__":
    rs = RangeSumQuery([1, 2, 3, 4])
    print(rs.query(1, 3))  # 9
