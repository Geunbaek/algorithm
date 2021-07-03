import sys
input = sys.stdin.readline

def check(x1, y1, x2, y2):
    num = board[y1][x1]
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if board[y][x] != num:
                return False
    cnt[num+1] += 1
    return True


def solve(x1, y1, x2, y2, n):
    ck = check(x1, y1, x2, y2)
    if ck:
        return
    n //= 3
    solve(x1, y1, x1+n-1, y1+n-1,n)
    solve(x1+n, y1, x1+(2*n)-1, y1+n-1,n)
    solve(x1+(2*n), y1, x1+(3*n)-1, y1+n-1,n)
    solve(x1, y1+n, x1+n-1, y1+(2*n)-1,n)
    solve(x1+n, y1+n, x1+(2*n)-1, y1+(2*n)-1,n)
    solve(x1+(2*n), y1 + n, x1+(3*n)-1, y1+(2*n)-1,n)
    solve(x1, y1+(2*n), x1+n-1, y1+(3*n)-1,n)
    solve(x1+n, y1 + (2 * n), x1+(2*n)-1, y1 + (3 * n) - 1,n)
    solve(x1+(2*n), y1 + (2 * n), x1+(3*n)-1, y1 + (3 * n) - 1,n)


n = int(input())
board = []
cnt = [0 for i in range(3)]
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

solve(0,0,n-1,n-1, n)
for c in cnt:
    print(c)

