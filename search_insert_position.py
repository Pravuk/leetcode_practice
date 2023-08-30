from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target > nums[right]:
            return right + 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return left


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3], 2))
