import sys
input = sys.stdin.readline
import heapq

n = int(input())
left = []
right = []

for _ in range(n):
    num = int(input())
    if not left or not right:
        heapq.heappush(right, -num)
    else:
        if num > -right[0]:
            heapq.heappush(left, num)
        else:
            heapq.heappush(right, -num)

    while not (len(left) == len(right) or len(left) + 1 == len(right)):
        if len(left) > len(right):
            heapq.heappush(right, -heapq.heappop(left))
        else:
            heapq.heappush(left,  -heapq.heappop(right))

    print(-right[0])
