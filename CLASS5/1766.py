import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
q = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    print(now, end = ' ')
    for ne in graph[now]:
        in_degree[ne] -=1
        if in_degree[ne] == 0:
            heapq.heappush(q, ne)



