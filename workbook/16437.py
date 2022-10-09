import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(now):
    s = 0
    for _, count, _next in graph[now]:
        s += dfs(_next)

    if now != 1:
        if info[now][0] == 'S':
            s += info[now][1]
        elif info[now][0] == 'W':
            s -= info[now][1]
    if s <= 0:
        s = 0
    return s

n = int(input())

graph = [[] for _ in range(n + 1)]
info = [0 for _ in range(n + 1)]
for i in range(n - 1):
    t, a, p = input().split()
    info[i + 2] = (t, int(a), p)
    graph[int(p)].append((t, int(a), i + 2))

print(dfs(1))
