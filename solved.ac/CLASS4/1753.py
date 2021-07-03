import sys
input = sys.stdin.readline
import heapq

def solve(start):
    h = []
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    for cost, node in graph[start]:
        heapq.heappush(h, (cost, node))
    while h:
        weight, now = heapq.heappop(h)
        if dist[now] > weight:
            dist[now] = weight
            for cost, node in graph[now]:
                heapq.heappush(h, (weight+cost, node))

    return dist[1:]

n, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n+1)]

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

ans = solve(k)
for i in ans:
    if i != float('inf'):
        print(i)
    else:
        print("INF")
