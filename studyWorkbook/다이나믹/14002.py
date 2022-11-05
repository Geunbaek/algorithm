import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[1, []] for _ in range(n)]

for y in range(n):
    for x in range(y):
        if arr[x] < arr[y]:
            if dp[y][0] > dp[x][0] + 1:
                dp[y] = dp[y][:]
            else:
                dp[y][0] = dp[x][0] + 1
                dp[y][1] = dp[x][1] + [arr[x]]

_max = [0, 0]
_max_index = 0

for i, el in enumerate(dp):
    if _max[0] < el[0]:
        _max = el
        _max_index = i

print(_max[0])
print(" ".join(map(str, _max[1] + [arr[_max_index]])))

