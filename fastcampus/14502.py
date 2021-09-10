import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

v_pos = []
zero = []
for y in range(n):
    for x in range(m):
        if board[y][x] == 2:
            v_pos.append((x, y))
        if board[y][x] == 0:
            zero.append((x, y))

def bfs(arr):

    q = deque(v_pos)
    visit = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for x, y in v_pos:
        visit[y][x] = 1
    for x, y in arr:
        visit[y][x] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visit[ny][nx] == 0 and board[ny][nx] == 0:
                    visit[ny][nx] = 1
                    cnt += 1
                    q.append((nx, ny))

    return cnt

ans = 0
wall = list(combinations(zero, 3))

for el, el2, el3 in wall:
    ans = max(ans, len(zero) - bfs([el, el2, el3]) - 3)

print(ans)