import sys
input = sys.stdin.readline

n, c = map(int, input().split())
pos = []
ans = 0

for _ in range(n):
    pos.append(int(input()))

pos.sort()

l = 0
r = pos[-1]

while l <= r:
    mid = (l + r) // 2
    now = pos[0]
    cnt = 1
    for el in pos:
        if now + mid <= el:
            now = el
            cnt += 1
        if cnt == c:
            ans = max(ans, mid)
            break
    if cnt >= c:
        l = mid + 1
    else:
        r = mid - 1
print(ans)



