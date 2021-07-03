import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(q):
    length = len(q)
    ck = False
    while length:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    q.append((nx, ny))
                    ck = True
        length -= 1
    return ck

m, n = map(int, input().split())
board = []
q = deque()
ans = 0
ck = False

for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            q.append((x, y))

while q:
    if bfs(q):
        ans += 1

for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            ck = True
            break
    if ck:
        break
if ck :
    print(-1)
else:
    print(ans)