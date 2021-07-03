n = int(input())

dp = [0 for i in range(100000)]
for i in range(1, 100000):
    dp[i] = 1 + 3 * (i**2 - i)
    if dp[i] >= n:
        print(i)
        break
