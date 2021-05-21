from collections import deque
def bfs():
    q = deque()
    q.append((0, n))
    visit = [0 for _ in range(100001)]
    visit[n] = 1
    while q:
        cnt, now = q.popleft()
        if now == k:
            return cnt
        for i in (now-1, now+1, now*2):
            if 0 <= i <= 100000 and visit[i] == 0:
                visit[i] = 1
                q.append((cnt+1, i))

n, k = map(int, input().split())
result = bfs()
print(result)

