import sys
input = sys.stdin.readline

def find( x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union( a, b):
    ap = find(a)
    bp = find(b)
    p[ap] = bp

n, k = map(int, input().split())
edges = []
p = [i for i in range(n)]

for _ in range(k):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    edges.append((b, a, c))

edges.sort(key = lambda x: x[2])
cost = 0
mst = [[] for _ in range(n)]
node = -1
for a, b, c in edges:
    if find(a) != find(b):
        node = a
        union(a, b)
        mst[a].append((b, c))
        mst[b].append((a, c))
        cost += c

values = []

def dfs(node, cost):
    max_val = []
    visit[node] = 1
    for ne, c in mst[node]:
        if visit[ne] == 0:
            max_val.append(dfs(ne, c))

    if not max_val:
        return cost

    max_val.sort()
    if len(max_val) >= 2:
        values.append(max_val[-1] + max_val[-2])
    values.append(max_val[-1] + cost)

    return max_val[-1] + cost

visit = [0 for _ in range(n)]
dfs(node, 0)
values.sort()
print(cost)
print(values[-1])


