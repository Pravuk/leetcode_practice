from collections import defaultdict
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        sizes = defaultdict(lambda: 1)
        back_track = defaultdict(lambda: -1)

        max_size = 1
        max_index = 0
        for i_, num_i in enumerate(nums[1:]):
            i = i_ + 1
            for j, num_j in enumerate(nums[:i]):
                if nums[i] % nums[j] == 0 and sizes[j] + 1 > sizes[i]:
                    sizes[i] = sizes[j] + 1
                    back_track[i] = j
            if sizes[i] > max_size:
                max_size = sizes[i]
                max_index = i

        # Backtrack
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = back_track[max_index]
        return result


if __name__ == "__main__":
    print(Solution().largestDivisibleSubset([5, 9, 18, 54, 108, 540, 90, 180, 360, 720]))
