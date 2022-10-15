import sys
input = sys.stdin.readline
from collections import deque

def splitAndRotateArea(l):
    for y in range(0, 2 ** n - 2 ** l + 1, 2 ** l):
        for x in range(0, 2 ** n - 2 ** l + 1, 2 ** l):
            rotate(x, y, x + 2 ** l, y + 2 ** l)

def rotate(x1, y1, x2, y2):
    ret = []
    for x in range(x1, x2):
        ret.append([])
        for y in range(y2 - 1, y1 - 1, -1):
            ret[-1].append(board[y][x])

    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = ret[y - y1][x - x1]

def isMeltArea(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
            if board[ny][nx] > 0:
                count += 1
    return count < 3

def meltIce():
    meltedIce = []
    for y in range(2**n):
        for x in range(2**n):
            if isMeltArea(x, y) and board[y][x] > 0:
                meltedIce.append((x, y))

    for x, y in meltedIce:
        board[y][x] -= 1

def getSumOfIce():
    _sum = 0
    for line in board:
        _sum += sum(line)
    return _sum

def getSizeOfIce(visited, x, y):
    q = deque([(x, y)])
    visited[y][x] = 1
    size = 0
    while q:
        nowX, nowY = q.popleft()
        size += 1
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                if board[ny][nx] > 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny))
    return size

def getBiggestSizeOfIce():
    visited = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
    maxSize = 0
    for y in range(2 ** n):
        for x in range(2 ** n):
            if board[y][x] > 0:
                maxSize = max(maxSize, getSizeOfIce(visited, x, y))
    return maxSize

n, q = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(2 ** n):
    board.append(list(map(int, input().split())))

qArr = list(map(int, input().split()))
for l in qArr:
    splitAndRotateArea(l)
    meltIce()

print(getSumOfIce())
print(getBiggestSizeOfIce())


