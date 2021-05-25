import sys
input = sys.stdin.readline
from collections import deque

def bfs(q):
    length = len(q)
    check = False
    while length:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0<= nz < h:
                if board[nz][ny][nx] == 0:
                    board[nz][ny][nx] = 1
                    q.append((nx, ny, nz))
                    check = True
        length -= 1
    return check

m, n, h = map(int,input().split())
board = []
visit = [[0] * m for _ in range(n*h)]

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]
ans = 0
q = deque()

for _ in range(h):
    arr = []
    for _ in range(n):
        line = list(map(int, input().split()))
        arr.append(line)
    board.append(arr)

for z in range(h):
    for y in range(n):
        for x in range(m):
            if board[z][y][x] == 1:
                q.append((x, y, z))
while q:
    if bfs(q):
        ans += 1

ck = True
for z in range(h):
    for y in range(n):
        for x in range(m):
            if board[z][y][x] == 0:
                ck = False
                break
        if not ck:
            break
    if not ck:
        break
if ck:
    print(ans)
else:
    print(-1)
