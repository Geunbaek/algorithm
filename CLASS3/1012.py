import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    board[b][a] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    q.append((nx, ny))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    cnt = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                bfs(x, y)
                cnt += 1

    print(cnt)