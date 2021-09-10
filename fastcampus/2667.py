import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().strip())))

def dfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    board[sy][sx] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    q.append((nx, ny))
    return cnt

result = []

for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            result.append(dfs(x, y))

result.sort()
print(len(result))
for el in result:
    print(el)

