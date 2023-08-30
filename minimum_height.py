from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(lambda: set([]))
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        leaves = deque()
        for i in range(n):
            if i in graph and len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            leaves_count = len(leaves)
            n -= leaves_count
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)


if __name__ == '__main__':
    s = Solution()
    s.findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
