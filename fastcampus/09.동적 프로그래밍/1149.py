import sys
input = sys.stdin.readline

n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(1, n):
    for x in range(3):
        if x == 0:
            board[y][x] += min(board[y-1][1], board[y-1][2])
        elif x == 1:
            board[y][x] += min(board[y - 1][0], board[y - 1][2])
        else:
            board[y][x] += min(board[y - 1][0], board[y - 1][1])

print(min(board[-1]))
