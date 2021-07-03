import sys
input = sys.stdin.readline

INF = 10**9

n = int(input())
m = int(input())
cost = [[INF] * (n+1) for _ in range(n+1)]

for y in range(1, n+1):
    for x in range(1, n+1):
        if x == y:
            cost[y][x] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(1, n+1):
    for y in range(1, n+1):
        for x in range(1, n+1):
            cost[y][x] = min(cost[y][x], cost[y][k] + cost[k][x])

for y in range(1, n+1):
    for x in range(1, n+1):
        if cost[y][x] == INF:
            print(0, end = " ")
        else:
            print(cost[y][x], end = " ")
    print()