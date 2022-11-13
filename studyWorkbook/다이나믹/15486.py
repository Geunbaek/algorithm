import sys

input = sys.stdin.readline

n = int(input())
works = []

for _ in range(n):
    t, p = map(int, input().split())
    works.append((t, p))

dp = [0 for _ in range(n + 1)]

for i, work in enumerate(works):
    t, p = work
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    elif i - 1 >= 0:
        dp[i] = max(dp[i], dp[i - 1])

print(max(dp))