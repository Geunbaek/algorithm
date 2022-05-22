import sys
input = sys.stdin.readline
import heapq

n = int(input())
schedule = []
h = []
for _ in range(n):
    a, b = map(int, input().split())
    schedule.append((a, b))

schedule.sort()
for i in range(len(schedule)):
    if h and h[0] <= schedule[i][0]:
        heapq.heappop(h)
    heapq.heappush(h, schedule[i][-1])

print(len(h))