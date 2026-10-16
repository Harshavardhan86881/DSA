"""Solution for 'Next Greater Element I'. O(n + m) time, O(n + m) space."""


def next_greater_element(nums1, nums2):
    greater = {}
    stack = []
    for value in nums2:
        while stack and stack[-1] < value:
            greater[stack.pop()] = value
        stack.append(value)
    for value in stack:
        greater[value] = -1
    return [greater.get(v, -1) for v in nums1]
