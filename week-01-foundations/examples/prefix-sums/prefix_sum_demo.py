"""Build a prefix-sum array and inspect it.

Run: python3 prefix_sum_demo.py
"""


def build_prefix(nums: list[int]) -> list[int]:
    P = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        P[i + 1] = P[i] + nums[i]
    return P


def main() -> None:
    nums = [1, 2, 3, 4]
    P = build_prefix(nums)
    print("nums:   ", nums)
    print("prefix: ", P)


if __name__ == "__main__":
    main()
