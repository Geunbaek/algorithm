from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dx = [1, -1]
        dy = [-1, 1]
        ans = []
        q = deque()
        q.append((0,0, 0))
        while q:
            x, y, d = q.popleft()
            ans.append(mat[y][x])
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < len(mat[0]) and 0 <= ny < len(mat):
                q.append((nx, ny, d))
            else:
                if d == 0:
                    if 0 <= x + 1 < len(mat[0]):
                        q.append((x + 1, y, (d + 1) % 2))
                    elif 0 <= y + 1 < len(mat):
                        q.append((x, y + 1, (d + 1) % 2))
                elif d == 1:
                    if 0 <= y + 1 < len(mat):
                        q.append((x, y + 1, (d + 1) % 2))
                    elif 0 <= x + 1 < len(mat[0]):
                        q.append((x + 1, y, (d + 1) % 2))

        return ans

sol = Solution()
sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])