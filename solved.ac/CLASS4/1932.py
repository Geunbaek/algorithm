import sys
input = sys.stdin.readline

dp = []
n = int(input())

for _ in range(n):
    dp.append(list(map(int, input().split())))

for y in range(1, n):
    for x in range(len(dp[y])):
        if x == 0:
            dp[y][x] = dp[y-1][x]+dp[y][x]
        elif x == len(dp[y])-1:
            dp[y][x] = dp[y-1][x-1] + dp[y][x]
        else:
            dp[y][x] = max(dp[y-1][x-1]+dp[y][x], dp[y-1][x] + dp[y][x])

print(max(dp[len(dp)-1]))

