import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def getPosOfString(r, c):
    return f"{r}-{c}"

def getMovements():
    movements = defaultdict(list)
    for fireBall in fireBalls:
        nr, nc = fireBall.move()
        movements[getPosOfString(nr, nc)].append(fireBall)
    return movements

def isEqualDirectionOfEvenOrOdd(arr):
    oddCount = 0
    evenCount = 0
    for fireBall in arr:
        if fireBall.d % 2 != 0:
            oddCount += 1
        else:
            evenCount += 1

    return True if oddCount == len(arr) or evenCount == len(arr) else False

def union(arr, r, c):
    sumM = 0
    sumS = 0

    for fireBall in arr:
        sumM += fireBall.m
        sumS += fireBall.s
    # print(r, c, sumM)
    if sumM // 5 == 0:
        return

    nextDirection = (0, 2, 4, 6) if isEqualDirectionOfEvenOrOdd(arr) else (1, 3, 5, 7)
    for direction in nextDirection:
        fireBalls.add(FireBall(r, c, sumM // 5, sumS // len(arr), direction))

    return

class FireBall:
    def __init__(self, r, c, m, s, d):
        self.r = r
        self.c = c
        self.m = m
        self.s = s
        self.d = d

    def move(self):
        nc = (self.c + dc[self.d] * self.s) % n
        nr = (self.r + dr[self.d] * self.s) % n

        self.c = nc
        self.r = nr
        return self.r, self.c

    def __repr__(self):
        return f'{self.r}-{self.c}-{self.m}-{self.s}-{self.d}'


n, m, k = map(int, input().split())
fireBalls = set()
dc = [0, 1, 1, 1, 0, -1, -1, -1]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireBalls.add(FireBall(r-1, c-1, m, s, d))

for _ in range(k):
    movements = getMovements()
    for key, val in movements.items():
        nowR, nowC = map(int, key.split('-'))
        if len(val) >= 2:
            union(val, nowR, nowC)
            for f in val:
                fireBalls.remove(f)

answer = 0
for fireBall in fireBalls:
    answer += fireBall.m
print(answer)
