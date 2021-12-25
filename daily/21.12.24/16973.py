import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(h, w, sy, sx, fy, fx):
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[sy-1][sx-1] = 1
    q = deque()
    q.append((sx-1, sy-1, 0))
    while q:
        x, y, cnt = q.popleft()
        if x == fx-1 and y == fy-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visit[ny][nx] == 0 and check(h, w, nx, ny):
                    visit[ny][nx] = 1
                    q.append((nx, ny, cnt + 1))

    return -1

def check(h, w, nx, ny):
    finx, finy = nx + w - 1, ny + h - 1
    if 0 <= finx < m and 0 <= finy < n:
        if nx == 0 and ny == 0:
            if dp[finy][finx] != 0:
                return False
        elif nx == 0:
            if dp[finy][finx] - dp[ny - 1][finx] != 0:
                return False
        elif ny == 0:
            if dp[finy][finx] - dp[finy][nx - 1] != 0:
                return False
        else:
            if dp[finy][finx] - dp[ny - 1][finx] - dp[finy][nx - 1] + dp[ny - 1][nx - 1] != 0:
                return False
        return True
    else:
        return False


n, m = map(int, input().split())
board = []
dp = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        if x == 0:
            dp[y][x] = board[y][0]
            continue
        dp[y][x] = dp[y][x-1] + board[y][x]

for y in range(1, n):
    for x in range(m):
        dp[y][x] = dp[y-1][x] + dp[y][x]

h, w, sy, sx, fy, fx = map(int, input().split())
print(bfs(h, w, sy, sx, fy, fx))