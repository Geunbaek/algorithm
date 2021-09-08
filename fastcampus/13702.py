import sys
input = sys.stdin.readline

n, k = map(int, input().split())
capacity = []

for _ in range(n):
    capacity.append(int(input()))

l = 0
r = 2 ** 31 - 1
ans = 0

while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for el in capacity:
        cnt += el // mid

    if cnt < k:
        r = mid - 1
    else:
        l = mid + 1
        ans = max(ans, mid)

print(ans)
