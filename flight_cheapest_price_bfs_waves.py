from typing import List

import numpy as np


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency_matrix = [[0] * n for _ in range(n)]
        # adjacency_matrix = [[None] * n] * n
        # adjacency_matrix = np.stack(adjacency_matrix)
        # adjacency_matrix = np.stack(adjacency_matrix)
        for f in flights:
            s = f[0]
            d = f[1]
            cost = f[2]
            row = adjacency_matrix[s]
            row[d] = cost

        adjacency_matrix = np.stack(adjacency_matrix)
        queue = [(src, 0)]
        k_i = 0

        min_prices = [float('inf')] * n
        while len(queue) and k_i <= k + 1:
            queue_size = len(queue)
            for i in range(queue_size):
                cur = queue.pop(0)
                if cur[1] >= min_prices[cur[0]]:
                    continue

                min_prices[cur[0]] = cur[1]
                for j in range(n):
                    price = adjacency_matrix[cur[0]][j]
                    if price > 0:
                        queue.append((j, price + cur[1]))

            k_i += 1

        return -1 if min_prices[dst] == float('inf') else min_prices[dst]


import unittest


class TestSolution(unittest.TestCase):
    def test_findCheapestPrice(self):
        sol = Solution()

        # Test case 1
        n = 3
        flights = [[0, 1, 100], [1, 2, 200], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), 300)

        # Test case 2
        n = 3
        flights = [[0, 1, 100], [1, 2, 200], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), 500)

        # Test case 3
        n = 4
        flights = [[0, 1, 100], [1, 2, 200], [2, 3, 300]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), -1)


if __name__ == '__main__':
    unittest.main()
# if __name__ == '__main__':
#     s = Solution()
#     s.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0,
#                         dst=3,
#                         k=1)
#     pass
