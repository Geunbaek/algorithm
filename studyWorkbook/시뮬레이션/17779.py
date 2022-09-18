import sys

input = sys.stdin.readline

def isValidRange(x, y, d1, d2):
    return 1 < x + d1 + d2 <= n and 1 <= y - d1 and y + d2 <= n

def getPopulation(x, y, d1, d2):
    population = [0 for _ in range(5)]
    areaBoard = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    areaBoard[x][y] = -1
    r, c = 0, 0
    for i in range(1, d1 + 1):
        r = x + i
        c = y - i
        areaBoard[r][c] = -1

    for i in range(1, d2 + 1):
        nr = r + i
        nc = c + i
        areaBoard[nr][nc] = -1

    for i in range(1, d2 + 1):
        r = x + i
        c = y + i
        areaBoard[r][c] = -1

    for i in range(1, d1 + 1):
        nr = r + i
        nc = c - i
        areaBoard[nr][nc] = -1

    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if areaBoard[r][c] == -1:
                break
            areaBoard[r][c] = 1
            population[1] += board[r][c]

    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if areaBoard[r][c] == -1:
                break
            areaBoard[r][c] = 2
            population[2] += board[r][c]

    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if areaBoard[r][c] == -1:
                break
            areaBoard[r][c] = 3
            population[3] += board[r][c]

    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 -1, -1):
            if areaBoard[r][c] == -1:
                break
            areaBoard[r][c] = 4
            population[4] += board[r][c]

    population[0] = total - sum(population)
    return population

n = int(input())
board = [[0 for _ in range(n + 1)]]
ans = 1e9
total = 0

for _ in range(n):
    line = list(map(int, input().split()))
    board.append([0] + line)
    total += sum(line)

for y in range(1, n + 1):
    for x in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if not isValidRange(x, y, d1, d2): continue
                population = getPopulation(x, y, d1, d2)
                ans = min(ans, max(population) - min(population))

print(ans)
