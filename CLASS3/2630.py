import sys
input = sys.stdin.readline

def check(x1, y1, x2, y2):
    num = board[y1][x1]
    if x1 == x2 and y1 == y2:
        return num
    for y in range(y1, y2+1):
        for x in range(x1, x2 + 1):
            if board[y][x] != num:
                return -1
    return num


def solve(x1, y1, x2, y2):
    global one_cnt
    global zero_cnt
    ck = check(x1, y1, x2, y2)
    if ck == 1:
        one_cnt +=1
        return
    if ck == 0:
        zero_cnt += 1
        return


    solve(x1, y1, (x1+x2)//2, (y1+y2)//2)
    solve((x1+x2)//2 +1, y1, x2, (y1+y2)//2)
    solve(x1, (y1+y2)//2 + 1, (x1+x2)//2, y2)
    solve((x1+x2)//2 +1, (y1+y2)//2 + 1, x2, y2)

n = int(input())
board = []
one_cnt =0
zero_cnt = 0

for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

solve(0, 0, n-1, n-1)
print(zero_cnt)
print(one_cnt)