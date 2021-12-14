import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end = ' ')
    for el in graph[now]:
        degree[el] -= 1
        if degree[el] == 0:
            q.append(el)


