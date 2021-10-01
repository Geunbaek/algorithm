import sys
input = sys.stdin.readline
import heapq

def dij(start):
    dist[start] = 0
    for node, c in graph[start]:
        heapq.heappush(h, (c, node))

    while h:
        cur, now = heapq.heappop(h)
        if dist[now] > cur:
            dist[now] = cur
            for node, c in graph[now]:
                if dist[node] > cur + c:
                    heapq.heappush(h, (c + cur, node))

v, e = map(int, input().split())
k = int(input())
h = []
dist = [float('inf') for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))

dij(k)
for el in dist[1:]:
    if el != float('inf'):
        print(el)
    else:
        print("INF")