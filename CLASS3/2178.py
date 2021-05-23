import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visit[ny][nx] == 0 and board[ny][nx] == 1:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((nx, ny))

    return visit[-1][-1]

n, m = map(int, input().split())
board = []

for _ in range(n):
    line = list(map(int, input().strip()))
    board.append(line)

print(bfs())