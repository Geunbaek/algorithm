import sys

input = sys.stdin.readline

def check(x, y):
    if board[y][x] == 0:
        return False

    if left_diag[x + y] or right_diag[x - y + n - 1]:
        return False

    return True

def n_bishop(bishop, index, count, type):
    flag = False
    for i in range(index, len(bishop)):
        x, y = bishop[i]
        if check(x, y):
            left_diag[x + y] = 1
            right_diag[x - y + n - 1] = 1
            n_bishop(bishop, i, count + 1, type)
            left_diag[x + y] = 0
            right_diag[x - y + n - 1] = 0
            flag = True

    if not flag:
        ans[type] = max(ans[type], count)
        return



n = int(input())
board = []
board_color = [[0 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        if (x + y) % 2 == 0:
            board_color[y][x] = 1

left_diag = [0 for _ in range(2 * (n - 1) + 1)]
right_diag = [0 for _ in range(2 * (n - 1) + 1)]
white = []
black = []

ans = [0, 0]
for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(n):
        if line[x] == 1 and board_color[y][x] == 1:
            black.append((x, y))
        elif line[x] == 1 and board_color[y][x] == 0:
            white.append((x, y))

n_bishop(black, 0, 0, 1)
n_bishop(white, 0, 0, 0)

print(sum(ans))