import sys

input = sys.stdin.readline

def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
    return p[x]

def union(a, b):
    ap = find_p(a)
    bp = find_p(b)
    p[ap] = bp

v, e = map(int, input().split())
p = [i for i in range(v+1)]
edges = []
cost = 0

for _ in range(e):
    edges.append(list(map(int, input().split())))

edges.sort(key = lambda x: x[2])

for start, end, c in edges:
    if find_p(start) != find_p(end):
        union(start, end)
        cost += c

print(cost)