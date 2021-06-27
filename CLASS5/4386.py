import sys
input = sys.stdin.readline
import math

def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
    return p[x]

def union(a, b):
    ap = find_p(a)
    bp = find_p(b)
    p[ap] = bp


n = int(input())
points = []
edges = []
p = [i for i in range(n+1)]
cost = 0

for _ in range(n):
    points.append(list(map(float, input().split())))

for i in range(n):
    for j in range(n):
        if i != j:
            edges.append((i, j, math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)))

edges.sort(key = lambda x:x[2])

for edge in edges:
    if find_p(edge[0]) != find_p(edge[1]):
        union(edge[0], edge[1])
        cost += edge[2]

print(cost)