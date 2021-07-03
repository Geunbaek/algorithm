import sys

input = sys.stdin.readline

s1 = '0' + input().strip()
s2 = '0' + input().strip()

dp = [[[0, []] for _ in range(len(s1))] for _ in range(len(s2))]


for y in range(1, len(s2)):
    for x in range(1, len(s1)):
        if s1[x] == s2[y]:
            dp[y][x][0] = max(max(dp[y-1][x][0], dp[y][x-1][0]), dp[y-1][x-1][0] + 1)
            dp[y][x][1] = dp[y-1][x-1][1] + [s1[x]]
        else:
            dp[y][x][0] = max(dp[y-1][x][0], dp[y][x-1][0])
            dp[y][x][1] = max(dp[y][x-1][1], dp[y-1][x][1], key = lambda x:len(x))

print(dp[-1][-1][0])
print(''.join(dp[-1][-1][1]))
