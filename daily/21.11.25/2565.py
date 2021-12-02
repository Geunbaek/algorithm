import sys
input = sys.stdin.readline

n = int(input())
max_val = 0
connect = []

for _ in range(n):
    a, b = map(int, input().split())
    connect.append((a, b))

connect.sort()
dp = [0] * 501

for y in range(1, len(connect) + 1):
    for x in range(y + 1):
        if connect[y-1][1] > connect[x-1][1] and dp[x] > dp[y]:
            dp[y] = dp[x]
    dp[y] +=1

print(len(connect) - max(dp))