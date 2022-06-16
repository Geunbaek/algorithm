import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[y][x] = 1
    max_count = 0

    while q:
        x, y, cnt = q.popleft()
        max_count = max(max_count, cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 0 and board[ny][nx] == 'L':
                    visited[ny][nx] = 1
                    q.append((nx, ny, cnt + 1))
    return max_count

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
n, m = map(int, input().split())
board = []
ans = 0

for _ in range(n):
    line = list(input().strip())
    board.append(line)

for y in range(n):
    for x in range(m):
        if board[y][x] == 'L':
            ans = max(ans, bfs(x, y))

print(ans)