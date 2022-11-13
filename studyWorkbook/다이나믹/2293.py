import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for x in range(k + 1):
        if x - coin >= 0:
            dp[x] += dp[x - coin]
print(dp[-1])

"""
3 10
1
2
5
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
[1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]

"""