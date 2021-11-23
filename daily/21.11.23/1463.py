import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(1000001)]
dp[2] = 1
dp[3] = 1

for i in range(2, n + 1):
    temp = [sys.maxsize]
    if i % 3 == 0:
        temp.append(dp[i // 3] + 1)
    if i % 2 == 0:
        temp.append(dp[i // 2] + 1)

    dp[i] = min(min(temp), dp[i - 1] + 1)

print(dp[n])