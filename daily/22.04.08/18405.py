import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, k = map(int, input().split())
board = []
virus = []

for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(len(line)):
        if line[x] != 0:
            virus.append((line[x], x, y))

s, x1, y1 = map(int, input().split())

virus.sort(key = lambda x: x[0])
q = deque(virus)

while s:
    length = len(q)
    temp = []
    while length:
        v_num, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 0:
                    board[ny][nx] = v_num
                    temp.append((v_num, nx, ny))
        length -= 1
    temp.sort(key = lambda x: x[0])
    q = deque(temp)
    s -= 1

print(board[x1 - 1][y1 - 1])

