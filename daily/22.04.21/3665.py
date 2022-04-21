import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    rank = list(map(int, input().split()))
    edges = [[] for _ in range(n + 1)]
    degree = [0 for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            edges[rank[i]].append(rank[j])
            degree[rank[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in edges[a]:
            edges[a].remove(b)
            edges[b].append(a)
            degree[a] += 1
            degree[b] -= 1
        elif a in edges[b]:
            edges[b].remove(a)
            edges[a].append(b)
            degree[b] += 1
            degree[a] -= 1

    q = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)

    ans = []
    while q:
        now = q.popleft()
        ans.append(now)
        for el in edges[now]:
            degree[el] -= 1
            if degree[el] == 0:
                q.append(el)
    if len(ans) == len(rank):
        print(" ".join(map(str, ans)))
    else:
        print("IMPOSSIBLE")


