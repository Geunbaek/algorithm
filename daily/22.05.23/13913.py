import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
q = deque()
visit = [0 for _ in range(100001)]
dist = [0 for _ in range(100001)]
q.append((n, 0))

while q:
    now, count = q.popleft()
    if now == k:
        print(dist[k])
        prev = now
        break
    for next_ in (now + 1, now - 1, now * 2):
        if 0 <= next_ <= 100000 and dist[next_] == 0:
            dist[next_] = count + 1
            visit[next_] = now
            q.append((next_, count + 1))

ans = []

print(visit[:10], prev)
for i in range(dist[k] + 1):
    ans.append(prev)
    prev = visit[prev]
print(*ans[::-1])

