"""Solution: Split Array Largest Sum. O(n log sum) time, O(1) space."""


def split_array(nums: list[int], m: int) -> int:
    def feasible(limit: int) -> bool:
        count = 1
        current = 0
        for n in nums:
            if current + n > limit:
                count += 1
                current = n
            else:
                current += n
        return count <= m

    left, right = max(nums), sum(nums)
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    print(split_array([7, 2, 5, 10, 8], 2))  # 18
