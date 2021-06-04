import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

result = []

def dfs(start, depth):
    for ne, c in tree[start]:
        if visit[ne] != 1:
            break
    else:
        result.append((start, depth))
        return

    visit[start] = 1

    for ne, c in tree[start]:
        if visit[ne] == 0:
            dfs(ne, depth+c)



n = int(input())
tree = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int,input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

dfs(1, 0)
result.sort(key = lambda x: x[1])
idx = result[-1][0]

visit = [0 for _ in range(n+1)]
result = []
dfs(idx, 0)
print(max(result, key = lambda x:x[1])[1])






