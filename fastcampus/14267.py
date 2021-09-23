import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(i, prev):

    if dp[i] == 0:
        dp[i] = dp[prev]
    else:
        dp[i] += dp[prev]

    for ne in graph[i]:
        if ne != prev:
            dfs(ne, i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

arr = list(map(int, input().split()))

for idx, el in enumerate(arr):
    if el != -1:
        graph[idx + 1].append(el)
        graph[el].append(idx + 1)

for _ in range(m):
    i, w = map(int, input().split())
    dp[i] += w

dfs(1, 0)

for el in dp[1:]:
    print(el, end = ' ')

"""
5 3
-1 1 1 2 2
2 2
3 4
5 6
"""