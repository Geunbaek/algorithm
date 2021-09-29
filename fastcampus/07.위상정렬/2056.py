import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
d = [0 for _ in range(n + 1)]
degree = {i + 1: 0 for i in range(n)}
dp = [0 for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
q = deque()

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    d[i] = arr[0]

    for el in arr[2:]:
        graph[el].append(i)
        degree[i] += 1

for key, val in degree.items():
    if val == 0:
        q.append(key)

for el in q:
    dp[el] = d[el]

while q:
    now = q.popleft()
    visit[now] = 1
    for el in graph[now]:
        degree[el] -= 1
        dp[el] = max(dp[el], dp[now] + d[el])
        if degree[el] == 0 and visit[el] == 0:
            q.append(el)

print(max(dp))


