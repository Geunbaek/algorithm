import sys
input = sys.stdin.readline
import heapq

n = int(input())
initTable = []
s = []

for _ in range(n):
    a, b, c = map(int, input().split())
    initTable.append((a, b, c))

table = sorted(initTable, key = lambda x: (x[-2]))
h = []
info = {}

for t in table:
    num, start, end = t
    if not h:
        heapq.heappush(h, (end, 1))
        info[num] = 1
        continue

    if h[0][0] <= start:
        first = heapq.heappop(h)
        heapq.heappush(h, (end, first[1]))
        info[num] = first[1]
    else:
        heapq.heappush(h, (end, len(h) + 1))
        info[num] = len(h)

print(len(h))
for i in range(1, len(table) + 1):
    print(info[i])
