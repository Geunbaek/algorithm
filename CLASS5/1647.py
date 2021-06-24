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

n, m = map(int, input().split())
edges = []
p = [i for i in range(n+1)]
cost = 0

for _ in range(m):
    edges.append(list(map(int, input().split())))

edges.sort(key = lambda x: x[2])

cnt = 0

for start, end, c in edges:
    if find_p(start) != find_p(end):
        union(start, end)
        cost += c
        cnt += 1

    if cnt == n-2:
        break

print(cost)