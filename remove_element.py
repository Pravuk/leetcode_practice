from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


if __name__ == "__main__":
    nums = [2, 3, 3, 4, 2]
    Solution().removeElement(nums, 3)
