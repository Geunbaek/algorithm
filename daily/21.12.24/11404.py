import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
INF = sys.maxsize
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for y in range(n + 1):
    for x in range(n + 1):
        if x == y:
            graph[y][x] = 0

for z in range(n + 1):
    for y in range(n + 1):
        for x in range(n + 1):
            graph[y][x] = min(graph[y][x], graph[y][z] + graph[z][x])

for y in range(1, n + 1):
    for x in range(1, n + 1):
        if graph[y][x] == INF:
            graph[y][x] = 0

for line in graph[1:]:
    print(*line[1:])
