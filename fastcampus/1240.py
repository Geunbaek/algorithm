# dfs
# import sys
# input = sys.stdin.readline
#
# def dfs(a, b, length):
#     if a == b:
#         print(length)
#         return
#     visited[a] = 1
#     for ne, w in graph[a]:
#         if visited[ne] == 0:
#             dfs(ne, b, length+w)
#
#
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(n - 1):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     visited = [0 for _ in range(n + 1)]
#     dfs(a, b, 0)

# dijstra

import sys
input = sys.stdin.readline
import heapq

def sol(start, end):
    h = []
    dist = [float('inf') for _ in range(n + 1)]
    for ne, w in graph[start]:
        heapq.heappush(h, (ne, w))

    while h:
        now, cost = heapq.heappop(h)
        if dist[now] > cost:
            dist[now] = cost
            for ne, w in graph[now]:
                heapq.heappush(h, (ne, w + cost))
    return dist[end]



n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for _ in range(m):
    a, b = map(int, input().split())
    print(sol(a, b))









