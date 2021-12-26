import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((0, 1))

    while q:
        clip, now = q.popleft()
        if dp[now][now] == -1:
            dp[now][now] = dp[now][clip] + 1
            q.append((now, now))
        if now + clip <= s and dp[now + clip][clip] == -1:
            dp[now + clip][clip] = dp[now][clip] + 1
            q.append((clip, now + clip))
        if now - 1 >= 1 and dp[now - 1][clip] == -1:
            dp[now - 1][clip] = dp[now][clip] + 1
            q.append((clip, now - 1))


s = int(input())

dp = [[-1 for _ in range(s + 1)] for _ in range(s + 1)]
dp[1][0] = 0
bfs()

ans = -1
for x in range(s + 1):
    if dp[s][x] != -1:
        if ans == -1 or ans > dp[s][x]:
            ans = dp[s][x]

print(ans)