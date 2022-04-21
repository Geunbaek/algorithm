import math
import sys
input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    if pos[ap][-1] < pos[bp][-1]:
        p[bp] = ap
    else:
        p[ap] = bp

def check(s, c):
    x = abs(s[1] - c[1])
    y = abs(s[2] - c[2])
    z = s[-1] + c[-1]
    return x * x + y * y <= z * z

t = int(input())

for _ in range(t):
    n = int(input())
    p = []
    pos = []

    for i in range(n):
        x, y, r = map(int, input().split())
        p.append(i)
        pos.append((i, x, y, r))

    for i in range(len(pos)):
        for j in range(i - 1, -1, -1):
            if i == j:
                continue
            if check(pos[i], pos[j]) and p[i] != p[j]:
                union(i, j)

    count = set()
    for i in p:
        count.add(find(i))
    print(len(count))
