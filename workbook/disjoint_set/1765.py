import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    parent[ap] = bp

n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
e = [[] for i in range(n + 1)]

for _ in range(m):
    r, p, q = input().split()
    p, q = int(p), int(q)
    if r == "F":
        union(p, q)
    else:
        e[p].append(q)
        e[q].append(p)

for i, enemy in enumerate(e):
    if i == 0:
        continue

    for j in enemy:
        for f in e[j]:
            if f == i:
                continue
            union(f, i)

count = set()

for i in range(1, n + 1):
    count.add(find(i))

print(len(count))