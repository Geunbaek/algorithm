import sys
input = sys.stdin.readline

def dfs(depth, path):
    if depth >= n:

        result.append(path)
        return
    if depth == 0:
        dfs(depth + 1, path + [1])
    else:
        if path[-1] != 1:
            dfs(depth + 1, path + [1])
            dfs(depth + 1, path + [0])
        else:
            dfs(depth + 1, path + [0])


n = int(input())
dp = [0 for _ in range(91)]

dp[1] = 1
dp[2] = 1
for i in range(3, n+ 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])