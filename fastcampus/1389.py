import sys
input = sys.stdin.readline
import heapq

def dij(s):
    h = []
    dist = [50001 for _ in range(n+1)]
    dist[s] = 0

    for ne in graph[s]:
        heapq.heappush(h, (1, ne))

    while h:
        cost, now = heapq.heappop(h)
        if dist[now] > cost:
            dist[now] = cost
            for ne in graph[now]:
                heapq.heappush(h, (cost + 1, ne))

    return dist[1:]


n, m = map(int, input().split())
result = []

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    result.append((i, sum(dij(i))))

result.sort(key = lambda x:(x[1], x[0]))
print(result[0][0])


