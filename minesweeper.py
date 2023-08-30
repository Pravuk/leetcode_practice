from collections import deque
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        n = len(board)
        m = len(board[0])

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m

        queue = deque()
        queue.append(click)

        while len(queue) > 0:
            cell = queue.popleft()
            bombs = 0
            cell_queue = deque()
            if board[cell[0]][cell[1]] == "E":
                for d in directions:
                    adj_row = cell[0] + d[0]
                    adj_col = cell[1] + d[1]
                    if in_bound(adj_row, adj_col):
                        match board[adj_row][adj_col]:
                            case "E":
                                cell_queue.append((adj_row, adj_col))
                            case "M":
                                bombs += 1
                if bombs == 0:
                    queue.extend(cell_queue)
                    board[cell[0]][cell[1]] = "B"
                else:
                    board[cell[0]][cell[1]] = f"{bombs}"

        return board


if __name__ == "__main__":
    s = Solution()
    s.updateBoard(
        board=[["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"],
               ["E", "E", "E", "E", "E"]], click=[3, 0])
    pass
