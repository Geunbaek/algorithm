import sys
input = sys.stdin.readline

INF = sys.maxsize
n = int(input())
graph = []
check = [[0 for _ in range(n)] for _ in range(n)]
result = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for y in range(n):
        for x in range(n):
            if i == x or i == y or x == y:
                continue
            if graph[y][x] == graph[y][i] + graph[i][x]:
                check[y][x] = 1
            elif graph[y][x] > graph[y][i] + graph[i][x]:
                result = -1

if result != -1:
    for y in range(n):
        for x in range(y, n):
            if not check[y][x]:
                result += graph[y][x]

print(result)


