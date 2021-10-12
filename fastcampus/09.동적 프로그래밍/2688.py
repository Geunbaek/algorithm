import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(n)]

    for i in range(10):
        dp[0][i] = 10-i

    for y in range(1, n):
        num = 0
        for x in range(10):
            if x == 0:
                dp[y][x] = sum(dp[y - 1])
                num = dp[y-1][x]
            else:
                dp[y][x] = dp[y][x-1] - dp[y-1][x-1]

    print(dp[n - 1][0])

