import sys
input = sys.stdin.readline

def check(x1, y1, x2, y2):
    temp = dp[y1][x1]
    temp -= dp[y1][x2 - 1] if x2 != 0 else 0
    temp -= dp[y2 - 1][x1] if y2 != 0 else 0
    temp += dp[y2 - 1][x2 - 1] if y != 0 and x != 0 else 0
    return temp == 0



def oper(x, y):
    global ans
    r = min(x, y)

    if r <= ans:
        return

    for i in range(ans, r):
        if check(x, y, x - i, y - i):
            ans = max(ans, i + 1)


n, m = map(int, input().split())
board = []
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
ans = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(1, n + 1):
    for x in range(1, m + 1):
        if board[y - 1][x - 1] == 0:
            dp[y][x] = min(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1]) + 1
            ans = max(ans, dp[y][x])
print(ans)


