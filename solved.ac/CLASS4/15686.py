import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    dist = [0 for _ in range(len(store))]
    visit = [[0] * n for _ in range(n)]
    visit[b][a] = 1
    while q:
        x, y = q.popleft()
        for i, p in enumerate(store):
            if x == p[0] and y == p[1]:
                dist[i] = visit[y][x]-1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[ny][nx] == 0:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((nx, ny))

    distance.append(dist[:])

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

store = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 2:
            store.append((x, y))

distance = []

for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            bfs(x, y)

results = []

for idx in combinations([i for i in range(len(store))], m):
    val = 0
    for d in distance:
        min_val = 10**9
        for i in idx:
            min_val = min(min_val, d[i])
        val += min_val
    results.append(val)

print(min(results))