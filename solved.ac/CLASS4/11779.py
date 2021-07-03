import sys
input = sys.stdin.readline
import heapq

INF = 10**9

def sol(node):
    h = []
    distance = [INF] * (n+1)
    distance[node] = 0
    paths = {}
    for c, next in graph[node]:
        heapq.heappush(h, (c, next, [node, next]))

    while h:
        cost, now, path = heapq.heappop(h)
        if distance[now] > cost:
            distance[now] = cost
            paths[now] = path
            for c, next in graph[now]:
                new_path = path + [next]
                heapq.heappush(h, (cost+c, next, new_path))
    return distance[1:], paths


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append((c, v))

start, end = map(int, input().split())
dist, path = sol(start)
print(dist[end-1])
print(len(path[end]))
for i in path[end]:
    print(i, end = ' ')

