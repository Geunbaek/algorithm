import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
    return p[x]

def union(a,b):
    ap = find_p(a)
    bp = find_p(b)
    p[ap] = bp

n, m = map(int, input().split())
p = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    if find_p(a) != find_p(b):
        union(a, b)

for i in range(1, n+1):
    find_p(i)

print(len(set(p[1:])))
