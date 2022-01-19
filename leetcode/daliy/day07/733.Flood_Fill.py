from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        def bfs(a, b, cur_color, change_color):
            q = deque()
            q.append((a, b))
            while q:
                x, y = q.popleft()
                image[y][x] = change_color
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(image[0]) and 0 <= ny < len(image):
                        if image[ny][nx] == cur_color:
                            q.append((nx, ny))
        if image[sr][sc] != newColor:
            bfs(sc, sr, image[sr][sc], newColor)
        return image