import sys
input = sys.stdin.readline

def check(target, path):
    for node in path:
        if target not in graph[node]:
            return False
    return True

def dfs(depth, now, path):
    if depth >= k:
        ans.append(path)
        return

    if ans:
        return

    for next_ in graph[now]:
        if visited[next_] == 0 and len(graph[next_]) >= k - 1:
            if check(next_, path):
                visited[next_] = 1
                dfs(depth + 1, next_, path + [next_])
                visited[next_] = 0


k, n, f = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
ans = []

for _ in range(f):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

for line in graph:
    line.sort()

for i in range(1, n + 1):
    if len(graph[i]) >= k - 1:
        visited[i] = 1
        dfs(1, i, [i])
        visited[i] = 0

if ans:
    print("\n".join(map(str, ans[0])))
else:
    print(-1)