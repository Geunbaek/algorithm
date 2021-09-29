import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
degree = {i + 1: 0 for i in range(n)}
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    degree[x] += 1

q = deque()
for key, val in degree.items():
    if val == 0:
        q.append(key)
        dp[key][key] = 1

while q:
    now = q.popleft()
    for el, val in graph[now]:
        degree[el] -= 1
        for i in range(1, n + 1):
            dp[el][i] += dp[now][i] * val
        if degree[el] == 0:
            q.append(el)

for idx in range(1, n + 1):
    if dp[n][idx] != 0:
        print(idx, dp[n][idx])


