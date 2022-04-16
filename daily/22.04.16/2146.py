import sys
input = sys.stdin.readline
from collections import deque

def grouping(a, b, num):
    q = deque()
    q.append((a, b))
    board[b][a] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 1:
                    board[ny][nx] = num
                    q.append((nx, ny))


def bfs(a, b, num):
    q = deque()
    q.append((a, b, 0))
    visit = [[0 for _ in range(n)] for _ in range(n)]
    visit[b][a] = 1

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[ny][nx] == 0 and board[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny, cnt + 1))
                elif visit[ny][nx] == 0 and board[ny][nx] not in (0, num):
                    return cnt
    return 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = []
ans = sys.maxsize

for _ in range(n):
    board.append(list(map(int, input().split())))

i = 2
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            grouping(x, y, i)
            i += 1

for y in range(n):
    for x in range(n):
        if board[y][x] != 0:
            count = bfs(x, y, board[y][x])
            if count:
                ans = min(ans, count)

print(ans)