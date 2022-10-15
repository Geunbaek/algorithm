import sys
input = sys.stdin.readline

def isValidMovement(x, y, prev, d):
    if abs(prev - d) > 1:
        return False
    nx = x + dx[d]
    ny = y + dy[d]
    if (nx, ny) in startPos:
        return False
    if not (0 <= nx < n and 0 <= ny < n):
        return False
    if board[ny][nx] != 0:
        return False
    if d == 1 and not(board[ny - 1][nx] == 0 and board[ny][nx - 1] == 0):
        return False
    return True


n = int(input())
board = []
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
dx = [1, 1, 0]
dy = [0, 1, 1]

for _ in range(n):
    board.append(list(map(int, input().split())))

startPos = [(0, 0), (1, 0)]
for y in range(n):
    for x in range(n):
        for prev in range(3):
            for d in range(3):
                if isValidMovement(x, y, prev, d):
                    nx, ny = x + dx[d], y + dy[d]
                    dp[ny][nx][d] += dp[y][x][prev]

print(sum(dp[-1][-1]))