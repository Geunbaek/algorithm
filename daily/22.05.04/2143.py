import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_dp = [0 for _ in range(n + 1)]
m_dp = [0 for _ in range(m + 1)]
n_dict = {}
ans = 0

for i in range(1, n + 1):
    n_dp[i] = n_dp[i - 1] + n_arr[i - 1]

for i in range(1, m + 1):
    m_dp[i] = m_dp[i - 1] + m_arr[i - 1]

for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        sums = n_dp[i] - n_dp[j]
        n_dict[sums] = n_dict.get(sums, 0) + 1

for i in range(1, m + 1):
    for j in range(i - 1, -1, -1):
        sums = m_dp[i] - m_dp[j]
        if t - sums in n_dict:
            ans += n_dict[t - sums]

print(ans)