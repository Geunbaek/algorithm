import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
m = int(input())

l = 1
r = m
ans = 0

while l <= r:
    mid = (l + r) // 2
    cost = 0
    for re in req:
        cost += re if mid >= re else mid
    if cost > m:
        r = mid - 1
    else:
        l = mid + 1
        ans = max(ans, mid)
if ans > max(req):
    print(max(req))
else:
    print(ans)