import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []

for _ in range(n):
    s, t = map(int, input().split())
    arr.append((s, t))

ans = []
arr.sort()
heapq.heappush(ans, (arr[0][1], arr[0][0]))

for i in range(1, len(arr)):
    end, start = heapq.heappop(ans)
    if end <= arr[i][0]:
        end = arr[i][1]
        heapq.heappush(ans, (end, start))
    else:
        heapq.heappush(ans, (end, start))
        heapq.heappush(ans, (arr[i][1], arr[i][0]))

print(len(ans))
