import sys
from collections import deque
input = sys.stdin.readline

def isValidRange(x, y):
    return 0 <= x < c and 0 <= y < r

def bfs(a, b):
    q = deque([(a, b)])
    size = 1
    board[b][a] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isValidRange(nx, ny): continue
            if board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((nx, ny))
                size += 1
    return size

r, c = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
maxSize = 0
imageCount = 0

for _ in range(r):
    board.append(list(map(int, input().split())))

for y in range(r):
    for x in range(c):
        if board[y][x] == 1:
            imageCount += 1
            maxSize = max(maxSize, bfs(x, y))

print(imageCount)
print(maxSize)

