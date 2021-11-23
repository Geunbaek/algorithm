import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0]
dy = [0, 1]

y, x = map(int, input().split())

board = []
results = []

for i in range(y):
    board.append(list(input().strip()))

def bfs(s_x, s_y, d):
    q = deque()
    q.append((s_x, s_y))
    s = ''
    while q:
        now_x, now_y = q.popleft()
        s += board[now_y][now_x] if board[now_y][now_x] != '#' else " "
        nx = now_x + dx[d]
        ny = now_y + dy[d]
        if 0 <= nx < x and 0 <= ny < y:
            q.append((nx, ny))
    return s

for i in range(x):
    temp = bfs(i, 0, 1)
    for el in temp.split():
        if len(el) >= 2:
            results.append(el)

for i in range(y):
    temp = bfs(0, i, 0)
    for el in temp.split():
        if len(el) >= 2:
            results.append(el)

results.sort()
print(results[0])