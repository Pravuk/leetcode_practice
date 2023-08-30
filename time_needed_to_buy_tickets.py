from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for i in range(len(tickets)):
            if i > k:
                result += min(tickets[k] - 1, tickets[i])
            else:
                result += min(tickets[k], tickets[i])
        return result


if __name__ == "__main__":
    print(Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2))
