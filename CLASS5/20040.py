import sys

input = sys.stdin.readline
sys.setrecursionlimit(500001)

def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
    return p[x]

def union(a, b):
    ap = find_p(a)
    bp = find_p(b)
    p[ap] = bp

n, m = map(int, input().split())
p = [i for i in range(n)]
ans = 0

for i in range(m):
    u, v = map(int, input().split())
    if find_p(u) != find_p(v):
        union(u, v)
    else:
        ans = i + 1
        break

print(ans)