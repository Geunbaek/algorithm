import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = []

for _ in range(n):
    w.append(int(input()))

l = max(w)
r = 1000000000
ans = 1000000000

while l <= r:
    mid = (l + r) // 2
    now, cnt = 0, 0
    for el in w:
        if now + el > mid:
            now = 0
            cnt += 1
        now += el
    if now != 0:
        cnt += 1

    if cnt > m:
        l = mid + 1
    else:
        r = mid - 1
        ans = min(ans, mid)
print(ans)
