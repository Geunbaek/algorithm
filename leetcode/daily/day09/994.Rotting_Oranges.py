from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        rot = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2:
                    rot.append((x, y))

        q = deque()
        q.append(rot)
        ans = 0
        while q:
            length = len(q)
            while length:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                        if grid[ny][nx] == 1:
                            grid[ny][nx] = 0
                            q.append((nx, ny))
                length -= 1
            ans += 1
        for line in grid:
            if 1 in line:
                return -1

        return ans - 1