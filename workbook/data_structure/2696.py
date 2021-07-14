import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    arr = []
    while m > 10:
        arr.extend(list(map(int, input().split())))
        m -= 10

    arr.extend(list(map(int, input().split())))
    h = []
    temp = []
    ans = []

    for i, num in enumerate(arr):
        heapq.heappush(h, (i, num))

    for i in range(0, len(arr)):
        temp.append(heapq.heappop(h)[1])
        if i % 2 == 0:
            temp.sort()
            ans.append(temp[len(temp)//2])


    print(len(ans))
    for e in ans:
        print(e, end = ' ')
    print()