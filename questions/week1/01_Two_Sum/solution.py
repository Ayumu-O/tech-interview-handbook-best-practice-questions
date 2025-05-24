from typing import List


class Solution:
    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            remain = target - num
            fid = seen.get(remain)
            if fid is not None:
                return [i, fid]
            seen[num] = i

    # O(n^2)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remain = target - num
            for j, num2 in enumerate(nums[(i + 1) :], start=i + 1):
                if num2 == remain:
                    return [j, i]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Output: [1, 0]
    print(s.twoSum([3, 2, 4], 6))  # Output: [2, 1]
    print(s.twoSum([3, 3], 6))  # Output: [1, 0]

    print(s.twoSum2([2, 7, 11, 15], 9))  # Output: [1, 0]
    print(s.twoSum2([3, 2, 4], 6))  # Output: [2, 1]
    print(s.twoSum2([3, 3], 6))  # Output: [1, 0]
