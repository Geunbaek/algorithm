import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0,0] for i in range(n+1)]
    dp[0] = [1, 0]
    for i in range(1, len(dp)):
        dp[i] = [dp[i-1][1], dp[i-1][0] + dp[i-1][1]]
    print(dp[n][0], dp[n][1])