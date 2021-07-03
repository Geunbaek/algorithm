import sys
input = sys.stdin.readline
import heapq

n = int(input())
h = []

for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(h, num)
    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
