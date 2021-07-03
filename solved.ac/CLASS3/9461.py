import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(101)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(1, n-1):
        dp[i+2] = dp[i] + dp[i-1]
    print(dp[n-1])