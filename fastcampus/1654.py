import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []

for _ in range(k):
    lines.append(int(input()))

max_line = max(lines)
ans = 0

l = 1
r = max_line
while l <= r:
    mid = (l + r) // 2
    count = 0
    for line in lines:
        count += line // mid
    if count < n:
        r = mid - 1
    else:
        l = mid + 1
        ans = max(ans, mid)

print(ans)



