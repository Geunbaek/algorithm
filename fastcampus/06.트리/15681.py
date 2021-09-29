import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(node, prev):
    dp[node] = 1
    for ne in graph[node]:
        if ne != prev:
            dfs(ne, node)
            dp[node] += dp[ne]

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r, -1)

for _ in range(q):
    u = int(input())
    print(dp[u])






