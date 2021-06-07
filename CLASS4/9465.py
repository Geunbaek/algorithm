import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = []
    dp.append(list(map(int, input().split())))
    dp.append(list(map(int, input().split())))
    dp[0][1] = dp[0][1] + dp[1][0]
    dp[1][1] = dp[0][0] + dp[1][1]

    for x in range(2, n):
        for y in range(2):
            if y == 0:
                dp[y][x] = dp[y][x] + max(dp[y+1][x-1], dp[y][x-2], dp[y+1][x-2])
            elif y == 1:
                dp[y][x] = dp[y][x] + max(dp[y-1][x-1], dp[y][x-2], dp[y-1][x-2])

    max_val = max(dp[0][-1], dp[1][-1])
    print(max_val)