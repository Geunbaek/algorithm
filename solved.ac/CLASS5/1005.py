import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]

    q = deque()
    ans = 0

    for _ in range(k):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    end = int(input())
    end_depth = 10**9

    for idx in range(1, n+1):
        if indegree[idx] == 0:
            q.append(idx)
            dp[idx] = arr[idx-1]

    while q:
        length = len(q)

        while length:
            now = q.popleft()

            for next in graph[now]:
                indegree[next] -= 1
                dp[next] = max(dp[now]+ arr[next-1], dp[next])
                if indegree[next] == 0:
                    q.append(next)

            length -= 1

    print(dp[end])




