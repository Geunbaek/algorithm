import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
INF = 10 ** 9
item_cnt = list(map(int, input().split()))
distance = [[INF] * (n+1) for _ in range(n+1)]

for y in range(n+1):
    for x in range(n+1):
        if x == y:
            distance[y][x] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    distance[a][b] = l
    distance[b][a] = l

for k in range(n+1):
    for y in range(n+1):
        for x in range(n+1):
            distance[y][x] = min(distance[y][x], distance[y][k]+distance[k][x])

result = 0
for e in distance[1:]:
    val = 0
    for i, num in enumerate(e[1:]):
        if num <= m:
            val += item_cnt[i]

    result = max(result, val)

print(result)





