import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

r, total, ans = -1, 0, n + 1

for l in range(n):
    while r + 1 < n and total < s:
        r += 1
        total += arr[r]

    if total >= s:
        ans = min(ans, r - l + 1)

    total -= arr[l]

if ans == n+1:
    print(0)
else:
    print(ans)