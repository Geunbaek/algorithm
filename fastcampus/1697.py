import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
ans = 0

def bfs():
    q = deque()
    q.append((n, 0))
    visit = [100001 for _ in range(100001)]
    visit[n] = 0
    while q:
        now, time = q.popleft()
        if now == k:
            return time
        for pos in (now + 1, now - 1, now * 2):
            if 0 <= pos < 100001 and visit[pos] > time:
                visit[pos] = time
                q.append((pos, time + 1))
print(bfs())