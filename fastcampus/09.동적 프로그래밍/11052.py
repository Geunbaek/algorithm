import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(len(arr))]

for y in range(len(arr)):
    for x in range(1, n + 1):
        if (y + 1) > x:
            dp[y][x] = dp[y-1][x]
        else:
            dp[y][x] = max(dp[y][x - (y+1)] + arr[y], dp[y-1][x])

print(dp[-1][-1])