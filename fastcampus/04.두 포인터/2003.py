import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

r, total, ans = -1, 0, 0

for l in range(n):
    while r + 1 < n and total < m:
        r += 1
        total += arr[r]

    if total == m:
        ans += 1

    total -= arr[l]

print(ans)