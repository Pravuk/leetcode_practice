from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        n = len(nums)
        for i in range(n):
            if (target - nums[i]) not in sums:
                sums[target - nums[i]] = i

        for i in range(n):
            if nums[i] in sums and i != sums[nums[i]]:
                return [i, sums[nums[i]]]


if __name__ == "__main__":
    print(Solution().twoSum(nums=[3, 2, 4], target=6))
