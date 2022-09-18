import sys
from collections import deque
input = sys.stdin.readline

def isValidRange(x, y):
    return 0 <= x < m and 0 <= y < n

def bfs(a, b):
    q = deque([(a, b, 1)])
    board[b][a] = 0

    while q:
        x, y, moveCount = q.popleft()
        if x == m - 1 and y == n - 1:
            return moveCount

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isValidRange(nx, ny): continue
            if board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((nx, ny, moveCount + 1))


n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
board = []

for _ in range(n):
    board.append(list(map(int, input().strip())))

print(bfs(0, 0))
