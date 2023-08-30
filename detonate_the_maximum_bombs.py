from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph: dict[int, list] = defaultdict(list)
        result = 0
        n = len(bombs)

        for i in range(n):
            for j in range(i + 1, n):
                bomb = bombs[i]
                another_bomb = bombs[j]
                distance_i_2_j = sqrt((another_bomb[0] - bomb[0]) ** 2 + (another_bomb[1] - bomb[1]) ** 2)
                if distance_i_2_j <= bomb[2]:
                    graph[i].append(j)
                if distance_i_2_j <= another_bomb[2]:
                    graph[j].append(i)

        def explode(bomb_index: int, exploded: set[int]):
            for adj_bomb in graph[bomb_index]:
                if adj_bomb not in exploded:
                    exploded.add(adj_bomb)
                    if adj_bomb in graph:
                        exploded = explode(adj_bomb, exploded)
            return exploded

        for bomb_i in range(n):
            exploded = {bomb_i}
            result = max(result, explode(bomb_i, exploded))
            if result == n:
                break

        return result


if __name__ == "__main__":
    print(Solution().maximumDetonation(bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
