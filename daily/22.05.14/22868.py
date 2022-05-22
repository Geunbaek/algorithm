import sys
input = sys.stdin.readline
from collections import deque

def up():
    q = deque()
    q.append((s, [s]))

    while q:
        now, path = q.popleft()
        if now == e:
            return path
        for node in graph[now]:
            if node not in path:
                q.append((node, path + [node]))

def down(p):
    q = deque()
    for node in graph[e]:
        if node not in p:
            q.append((node, p + [node]))

    while q:
        now, path = q.popleft()
        for node in graph[now]:
            if node not in path:
                q.append((node, path + [node]))
            elif node == s:
                return path

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for el in graph:
    el.sort()
s, e = map(int, input().split())

print(len(down(up())))





