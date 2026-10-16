"""Runnable example: next greater element using a monotonic stack."""


def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            idx = stack.pop()
            result[idx] = value
        stack.append(i)
    return result


if __name__ == "__main__":
    print(next_greater([2, 1, 2, 4, 3]))
