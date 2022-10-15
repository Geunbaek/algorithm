import sys, copy
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

def moveNextPhase(board):
    board.pop()

def getDist(ax, ay, ex, ey):
    return abs(ey - ay) + abs(ex - ax)

def isAttackable(dist):
    return dist <= d

def getAttackableEnemy(archerPos, board):
    ax, ay = archerPos
    attackableEnemyInfo = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 1:
                dist = getDist(ax, ay - phase, x, y)
                if isAttackable(dist):
                    attackableEnemyInfo.append((dist, x, y))

    return attackableEnemyInfo

n, m, d = map(int, input().strip().split())
board = []
maxKillCount = 0

for _ in range(n):
    board.append(list(map(int, input().split())))

for comb in combinations(range(m), 3):
    killCount = 0
    phase = 0
    archeres = []
    copyBoard = copy.deepcopy(board)
    for x in comb:
        archeres.append((x, n))
    while copyBoard:
        attackedEnemies = []
        for archer in archeres:
            attackableEnemyInfo = getAttackableEnemy(archer, copyBoard)

            if not attackableEnemyInfo:
                continue

            attackedEnemy = sorted(attackableEnemyInfo)[0]
            attackedEnemies.append(attackedEnemy)

        for enemy in attackedEnemies:
            dist, x, y = enemy
            if copyBoard[y][x] == 1:
                copyBoard[y][x] = 0
                killCount += 1
        moveNextPhase(copyBoard)
        phase += 1
    maxKillCount = max(maxKillCount, killCount)
print(maxKillCount)


