import sys
input = sys.stdin.readline

def dfs(node, path):
    if node == b:
        if sum(path) <= c:
            ans.append(max(path))
        return

    for next_node, cost in edges[node]:
        if visit[next_node] == 0:
            visit[next_node] = 1
            dfs(next_node, path + [cost])
            visit[next_node] = 0

n, m, a, b, c = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
ans = []

for _ in range(m):
    u, v, cost = map(int, input().split())
    edges[u].append((v, cost))
    edges[v].append((u, cost))
visit[a] = 1
dfs(a, [])
print(min(ans) if ans else -1)
