import sys
input = sys.stdin.readline

import heapq

n = int(input())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

val = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))

h = [(0, 0, 0)]

while h:
    l, x, y = heapq.heappop(h)
    if val[y][x] != -1:
        continue
    if y == n - 1 and x == n - 1:
        print(l)
        break
    val[y][x] = l
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if val[ny][nx] != -1:
                continue
            heapq.heappush(h, (max(l, abs(board[ny][nx] - board[y][x])), nx, ny))



