import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(node, depth):
    global cnt
    visited[node] = 1
    count = 0
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i, depth+1)
            count += 1
    if not count:
        cnt += depth

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
cnt = 0

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

if cnt % 2 == 0:
    print('No')
else:
    print("Yes")
