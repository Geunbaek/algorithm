import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    degree = {i: 0 for i in range(1, n + 1)}
    graph = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    q = deque()

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        degree[y] += 1

    for key, val in degree.items():
        if val == 0:
            q.append(key)

    target = int(input())
    for i in range(len(q)):
        dp[q[i]] = d[q[i]]
    while q:
        now = q.popleft()
        visited[now] = 1
        for el in graph[now]:
            degree[el] -= 1
            dp[el] = max(dp[el], dp[now] + d[el])
            if degree[el] == 0 and visited[el] == 0:
                q.append(el)

    if dp[target]:
        print(dp[target])
    else:
        print(d[target])
