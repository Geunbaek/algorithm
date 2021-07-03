import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
q.append(1)
visit = [0 for _ in range(n+1)]
visit[1] = 1
while q:
    now = q.popleft()
    for node in tree[now]:
        if visit[node] == 0:
            visit[node] = now
            q.append(node)

for i in visit[2:]:
    print(i)
