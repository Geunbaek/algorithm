import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append(1)
    visit = [0 for _ in range(n+1)]
    visit[1] = 1
    cnt = -1
    while q:
        now = q.popleft()
        cnt += 1
        for num in graph[now]:
            if visit[num] == 0:
                visit[num] = 1
                q.append(num)
    return cnt

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs())

