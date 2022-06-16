import sys
input = sys.stdin.readline
from collections import deque

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    p[ap] = bp

n, m, k = map(int, input().split())
edges = deque()

for i in range(m):
    x, y = map(int, input().split())
    edges.append((x, y, i + 1))

while k:
    count = 0
    total = 0
    p = [i for i in range(n + 1)]
    for u, v, c in edges:
        if find(u) != find(v):
            union(u, v)
            total += c
            count += 1
    if count == n - 1:
        print(total, end = " ")
    else:
        print(0, end = " ")

    edges.popleft()
    k -= 1

