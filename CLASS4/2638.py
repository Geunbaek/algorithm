import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    ck = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[ny][nx] == 0:
                if board[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny))
                elif board[ny][nx] >= 1:
                    ck = True
                    board[ny][nx] += 1

    return ck


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = []
time = 0

for _ in range(n):
    board.append(list(map(int,input().split())))

while True:
    ans = bfs()

    if not ans:
        break

    for y in range(n):
        for x in range(m):
            if board[y][x] == 2:
                board[y][x] = 1
            elif board[y][x] >= 3:
                board[y][x] = 0
    time += 1

print(time)
"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
"""