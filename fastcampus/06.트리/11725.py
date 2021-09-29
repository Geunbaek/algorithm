import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**8)

def dfs(node):
    visit[node] = 1
    for child in graph[node]:
        if visit[child] == 0:
            parent[child] = node
            dfs(child)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = defaultdict(int)
visit = [0 for _ in range(n+1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
ans = sorted(parent.items())
for _, p in ans:
    print(p)



