import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n + 1)]

dp[0] = 1
dp[1] = 3
if n > 1:
    dp[2] = 7

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(dp[n])