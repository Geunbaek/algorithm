import sys
input = sys.stdin.readline

string = '0' + input().strip()
string2 = '0' + input().strip()

board = [[0 for _ in range(len(string))] for _ in range(len(string2))]

for y in range(1, len(string2)):
    for x in range(1, len(string)):
        if string2[y] == string[x]:
            board[y][x] = board[y-1][x-1] +1
        else:
            board[y][x] = max(board[y][x - 1], board[y - 1][x])


print(board[-1][-1])