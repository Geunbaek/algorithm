import sys
input = sys.stdin.readline

def dfs(node, total):
    ans = []
    flag = False
    for c, next_ in graph[node]:
        if visited[next_] == 0:
            visited[next_] = 1
            ans.append(dfs(next_, total + c))
            visited[next_] = 0
            flag = True

    if not flag:
        return total
    return max(ans)

edges = []
max_node = 0

while True:
    try:
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
        max_node = max(max_node, u, v)
    except:
        break

graph = [[] for _ in range(max_node + 1)]
visited = [0 for _ in range(max_node + 1)]
ans = 0

for u, v, c in edges:
    graph[u].append((c, v))
    graph[v].append((c, u))


for i in range(1, max_node + 1):
    visited[i] = 1
    ans = max(ans, dfs(i, 0))
    visited[i] = 0
print(ans)
