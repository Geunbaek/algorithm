import sys
input = sys.stdin.readline
import heapq

def dij(start, end):
    INF = 100000001
    dist = [INF for _ in range(n + 1)]
    h = []
    dist[start] = 0
    for node, c in graph[start]:
        heapq.heappush(h, (c, node))

    while h:
        cur, now = heapq.heappop(h)
        if dist[now] > cur:
            dist[now] = cur
            for node, c in graph[now]:
                heapq.heappush(h, (c+cur, node))

    return dist[end]

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

s, e = map(int, input().split())
print(dij(s, e))