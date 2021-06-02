import sys
input = sys.stdin.readline
import heapq

def solve(start):
    h = []
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    for w, ne in edges[start]:
        heapq.heappush(h, (w, ne))

    while h:
        weight, now = heapq.heappop(h)
        if distance[now] > weight:
            distance[now] = weight
            for w, ne in edges[now]:
                heapq.heappush(h, (weight+w, ne))
    return distance[1:]

n, m, x = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, w = map(int, input().split())
    edges[start].append((w, end))


ans = solve(x)

result = 0
for i in range(1, n+1):
    result = max(result, ans[i-1] + solve(i)[x-1])


print(result)




