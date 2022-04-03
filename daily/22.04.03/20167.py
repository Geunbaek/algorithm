import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append((start, dp[start][1] - k if dp[start][1] - k >= 0 else 0))
    val = 0

    while q:
        now, cur_val = q.popleft()
        val = max(val, cur_val)
        for i in range(now + dp[now][0], n):
            q.append((i, cur_val + (dp[i][1] - k if dp[i][1] - k >= 0 else 0)))
    return val

n, k = map(int, input().split())
worm = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)]
ans = 0

for i in range(n):
    val = worm[i]
    count = 1
    for j in range(i + 1, n):
        if val >= k:
            break
        val += worm[j]
        count += 1
    dp[i] = [count, val]

for i in range(n):
    ans = max(ans, bfs(i))

print(ans)