import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n)]

for i in range(k + 1):
    dp[0][i] = i + 1

for i in range(n):
    dp[i][0] = 1

for y in range(1, n):
    for x in range(1, k):
        dp[y][x] = (dp[y][x - 1] + dp[y - 1][x]) % 1_000_000_000

print(dp[-1][-2])