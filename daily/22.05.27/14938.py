import sys
input = sys.stdin.readline
import heapq

def dij(start):
    h = []
    heapq.heappush(h, (0, start))
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0

    while h:
        total, now = heapq.heappop(h)
        if dist[now] < total: continue

        for cost, next_ in edges[now]:
            if dist[next_] > total + cost:
                dist[next_] = total + cost
                heapq.heappush(h, (total + cost, next_))
    return dist[1:]




n, m, r = map(int, input().split())
arr = list(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
INF = sys.maxsize
ans = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    edges[a].append((l, b))
    edges[b].append((l, a))

for i in range(1, n + 1):
    temp = 0
    for index, d in enumerate(dij(i)):
        if d <= m:
            temp += arr[index]
    ans = max(ans, temp)

print(ans)

