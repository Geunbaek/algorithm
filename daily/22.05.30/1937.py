import sys
input = sys.stdin.readline
import heapq

n = int(input())
board = []
h = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dp = [[0 for _ in range(n)] for _ in range(n)]
ans = 0

for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(n):
        heapq.heappush(h, (-line[x], x, y))

while h:
    val, x, y = heapq.heappop(h)
    _max = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[ny][nx] > -val:
                _max = max(_max, dp[ny][nx])
    dp[y][x] = _max + 1
    ans = max(ans, dp[y][x])

print(ans)
