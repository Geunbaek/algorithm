import sys
input = sys.stdin.readline
from collections import deque

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    p[ap] = bp

def bfs(a, b):
    q = deque()
    visit = [[0 for _ in range(n)] for _ in range(n)]
    q.append((a, b, 0))
    visit[b][a] = 1
    while q:
        x, y, d = q.popleft()
        if d != 0 and (board[y][x] == 'K' or board[y][x] == 'S'):
            edges.append((keys[(a, b)], keys[(x, y)], d))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[ny][nx] == 0 and board[ny][nx] != '1':
                    visit[ny][nx] = 1
                    q.append((nx, ny, d + 1))

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
board = []
edges = []
keys = {}

count = 1
for y in range(n):
    board.append(list(input().strip()))
    for x in range(n):
        if board[y][x] == "S":
            keys[(x, y)] = 0
        if board[y][x] == "K":
            keys[(x, y)] = count
            count += 1

for key in keys.keys():
    bfs(key[0], key[1])

p = [i for i in range(len(keys))]
edges.sort(key = lambda x: x[-1])

if not edges:
    print(-1)
else:
    cost = 0
    count = 0
    for u, v, c in edges:
        if find(u) != find(v):
            union(u, v)
            cost += c
            count += 1
        if count == len(keys) - 1:
            break
    if count != len(keys) - 1:
        print(-1)
    else:
        print(cost)




