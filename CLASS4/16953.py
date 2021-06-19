import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))

while q:
    now, cnt = q.popleft()
    if now == b:
        print(cnt)
        exit()
    for ne in (now * 2, int(str(now) + "1")):
        if ne <= b:
            q.append((ne, cnt + 1))
print(-1)



