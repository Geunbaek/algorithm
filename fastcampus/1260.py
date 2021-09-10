import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for el in graph:
    el.sort()

def bfs(start):
    q = deque()
    visit = [0 for _ in range(n+1)]
    q.append(start)
    visit[start] = 1

    while q:
        now = q.popleft()
        print(now, end = ' ')
        for ne in graph[now]:
            if visit[ne] == 0:
                q.append(ne)
                visit[ne] = 1

def dfs(start):
    print(start, end = " ")
    visited[start] = 1
    for ne in graph[start]:
        if visited[ne] == 0:
            dfs(ne)

dfs(v)
print()
bfs(v)
