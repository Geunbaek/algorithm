import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
ans = -sys.maxsize
for i in range(n):
    dp[i + 1] = dp[i] + arr[i]

for l in range(n-k+1):
    ans = max(ans, dp[l+k] - dp[l])
print(ans)
