from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        q = deque()
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                if mat[y][x] == 0:
                    q.append((x, y, 0))
                else:
                    mat[y][x] = -1

        while q:
            x, y, cnt = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(mat[0]) and 0 <= ny < len(mat):
                    if mat[ny][nx] == -1:
                        mat[ny][nx] = cnt + 1
                        q.append((nx, ny, cnt + 1))

        return mat
