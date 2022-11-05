import sys
input = sys.stdin.readline

t, w = map(int, input().split())
treeInfo = []

dp = [[0 for _ in range(w + 1)] for _ in range(t)]
for _ in range(t):
    treeInfo.append(int(input()))

for y in range(t):
    for x in range(w + 1):
        if x == 0:
            if treeInfo[y] == 1:
                dp[y][0] = dp[y - 1][0] + 1
            else:
                dp[y][0] = dp[y - 1][0]
        else:
            if treeInfo[y] == 1 and x % 2 == 0:
                dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - 1]) + 1
            elif treeInfo[y] == 2 and x % 2 == 1:
                dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - 1]) + 1
            else:
                dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - 1])

print(max(dp[-1]))
