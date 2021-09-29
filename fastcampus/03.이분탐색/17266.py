import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

pos_x = list(map(int, input().split()))

l = 1
r = 100000
ans = sys.maxsize

while l <= r:
    mid = (l + r) // 2
    now = 0
    ck = True
    for el in pos_x:
        if el - now <= mid:
            now = el + mid
        else:
            break
    ck = now >= n

    if ck:
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1


print(ans)

