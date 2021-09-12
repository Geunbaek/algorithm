import sys
input = sys.stdin.readline
import heapq

def dij(s):
    h = []
    dist = [501 for _ in range(n+1)]
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


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for el in dij(1):
    if el == 1 or el == 2:
        cnt += 1

print(cnt)