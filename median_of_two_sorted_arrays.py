from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        a_len = len(a)
        b_len = len(b)

        left = 0
        right = a_len

        odd = (a_len + b_len) % 2 == 0

        while left <= right:
            part_a = int((left + right) / 2)
            part_b = int((a_len + b_len + 1) / 2) - part_a
            max_left_a = float("-inf") if part_a == 0 else a[part_a - 1]
            min_right_a = float("inf") if part_a == a_len else a[part_a]
            max_left_b = float("-inf") if part_b == 0 else b[part_b - 1]
            min_right_b = float("inf") if part_b == b_len else b[part_b]

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2 if odd else max(max_left_a,
                                                                                                         max_left_b)
            elif max_left_a > min_right_b:
                right = part_a - 1
            else:
                left = part_a + 1

        # total = len(a) + len(b)
        # half = total // 2
        #
        # left, right = 0, len(a)
        #
        # while left <= right + 1:
        #     print(f"{left}-{right}")
        #     amiddle = (left + right) // 2  # a
        #     bmiddle = half - amiddle - 1 - 1  # b
        #     aleft = a[amiddle] if amiddle >= 0 else float("-inf")
        #     aright = a[amiddle + 1] if amiddle + 1 < len(a) else float("inf")
        #     bleft = b[bmiddle] if bmiddle >= 0 else float("-inf")
        #     bright = b[bmiddle + 1] if bmiddle + 1 < len(b) else float("inf")
        #
        #     if aleft <= bright and bleft <= aright:
        #         if total % 2 == 0:  # even
        #             return (min(aright, bright) + max(aleft, bleft)) / 2
        #         else:  # odd
        #             return min(aright, bright)
        #     elif aleft > bright:
        #         right = amiddle - 1
        #     else:
        #         left = amiddle + 1
        #


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    # print(Solution().findMedianSortedArrays([1, 3, 10, 14, 20, 21, 22, 35, 40, 41, 45, 50, 51], [2, 5, 7, 60]))

    # 1,2,3,5,7,10,14,20,21,22,35,40,41,45,50,51,60
    pass
