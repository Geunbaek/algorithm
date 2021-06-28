import sys

input = sys.stdin.readline

n = int(input())
rgbs = []
result = float('inf')
dp = [[0 for _ in range(3)] for _ in range(n)]

for _ in range(n):
    rgbs.append(list(map(int, input().split())))

for y in range(3):
    for x in range(3):
        if y == x:
            dp[0][x] = rgbs[0][x]
            continue

        dp[0][x] = float('inf')

    for i in range(1, n):
        dp[i][0] = rgbs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = rgbs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rgbs[i][2] + min(dp[i-1][0], dp[i-1][1])

    for i in range(3):
        if i == y:
            continue
        result = min(result, dp[-1][i])

print(result)






