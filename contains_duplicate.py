from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
            set_of_nums = set(nums)
            return len(set_of_nums) == len(nums)


if __name__ == "__main__":
    Solution().containsDuplicate([1, 1, 2, 6, 3])
