import sys
input = sys.stdin.readline
from collections import deque

def dfs(node, visit):
    visit[node] = 1
    print(node, end = " ")
    for next_node in graph[node]:
        if visit[next_node] == 0:
            dfs(next_node, visit)


def bfs():
    q = deque()
    q.append(v)
    visit = [0 for i in range(n+1)]
    visit[v] = 1
    while q:
        now = q.popleft()
        print(now, end = " ")
        for next_node in graph[now]:
            if visit[next_node] == 0:
                visit[next_node] = 1
                q.append(next_node)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for node in graph:
    node.sort()

visit= [0 for i in range(n+1)]
dfs(v, visit)
print()
bfs()

