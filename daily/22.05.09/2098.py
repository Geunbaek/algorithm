import sys
input = sys.stdin.readline

def dfs(now, visit):
    if visit == (1 << n) - 1:
        if board[now][0]:
            return board[now][0]
        else:
            return INF

    if dp[now][visit] != INF:
        return dp[now][visit]

    for i in range(n):
        if not board[now][i]:
            continue
        if visit & (1 << i):
            continue

        dp[now][visit] = min( dp[now][visit], dfs(i, visit | (1 << i)) + board[now][i])
    return dp[now][visit]

n = int(input())
board = []
INF = 10**9
dp = [[INF for _ in range(1 << n)] for _ in range(n)]

for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

print(dfs(0, 1))


