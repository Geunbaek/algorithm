import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

i = 2
while i < n:
    if board[0][i]:
        break
    dp[0][0][i] = 1
    i += 1

for y in range(1, n):
    for x in range(2, n):
        if board[y][x] == 0 and board[y][x - 1] == 0 and board[y-1][x] == 0:
            dp[2][y][x] = sum(dp[z][y - 1][x - 1] for z in range(3))

        if board[y][x] == 0:
            dp[0][y][x] = dp[0][y][x-1] + dp[2][y][x-1]
            dp[1][y][x] = dp[1][y-1][x] + dp[2][y-1][x]

print(sum(dp[z][-1][-1] for z in range(3)))

