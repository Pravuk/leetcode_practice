class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left <= right:
            middle = (left + right) // 2
            if middle == x / middle:
                return int(middle)
            elif middle > x / middle:
                right = middle - 1
            else:
                left = middle + 1
        return int(right)


if __name__ == "__main__":
    print(Solution().mySqrt(2))
