from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, -1, -1, -1, 0, 1, 1, 1]
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        q = deque()
        q.append((0, 0, 1))

        while q:
            x, y, cnt = q.popleft()
            if x == len(grid) - 1 and y == len(grid) - 1:
                return cnt
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    if grid[ny][nx] == 0 and visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        q.append((nx, ny, cnt + 1))
        return -1


