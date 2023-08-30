from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph: dict[int, list] = defaultdict(list)
        queue = deque([(0, src, -1)])

        for _from, _to, _cost_to in flights:
            graph[_from].append([_to, _cost_to])

        costs = [float("inf")] * n

        while queue:
            _cost, _current, stops = queue.popleft()
            if stops < k:
                for _to, _cost_to in graph[_current]:
                    _cost_total = _cost + _cost_to
                    if _cost_total < costs[_to]:
                        costs[_to] = _cost_total
                        queue.append((_cost_total, _to, stops + 1))

        return costs[dst] if costs[dst] != float("inf") else -1


if __name__ == '__main__':
    s = Solution()
    s.findCheapestPrice(n=4,
                        flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                        src=0,
                        dst=3,
                        k=1)
    pass
