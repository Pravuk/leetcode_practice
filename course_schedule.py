from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = {}
        graph = {}
        nodes = range(numCourses)
        for p in prerequisites:
            if p[0] not in in_degree:
                in_degree[p[0]] = 0
            if p[1] not in graph:
                graph[p[1]] = []
            graph[p[1]].append(p[0])
            in_degree[p[0]] += 1
            pass

        schedule = []
        zero_in_degree = []

        for node in nodes:
            if node not in in_degree or in_degree[node] == 0:
                zero_in_degree.append(node)

        while len(zero_in_degree):
            node = zero_in_degree.pop()
            schedule.append(node)
            if node in graph:
                for target in graph[node]:
                    in_degree[target] -= 1
                    if in_degree[target] == 0:
                        zero_in_degree.append(target)
                del graph[node]

        return schedule if len(schedule) == numCourses else []


if __name__ == "__main__":
    assert Solution().canFinish(3, [[1, 0], [1, 2], [0, 1]])

    assert Solution().canFinish(2, [[1, 0]])
    assert Solution().canFinish(1, [])
    assert Solution().canFinish(6, [[1, 0], [2, 0], [3, 1], [4, 1], [4, 3], [5, 3]])
    assert not Solution().canFinish(6, [[1, 0], [2, 0], [3, 1], [4, 1], [4, 3], [5, 3], [0, 4]])
