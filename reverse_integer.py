class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        neg = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        return neg * result if result < 2 ** 31 - 1 else 0
    # def reverse(self, x: int) -> int:
    #     neg = -1 if x < 0 else 1
    #     digits = reversed([d for d in str(abs(x))])
    #     result = neg * int("".join(digits))
    #     return result if -2 ** 31 - 1 < result < 2 ** 31 - 1 else 0


if __name__ == "__main__":
    res = Solution().reverse(-123)
    pass
