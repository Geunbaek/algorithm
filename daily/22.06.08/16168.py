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

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
degree = [0 for _ in range(v + 1)]
p = [i for i in range(v + 1)]
count = 0
g = set()

for _ in range(e):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    degree[a] += 1
    degree[b] += 1

for i in range(1, v + 1):
    if degree[i] % 2 != 0:
        count += 1

for i in range(1, v + 1):
    g.add(find(i))

if len(g) == 1 and (count == 0 or count == 2):
    print("YES")
else:
    print("NO")


