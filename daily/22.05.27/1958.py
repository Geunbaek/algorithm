import sys
input = sys.stdin.readline

str1 = " " + input().strip()
str2 = " " + input().strip()
str3 = " " + input().strip()
dp = [[[0 for _ in range(len(str3))] for _ in range(len(str2))] for _ in range(len(str1))]

for z in range(1, len(str1)):
    for y in range(1, len(str2)):
        for x in range(1, len(str3)):
            if str1[z] == str2[y] and str1[z] == str3[x]:
                dp[z][y][x] = dp[z - 1][y - 1][x - 1] + 1
            else:
                dp[z][y][x] = max(dp[z - 1][y][x], dp[z][y - 1][x], dp[z][y][x - 1]);

print(dp[-1][-1][-1])