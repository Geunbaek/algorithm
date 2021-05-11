import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b, s):
    q = deque()
    q.append((a, b, s))
    cnt = 0
    if board[b][a] != s:
        cnt += 1
    visit = [[0] * 8 for _ in range(8)]
    visit[0][0] = s
    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if a <= nx <= a+7 and b <= ny <= b+7:
                if visit[ny-b][nx-a] == 0:
                    if c == 'W':
                        if board[ny][nx] != "B":
                            cnt += 1
                        visit[ny-b][nx-a] = "B"
                        q.append((nx, ny, "B"))
                    else:
                        if board[ny][nx] != "W":
                            cnt += 1
                        visit[ny-b][nx-a] = "W"
                        q.append((nx, ny, "W"))
    return cnt



n, m = map(int, input().split())
board =[]
for _ in range(n):
    line = list(input().strip())
    board.append(line)

min_val = 10 ** 8
for y in range(n-7):
    for x in range(m-7):
        min_val = min(min_val, bfs(x, y, 'W'), bfs(x, y, 'B'))

print(min_val)