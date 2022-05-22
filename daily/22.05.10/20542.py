import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = " " + input().strip()
b = " " + input().strip()

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for x in range(1, m + 1):
    dp[0][x] = x

for y in range(1, n + 1):
    dp[y][0] = y


info = {
    "i": {"j", "l"},
    "v": {'w'}
}


for y in range(1, n + 1):
    for x in range(1, m + 1):
        if a[y] == b[x] or (a[y] in info and b[x] in info[a[y]]) :
            dp[y][x] = dp[y - 1][x - 1]
        else:
            dp[y][x] = min(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1]) + 1

print(dp[-1][-1])