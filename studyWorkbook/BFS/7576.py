import sys
from collections import deque
input = sys.stdin.readline

def isValidRange(x, y):
    return 0 <= x < m and 0 <= y < n

def bfs(q):
    count = 0
    while q:
        length = len(q)
        count += 1
        while length:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isValidRange(nx, ny): continue
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    q.append((nx, ny))
                    q.append((nx, ny))
            length -= 1
    return count - 1

def checkTomatoState():
    zeroCount = 0
    for line in board:
        zeroCount += line.count(0)
    return zeroCount == 0

m, n = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque()

for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(m):
        if line[x] == 1:
            q.append((x, y))

count = bfs(q)

if checkTomatoState():
    print(count)
else:
    print(-1)