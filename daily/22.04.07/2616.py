import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
t = int(input())

sums = [0 for _ in range(n)]
sums[0] = arr[0]

for i in range(1, n):
    sums[i] = sums[i - 1] + arr[i]

dp = [[0 for _ in range(n + 1)] for _ in range(4)]

for y in range(1, 4):
    for x in range(y * t, n + 1):
        if y == 1:
            if x - t - 1 < 0:
                dp[y][x] = max(dp[y][x - 1], sums[x - 1])
            else:
                dp[y][x] = max(dp[y][x - 1], sums[x - 1] - sums[x - t - 1])
        else:
            if x - t - 1 < 0:
                dp[y][x] = max(dp[y][x - 1], dp[y - 1][x - t] + sums[x - 1])
            else:
                dp[y][x] = max(dp[y][x - 1], dp[y - 1][x - t] + sums[x - 1] - sums[x - t - 1])

print(dp[-1][-1])