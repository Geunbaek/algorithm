import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(1_000_001)] for _ in range(2)]
dp[0][0] = 1
dp[0][1] = 2
dp[0][2] = 7
dp[1][2] = 1

for i in range(3, n + 1):
    dp[1][i] = (dp[0][i - 2] + dp[1][i - 1]) % 1_000_000_007
    dp[0][i] = (3 * dp[0][i - 2] + 2 * dp[0][i - 1] + 2 * dp[1][i-1]) % 1_000_000_007

print(dp[0][n])