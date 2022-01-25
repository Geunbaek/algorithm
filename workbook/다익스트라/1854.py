import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 9

def dij(start):
    dist = [[INF for _ in range(k)] for _ in range(n + 1)]
    h = []
    if len(dist[start]) > 1:
        dist[start].pop()
    else:
        dist[start][-1] = 0

    for node, cost in edges[start]:
        heapq.heappush(h, (cost, node))

    while h:
        total, cur = heapq.heappop(h)
        if dist[cur][-1] > total:
            if len(dist[cur]) > 1:
                dist[cur].pop()
            else:
                dist[cur][-1] = total
            for node, cost in edges[cur]:
                if cost + total < dist[node][-1]:
                    heapq.heappush(h, (total + cost, node))
    return dist

n, m, k = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

ans = dij(1)
for el in ans[1:]:
    if el[-1] == INF:
        print(-1)
    else:
        print(el[-1])