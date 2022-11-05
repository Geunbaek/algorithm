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

n, m, k = map(int, input().split())
p = [i for i in range(n + 1)]
arr = list(map(int, input().split()))
answer = 0

for el in arr[1:]:
    union(arr[0], el)

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        answer += w

print(answer)