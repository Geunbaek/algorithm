import sys
input = sys.stdin.readline

n = int(input())
dp = [[10-i for i in range(10)] for _ in range(n)]

for y in range(1, n):
    for x in range(10):
        if x == 0:
            dp[y][x] = sum(dp[y-1])
        else:
            dp[y][x] = dp[y][x-1] - dp[y-1][x-1]

print(dp[n-1][0] % 10007)