import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((1, 0))
    dists = [-1 for _ in range(n + 1)]
    dists[1] = 0
    while q:
        now, dist = q.popleft()
        for ne in graph[now]:
            if dists[ne] == -1:
                dists[ne] = dist + 1
                q.append((ne, dist + 1))
    return map(str, dists[1:])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())

for _ in range(q):
    a, i, j = map(int, input().split())
    if a == 1:
        graph[i].append(j)
        graph[j].append(i)
    if a == 2:
        graph[i].remove(j)
        graph[j].remove(i)

    print(" ".join(bfs()))


