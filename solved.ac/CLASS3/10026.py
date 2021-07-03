import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b, color, board):
    q = deque()
    q.append((a, b))
    board[b][a] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == color:
                    board[ny][nx] = 0
                    q.append((nx, ny))


n = int(input())
rgb_board = []
gb_board = []
rgb_cnt = 0
gb_cnt = 0

for _ in range(n):
    line = input().strip()
    rgb_board.append(list(line))
    line = line.replace("R", "G")
    gb_board.append(list(line))

for y in range(n):
    for x in range(n):
        if rgb_board[y][x] != 0:
            bfs(x, y, rgb_board[y][x], rgb_board)
            rgb_cnt += 1

for y in range(n):
    for x in range(n):
        if gb_board[y][x] != 0:
            bfs(x, y, gb_board[y][x], gb_board)
            gb_cnt += 1

print(rgb_cnt, gb_cnt)