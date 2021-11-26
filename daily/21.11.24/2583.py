import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def change(x1, y1, x2, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

def bfs(a, b):
    q = deque()
    q.append((a, b))
    board[b][a] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    q.append((nx, ny))
    return cnt


m, n, k = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(m)]
ans = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    change(x1, y1, x2, y2)

for y in range(m):
    for x in range(n):
        if board[y][x] == 0:
            ans.append(bfs(x, y))
ans.sort()
print(len(ans))
print(*ans)



