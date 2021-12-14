import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
degree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
q = deque()
ans = []

for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        if arr[i + 1] not in graph[arr[i]]:
            graph[arr[i]].append(arr[i+1])
            degree[arr[i + 1]] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    ans.append(now)
    for el in graph[now]:
        degree[el] -=1
        if degree[el] == 0:
            q.append(el)
if len(ans) == n:
    for el in ans:
        print(el)
else:
    print(0)


