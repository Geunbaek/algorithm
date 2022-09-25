import sys
from collections import deque

input = sys.stdin.readline

def rotateClockwise(arr, k):
    for _ in range(k):
        arr.appendleft(arr.pop())


def rotateCounterclockwise(arr, k):
    for _ in range(k):
        arr.append(arr.popleft())

def isValidRange(y):
    return 0 <= y < n

def removeEqualArea(x, y, target):
    q = deque([(x, y)])
    isRemoved = False

    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if not isValidRange(ny): continue
            if circleBoard[ny][nx % m] == target:
                circleBoard[ny][nx % m] = 0
                q.append((nx, ny))
                isRemoved = True

    if isRemoved:
        circleBoard[y][x] = 0
    return isRemoved

def getTotal():
    total = 0
    for l in circleBoard:
        total += sum(l)
    return total

def getAverage():
    total = 0
    count = 0
    for y in range(n):
        for x in range(m):
            if circleBoard[y][x] > 0:
                count += 1
                total += circleBoard[y][x]
    if count == 0:
        return 0
    return total / count

n, m, t = map(int, input().split())
circleBoard = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    circleBoard.append(deque(list(map(int, input().split()))))

for _ in range(t):
    x, d, k = map(int, input().split())
    for y in range(n):
        if (y + 1) % x != 0: continue
        if d == 0:
            rotateClockwise(circleBoard[y], k)
        else:
            rotateCounterclockwise(circleBoard[y], k)

    isRemoved = False
    for y in range(n):
        for x in range(m):
            if circleBoard[y][x] != 0:
                temp = removeEqualArea(x, y, circleBoard[y][x])
                isRemoved = isRemoved or temp

    if not isRemoved:
        average = getAverage()
        for y in range(n):
            for x in range(m):
                if circleBoard[y][x] <= 0: continue
                if circleBoard[y][x] > average:
                    circleBoard[y][x] -= 1
                elif circleBoard[y][x] < average:
                    circleBoard[y][x] += 1

print(getTotal())
