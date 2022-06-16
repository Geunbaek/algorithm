import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = sys.maxsize
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

dist = [[x for x in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = "-"

for k in range(1, n + 1):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if graph[y][x] > graph[y][k] + graph[k][x]:
                graph[y][x] = graph[y][k] + graph[k][x]
                dist[y][x] = dist[y][k]

for d in dist[1:]:
    print(*d[1:])

