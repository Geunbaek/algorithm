import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(f + 1)]

q = deque()
q.append((s, 0))
visited[s] = 1
btns = []

if u:
    btns.append(u)
if d:
    btns.append(-d)

while q:
    now, count = q.popleft()

    if now == g:
        print(count)
        break

    for i in btns:
        next = now + i
        if 1 <= next <= f and visited[next] == 0:
            visited[next] = 1
            q.append((next, count + 1))
else:
    print("use the stairs")


