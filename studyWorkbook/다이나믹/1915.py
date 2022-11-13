import sys
input = sys.stdin.readline

def getAreas(a, b):
    areas = [1]
    count = 1
    while True:
        nx = a + count
        ny = b + count
        if not (0 <= nx < m + 1 and 0 <= ny < n + 1):
            break
        area = dp[ny][nx] - dp[b - 1][nx] - dp[ny][a - 1] + dp[b - 1][a - 1]

        if area == (count + 1) ** 2:
            areas.append(area)
        else:
            break
        count += 1
    return areas


n, m = map(int, input().split())
board = [[0 for _ in range(m + 1)]]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for _ in range(n):
    board.append([0] + list(map(int, list(input().strip()))))

for y in range(1, n + 1):
    temp = 0
    for x in range(1, m + 1):
        temp += board[y][x]
        dp[y][x] = temp

for x in range(1, m + 1):
    temp = 0
    for y in range(1, n + 1):
        temp += dp[y][x]
        dp[y][x] = temp


ans = 0
for y in range(1, n + 1):
    for x in range(1, m + 1):
        if board[y][x] == 1:
            ans = max([ans] + getAreas(x, y))

print(ans)

"""
3 3
101
011
111
"""