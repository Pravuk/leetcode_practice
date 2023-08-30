from typing import List


class Solution:
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        cache = [[0] * m for _ in range(n)]

        def is_in_bound(_row, _col: int) -> bool:
            return 0 <= _row < n and 0 <= _col < m

        def dfs(_row, _col: int) -> int:

            if cache[_row][_col] > 0:
                return cache[_row][_col]

            _max = 1
            cache[_row][_col] = _max
            for d in self.directions:
                new_row = _row + d[0]
                new_col = _col + d[1]
                if not is_in_bound(new_row, new_col):
                    continue
                if matrix[_row][_col] < matrix[new_row][new_col]:
                    _max = max(dfs(new_row, new_col) + 1, _max)

            cache[_row][_col] = _max  # ?

            return cache[_row][_col]

        max_path = 0
        for i in range(n):
            for j in range(m):
                max_path = max(dfs(i, j), max_path)
        return max_path


if __name__ == "__main__":

    result = Solution().longestIncreasingPath([[1,2]])

    print(result)
    pass
