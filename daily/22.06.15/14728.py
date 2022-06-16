import sys
input = sys.stdin.readline

n, t = map(int, input().split())
parts = []

for _ in range(n):
    k, s = map(int, input().split())
    parts.append((k, s))

dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for y in range(1, n + 1):
    for x in range(1, t + 1):
        if x < parts[y - 1][0]:
            dp[y][x] = dp[y - 1][x]
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - parts[y - 1][0]] + parts[y - 1][1])

print(dp[-1][-1])
