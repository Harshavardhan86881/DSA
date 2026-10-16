"""Solution for 'Prefix Sum Construction'. O(n) time, O(n) space."""


def build_prefix(nums: list[int]) -> list[int]:
    P = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        P[i + 1] = P[i] + nums[i]
    return P


if __name__ == "__main__":
    print(build_prefix([1, 2, 3, 4]))  # [0, 1, 3, 6, 10]
