import sys
input = sys.stdin.readline
import heapq

n = int(input())
h = []

for _ in range(n):
    oper = int(input())

    if oper == 0:
        if not h:
            print(0)
        else:
            elem = heapq.heappop(h)
            print(elem[1])

    else:
        if oper > 0:
            heapq.heappush(h, (oper, oper))
        elif oper < 0:
            heapq.heappush(h, (abs(oper), oper))