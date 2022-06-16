import sys, copy
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def dfs(v):
    q = deque(v)
    count = 0
    visited = copy.deepcopy(board)
    for x, y in v:
        visited[y][x] = 2

    while q:
        length = len(q)
        while length:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = 2
                        q.append((nx, ny))
            length -= 1
        count += 1
    for y in range(n):
        if visited[y].count(0):
            return sys.maxsize
    return count - 1

n, m = map(int, input().split())
board = []
virus = []
ans = sys.maxsize
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for y in range(n):
    line = list(map(int, input().split()))
    for x in range(n):
        if line[x] == 2:
            line[x] = 0
            virus.append((x, y))
    board.append(line)

for v in combinations(virus, m):
    ans = min(ans, dfs(v))

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)