import sys
input = sys.stdin.readline
from collections import deque

def sudoku(i):
    if i >= len(zero):
        for b in board:
            print(*b)
        exit()
    for j in range(1, 10):
        x, y = zero[i]
        if check(x, y, j):
            board[y][x] = j
            sudoku(i + 1)
            board[y][x] = 0

def check(x, y, num):
    sx = x - x % 3
    sy = y - y % 3

    ex = sx + 3
    ey = sy + 3

    for i in range(9):
        if board[y][i] == num:
            return False

    for i in range(9):
        if board[i][x] == num:
            return False

    for i in range(sy, ey):
        for j in range(sx, ex):
            if board[i][j] == num:
                return False
    return True

board = []
zero = deque()

for y in range(9):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(9):
        if board[y][x] == 0:
            zero.append((x, y))

sudoku(0)


"""
0 0 0 0 0 0 0 0 9
0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 1
"""