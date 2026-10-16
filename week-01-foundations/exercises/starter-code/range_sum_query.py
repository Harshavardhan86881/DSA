"""Starter code: Range Sum Query - Immutable.

Implement a class RangeSumQuery with __init__(nums) and query(i, j) returning the sum of
nums[i..j] inclusive in O(1). Aim for O(n) precompute, O(1) query.
"""


class RangeSumQuery:
    def __init__(self, nums: list[int]):
        pass

    def query(self, i: int, j: int) -> int:
        pass


if __name__ == "__main__":
    rs = RangeSumQuery([1, 2, 3, 4])
    print(rs.query(1, 3))
