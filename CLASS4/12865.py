import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
items = []

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

for y in range(1,n+1):
    for x in range(1,k+1):
        if items[y-1][0] <= x:
            dp[y][x] = max(
                dp[y-1][x],
                items[y-1][1] + dp[y-1][x-items[y-1][0]]
            )
        else:
            dp[y][x] = dp[y-1][x]
print(dp[-1][-1])




