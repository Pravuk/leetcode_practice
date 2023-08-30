from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        n = len(grid)
        m = len(grid[0])

        def in_bound(_i, _j):
            return 0 <= _i < n and 0 <= _j < m

        rotted_oranges = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotted_oranges.append((i, j))

        steps = -1
        while len(rotted_oranges) != 0:
            steps += 1
            next_portion_of_rotted_oranges = set()
            for i, j in rotted_oranges:
                for d_i, d_j in directions:
                    _i = i + d_i
                    _j = j + d_j
                    if in_bound(_i, _j) and grid[_i][_j] == 1 and (_i, _j) not in next_portion_of_rotted_oranges:
                        grid[_i][_j] = 2
                        next_portion_of_rotted_oranges.add((_i, _j))
            rotted_oranges.clear()
            rotted_oranges += list(next_portion_of_rotted_oranges)
            pass

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return steps


if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
