import sys
input = sys.stdin.readline

str1 = " " + input().strip()
str2 = " " + input().strip()

dp = [[[0, ""] for _ in range(len(str1))] for _ in range(len(str2))]

for y in range(1, len(str2)):
    for x in range(1, len(str1)):
        if str1[x] == str2[y]:
            dp[y][x][0] = dp[y - 1][x - 1][0] + 1
            dp[y][x][1] = dp[y - 1][x - 1][1] + str1[x]
        else:
            if dp[y - 1][x][0] > dp[y][x - 1][0]:
                dp[y][x][0] = dp[y - 1][x][0]
                dp[y][x][1] = dp[y - 1][x][1]
            else:
                dp[y][x][0] = dp[y][x - 1][0]
                dp[y][x][1] = dp[y][x - 1][1]


print(dp[-1][-1][0])
print(dp[-1][-1][1])
