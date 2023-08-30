from typing import List

import numpy as np


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0

        cols = len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1

        queue = []
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))

        path_len = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                x, y = queue.pop(0)
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[nx][ny] -= 1
                            if indegree[nx][ny] == 0:
                                queue.append((nx, ny))
            path_len += 1
        return path_len


if __name__ == '__main__':
    s = Solution()
    res = s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
    print(res)
