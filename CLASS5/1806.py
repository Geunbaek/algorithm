import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0 for _ in range(len(arr)+1)]
dp[0] = 0

for i in range(1, len(arr)+1):
    dp[i] = dp[i-1] + arr[i-1]

left, right = n-1, n
ans = float('inf')

while left >= 0:
    while left >= 0:
        if dp[right] - dp[left] >= s:
            ans = min(ans, right-left)
            break
        else:
            left -= 1
    right -= 1
    if left >= right:
        left = right - 1

if ans == float('inf'):
    print(0)
else:
    print(ans)


"""
10 10
10 1 1 1 1 1 1 1 1 1 
"""

