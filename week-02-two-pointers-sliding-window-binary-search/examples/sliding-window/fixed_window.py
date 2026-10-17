"""Fixed-size sliding window sum.

Run: python3 fixed_window.py
"""


def max_sum_subarray_k(nums: list[int], k: int) -> int:
    if not nums or k <= 0 or k > len(nums):
        return 0
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > best:
            best = window_sum
    return best


def main() -> None:
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))  # 9
    print(max_sum_subarray_k([1, 2, 3], 5))            # 0


if __name__ == "__main__":
    main()
