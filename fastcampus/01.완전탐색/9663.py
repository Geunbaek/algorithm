import sys

input = sys.stdin.readline

n = int(input())

board = [0] * n
count = 0

def attackable(r1, c1, r2, c2):
    if c1 == c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    return False

def n_queen(y):
    global count
    if y == n:
        count += 1
        return
    else:
        for cand in range(n):
            possible = True
            for i in range(y):
                if attackable(y, cand, i, board[i]):
                    possible = False
                    break
            if possible:
                board[y] = cand
                n_queen(y+1)
                board[y] = 0

n_queen(0)
print(count)

