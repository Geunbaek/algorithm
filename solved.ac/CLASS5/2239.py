import sys
input = sys.stdin.readline
# pypy
def ck(a, b, num):
    x = (a//3)*3
    y = (b//3)*3
    for i in range(y, y+3):
        for j in range(x, x+3):
            if board[i][j] == num:
                return False

    for i in range(9):
        if board[b][i] == num:
            return False
        if board[i][a] == num:
            return False
    return True

def recur(x, y):
    global state
    if y >= 9:
        for elem in board:
            print(''.join(map(str, elem)))
        state = True
        return

    if state:
        return

    if board[y][x] != 0:
        if x < 8:
            recur(x + 1, y)
        else:
            recur(0, y + 1)

    for i in range(1, 10):
        if board[y][x] == 0:
            if ck(x, y, i):
                board[y][x] = i
                if x < 8:
                    recur(x+1, y)
                else:
                    recur(0, y+1)
                board[y][x] = 0

board = []
for _ in range(9):
    board.append(list(map(int, input().strip())))
results = []
state = False
recur(0,0)

