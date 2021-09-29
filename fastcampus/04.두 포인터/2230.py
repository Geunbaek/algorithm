import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
r = 0
ans = 2000000001

for l in range(n):
    while r + 1 < n and arr[r] - arr[l] < m:
        r += 1
    if arr[r] - arr[l] >= m:
        ans = min(ans, arr[r] - arr[l])

print(ans)