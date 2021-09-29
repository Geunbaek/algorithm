import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 100001
ans = 0
r = -1

for l in range(n):
    while r + 1 < n and cnt[arr[r + 1]] == 0:
        r += 1
        cnt[arr[r]] += 1
    ans += r - l + 1
    cnt[arr[l]] -= 1

print(ans)
