import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
degree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)]
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    degree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

count = 1
while q:
    length = len(q)
    while length:
        now = q.popleft()
        ans[now] = count
        for el in graph[now]:
            degree[el] -= 1
            if degree[el] == 0:
                q.append(el)
        length -= 1
    count += 1

print(*ans[1:])