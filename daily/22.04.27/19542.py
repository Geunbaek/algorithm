import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(node):
    temp = []

    for el in graph[node]:
        if visit[el] == 0:
            visit[el] = 1
            temp.append(dfs(el))

    if len(temp) == 0:
        return -d + 1

    if len(temp) == 1:
        return temp[0] + 1
    else:
        ret = list(filter(lambda x: x > 0, temp))
        return sum(ret) + 1 if ret else max(temp) + 1

n, s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = 0
visit[s] = 1
for el in graph[s]:
    visit[el] = 1
    temp = dfs(el)
    ans += temp if temp > 0 else 0
print(ans * 2)
