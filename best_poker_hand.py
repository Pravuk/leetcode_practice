import collections
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits_set = set(suits)
        if len(suits_set) == 1:
            return "Flush"
        ranks_counts = collections.Counter(ranks)
        max_ranks_count = max(ranks_counts.values())
        if max_ranks_count >= 3:
            return "3"
        elif max_ranks_count == 2:
            return "2"
        return "1"


if __name__ == "__main__":
    print(Solution().bestHand(ranks=[2, 10, 7, 10, 7], suits=["a", "b", "a", "d", "b"]))
