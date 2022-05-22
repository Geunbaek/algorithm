import sys
input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    p[ap] = bp

n, m = map(int, input().split())
cost = []
p = [i for i in range(n + 1)]
edges = []
ans = 0
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    count += 1
    union(x, y)

for y in range(n):
    line = list(map(int, input().split()))
    for x in range(n):
        if x == 0 or y == 0:
            continue
        if x != y:
            edges.append((x + 1, y + 1, line[x]))

edges.sort(key = lambda x: x[2])
start = count
connect = []
for u, v, c in edges:
    if find(u) != find(v):
        union(u, v)
        ans += c
        count += 1
        connect.append([u, v])

print(ans, count - start)
for c in connect:
    print(*c)



