import sys
input = sys.stdin.readline
from collections import deque

# solve 1
n = int(input())

dp = [[0, []] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n+1):

    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][1] + [i]

    if i % 2 == 0 and dp[i][0] > dp[i//2][0] + 1:
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]

    if i % 3 == 0 and dp[i][0] > dp[i//3][0] + 1:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]


print(dp[n][0])
print(' '.join(map(str, reversed(dp[n][1]))))

# solve 2

INF = 10 ** 8
q = deque()
q.append((n, [n]))
visit = [INF] * (n+1)
visit[n] = 0

while q:
    now, path = q.popleft()
    if now == 1:
        print(visit[now])
        print(' '.join(map(str, path)))
        break
    for i, ne in enumerate((now - 1, now // 2, now // 3)):
        if i == 1 and now % 2 != 0:
            continue
        if i == 2 and now % 3 != 0:
            continue

        if visit[ne] > visit[now] + 1:
            q.append((ne, path + [ne]))
            visit[ne] = visit[now] + 1











