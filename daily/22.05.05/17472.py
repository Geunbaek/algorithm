import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b, num):
    q = deque()
    q.append((a, b))
    board[b][a] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 1:
                    board[ny][nx] = num
                    q.append((nx, ny))

def make_bridge(a, b, d):
    dist = 0
    while True:
        nx = a + dx[d]
        ny = b + dy[d]
        if 0 <= nx < m and 0 <= ny < n:
            if board[ny][nx] == 0:
                a = nx
                b = ny
            else:
                if dist + 1 > 2:
                    return board[ny][nx], dist
                else:
                    return -1, -1
        else:
            return -1, -1
        dist += 1

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    p[ap] = bp


n, m = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
bridges = []

for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

name = 2
for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            bfs(x, y, name)
            name += 1

p = [i for i in range(name)]

for y in range(n):
    for x in range(m):
        if board[y][x] != 0:
            for i in range(4):
                tar, dist = make_bridge(x, y, i)
                if dist != -1 and dist != 1:
                    bridges.append((board[y][x], tar, dist))

bridges.sort(key = lambda x:x[-1])
count = 0
total = 0
for u, v, dist in bridges:
    if find(u) != find(v):
        union(u, v)
        count += 1
        total += dist

if count == len(p) - 3:
    print(total)
else:
    print(-1)
