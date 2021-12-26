import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(k + 1)]

for _ in range(n):
    coins.append(int(input()))

dp[0] = 1
for coin in coins:
    for x in range(1, k + 1):
        if x - coin >= 0:
            dp[x] += dp[x - coin]

print(dp[k])
