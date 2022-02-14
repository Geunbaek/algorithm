from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        def check(a, b):
            q = deque()
            q.append((a, b))
            visit = set()
            visit.add((a, b))
            flag = False

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                        if board[ny][nx] == 'O' and (nx, ny) not in visit:
                            visit.add((nx, ny))
                            q.append((nx, ny))
                    else:
                        flag = True
            return flag, visit
        checked = set()
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 'O' and (x, y) not in checked:
                    ck, visit = check(x, y)
                    if not ck:
                        for x1, y1 in visit:
                            board[y1][x1] = "X"
                    else:
                        checked.union(visit)



