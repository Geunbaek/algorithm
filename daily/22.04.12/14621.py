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

def gender(a, b):
    if arr[a - 1] == "M" and arr[b - 1] == "W":
        return True
    elif arr[a - 1] == "W" and arr[b - 1] == "M":
        return True
    return False

n, m = map(int, input().split())
arr = input().strip().split()
p = [i for i in range(n + 1)]
edges = []
ans = 0

for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((u, v, d))

edges.sort(key = lambda x : x[2])
count = 0
for u, v, d in edges:
    if gender(u, v) and find(u) != find(v):
        union(u, v)
        ans += d
        count += 1
    if count == n - 1:
        break

print(ans if count == n - 1 else -1)