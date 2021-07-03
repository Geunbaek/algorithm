import sys
input = sys.stdin.readline
# pypy
def check(row):
    for i in range(row):
        if board[i] == board[row]:
            return False
        if abs(board[row]-board[i]) == row-i:
            return False
    return True


def n_queen(n, row):
    global cnt
    if row >= n:
        cnt += 1
        return

    for i in range(n):
        board[row] = i
        if check(row):
            n_queen(n, row+1)

n = int(input())
board = [0] * n
cnt = 0
n_queen(n, 0)
print(cnt)
