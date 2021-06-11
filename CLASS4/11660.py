import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
dp = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(1,n+1):
    for x in range(1,n+1):
        dp[y][x] = dp[y-1][x] + dp[y][x-1] - dp[y-1][x-1] + board[y-1][x-1]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    print(dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1])
