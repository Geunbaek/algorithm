import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m + 1)]
    dp[0] = 1
    for coin in coins:
        for x in range(1, m + 1):
            if x - coin >= 0:
                dp[x] += dp[x - coin]
    print(dp[-1])
