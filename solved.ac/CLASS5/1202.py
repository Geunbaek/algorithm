import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
bags = []
rubys = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(rubys, (m, v))

for _ in range(k):
    bags.append(int(input()))

bags.sort()
# print(rubys)
# print(bags)

ans = 0
candidate = []

for el in bags:
    while rubys and rubys[0][0] <= el:
        heapq.heappush(candidate, -heapq.heappop(rubys)[1])

    if candidate:
        ans -= heapq.heappop(candidate)

print(ans)