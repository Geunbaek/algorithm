import sys
from collections import deque
input = sys.stdin.readline

def isValidRange(x, y):
    return 0 <= x < m and 0 <= y < n

def setLandNum(x, y, num):
    q = deque([(x, y)])
    board[y][x] = num
    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if not (isValidRange(nx, ny)):
                continue

            if board[ny][nx] == 0 or board[ny][nx] == num:
                continue

            board[ny][nx] = num
            q.append((nx, ny))

def getBridge(x, y):
    q = deque()
    landNum = board[y][x]
    bridges = []

    for i in range(4):
        q.append((x, y, i, 0))

    while q:
        nowX, nowY, d, count = q.popleft()

        nx = nowX + dx[d]
        ny = nowY + dy[d]
        if not (isValidRange(nx, ny)):
            continue

        if board[ny][nx] == landNum:
            continue

        if board[ny][nx] == 0:
            q.append((nx, ny, d, count + 1))
        else:
            if count < 2:
                continue
            bridges.append((landNum, board[ny][nx], count))

    return bridges

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    p[ap] = bp

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

num = 1
for y in range(n):
    for x in range(m):
        if board[y][x] != 1:
            continue
        setLandNum(x, y, num + 1)
        num += 1

bridges = []
p = [i for i in range(num + 1)]

for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            continue
        bridges.extend(getBridge(x, y))

bridges.sort(key = lambda x: x[-1])
edgeCount = 0
edgeLength = 0

for u, v, length in bridges:
    if find(u) != find(v):
        union(u, v)
        edgeCount += 1
        edgeLength += length

if edgeCount == num - 2:
    print(edgeLength)
else:
    print(-1)

