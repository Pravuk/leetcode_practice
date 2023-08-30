from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for x in nums:
            candidate = x if count == 0 else candidate
            count = count + 1 if x == candidate else count - 1
        return candidate


if __name__ == "__main__":
    print(Solution().majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
