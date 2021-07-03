import sys
input = sys.stdin.readline

n = int(input())
dp = []

for _ in range(n):
    r, g, b = map(int, input().split())
    dp.append([r, g, b])

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i][j]+dp[i-1][1], dp[i][j]+dp[i-1][2])
        elif j == 1:
            dp[i][j] = min(dp[i][j] + dp[i - 1][0], dp[i][j] + dp[i - 1][2])
        elif j == 2:
            dp[i][j] = min(dp[i][j] + dp[i - 1][0], dp[i][j] + dp[i - 1][1])

print(min(dp[n-1]))