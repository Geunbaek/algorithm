from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        def bfs(a, b):
            q = deque()
            q.append((a, b))
            grid[b][a] = 0
            cnt = 1
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                        if grid[ny][nx] == 1:
                            grid[ny][nx] = 0
                            q.append((nx, ny))
                            cnt += 1
            return cnt

        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    ans = max(ans, bfs(x, y))
        return ans

sol = Solution()
print(sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))