import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n = int(input())
names = input().strip().split()
name_index = {name: index for index, name in enumerate(names)}
ans = defaultdict(list)
graph = [[] for _ in range(n)]
degree = [0 for _ in range(n)]

m = int(input())

for _ in range(m):
    x, y = input().strip().split()
    x_index, y_index = name_index[x], name_index[y]
    graph[y_index].append(x_index)
    degree[x_index] += 1

q = deque()
roots = []
for index, count in enumerate(degree):
    if count == 0:
        q.append(index)
        roots.append(names[index])

while q:
    now = q.popleft()
    for _next in graph[now]:
        degree[_next] -= 1
        if degree[_next] == 0:
            ans[now].append(_next)
            q.append(_next)

roots.sort()
print(len(roots))
print(" ".join(roots))

for name, index in sorted(name_index.items(), key = lambda x: x[0]):
    if not ans[index]:
        print(name, 0)
    else:
        temp = []
        for i in ans[index]:
            temp.append(names[i])
        temp.sort()
        print(name, len(ans[index]), *temp)

