import sys
input = sys.stdin.readline
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    board[b][a] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    q.append((nx, ny))
                    cnt += 1

    return cnt



n = int(input())
board = []
ans = []
for _ in range(n):
    line = list(map(int, input().strip()))
    board.append(line)

for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            ans.append(bfs(x, y))

ans.sort()

print(len(ans))
for i in ans:
    print(i)