import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
sums = [0 for _ in range(n + 1)]
mod = 1_000_000_007

for x in range(k + 1):
    dp[1][x] = 1

sums[1] = k
for y in range(2, n + 1):
    for x in range(1, k + 1):
        temp = 0
        for i in range(2 * x, k + 1, x):
            temp += dp[y - 1][i]
            temp %= mod
        dp[y][x] = sums[y - 1] - temp
        dp[y][x] %= mod
        sums[y] += dp[y][x]
        sums[y] %= mod

print(sums[n])
