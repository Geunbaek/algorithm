import sys
input = sys.stdin.readline

a = " " + input().strip()
b = " " + input().strip()

dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

for y in range(1, len(a)):
    for x in range(1, len(b)):
        if a[y] != b[x]:
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
        else:
            dp[y][x] = dp[y - 1][x - 1] + 1

print(dp[-1][-1])
"""
ACAYKP
CAPCAK

[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 2, 2, 2]
[0, 1, 2, 2, 2, 3, 3]
[0, 1, 2, 2, 2, 3, 3]
[0, 1, 2, 2, 2, 3, 4]
[0, 1, 2, 3, 3, 3, 4]
"""