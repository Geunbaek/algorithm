import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

r, ans, cnt = -1, n + 1, 0

for l in range(n):
    while r + 1 < n and cnt < k:
        r += 1
        if arr[r] == 1:
            cnt += 1
    if cnt == k:
        ans = min(ans, r - l + 1)

    if arr[l] == 1:
        cnt -= 1

if ans == n + 1:
    print(-1)
else:
    print(ans)