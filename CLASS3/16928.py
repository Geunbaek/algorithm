import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global result
    q = deque()
    q.append((1, 0, [1]))
    visit = [101 for _ in range(101)]
    while q:
        now,cnt, path = q.popleft()
        if now == 100:
            result = min(result, cnt)
        for i in range(6, 0, -1):
            next = now + i
            if next <= 100 and visit[next] > cnt+1:
                visit[next] = cnt+1
                if down[next]:
                    for dn in down[next]:
                        q.append((dn, cnt + 1, path + [dn]))
                elif graph[next]:
                    for dn in graph[next]:
                        q.append((dn, cnt+1, path+[dn]))
                else:
                    q.append((next, cnt+1, path+[next]))

n, m = map(int, input().split())
result = 101
graph = [[] for _ in range(101)]
down = [[] for _ in range(101)]

for _ in range(n):
    x, y = map(int,input().split())
    graph[x].append(y)

for _ in range(m):
    u, v = map(int, input().split())
    down[u].append(v)

bfs()
print(result)
