from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            middle = (left + right) // 2
            if arr[middle] >= arr[middle + 1]:
                right = middle
            else:
                left = middle + 1

        return left


if __name__ == "__main__":
    res = Solution().peakIndexInMountainArray([5, 7, 19, 17, 10])
    print(res)
