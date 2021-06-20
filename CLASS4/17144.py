import sys
input = sys.stdin.readline
from collections import deque

# pypy

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def ex_m():
    m_li = []
    for y in range(r):
        for x in range(c):
            if board[y][x] > 0:
                m_li.append((x, y, board[y][x]))

    for mx, my, val in m_li:
        tmp = val // 5
        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if board[ny][nx] != -1:
                    board[ny][nx] += tmp
                    board[my][mx] -= tmp

def clean_up():
    q = deque()
    cx, cy = cleaner[0]
    q.append((cx, cy-1, 0))

    while q:
        x, y, d = q.popleft()
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= c or ny < 0 or ny > cy:
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        if board[ny][nx] == -1:
            board[y][x] = 0
            break
        else:
            board[y][x] = board[ny][nx]
            q.append((nx, ny, d))

def clean_down():
    q = deque()
    cx, cy = cleaner[1]
    q.append((cx, cy + 1, 2))

    while q:
        x, y, d = q.popleft()
        nx = x + dx[d]
        ny = y + dy[d]
        if ny >= r or nx >= c or ny < cy:
            d = d - 1
            if d < 0:
                d = 3
            nx = x + dx[d]
            ny = y + dy[d]
        if board[ny][nx] == -1:
            board[y][x] = 0
            break
        else:
            board[y][x] = board[ny][nx]
            q.append((nx, ny, d))


r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

cleaner = []

for y in range(r):
    if board[y][0] == -1:
        cleaner.append((0, y))

for _ in range(t):
    ex_m()
    clean_up()
    clean_down()

result = 0

for y in range(r):
    for x in range(c):
        if board[y][x] != -1:
            result += board[y][x]

print(result)

