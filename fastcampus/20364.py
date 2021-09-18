import sys
input = sys.stdin.readline

def dfs(node, target, ans):
    if node <= 0:
        print(ans)
        visited[target] = 1
        return
    if visited[node]:
        dfs(node // 2, target, node)
    else:
        dfs(node // 2, target, ans)



n, q = map(int, input().split())
visited = [0 for _ in range(n + 1)]

for _ in range(q):
    target = int(input())
    dfs(target, target, 0)