import sys
input = sys.stdin.readline

def check(x1, y1, x2, y2):
    tmp = board[y1][x1]
    if x1 == x2 and y1 == y2:
        return tmp
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if board[y][x] != tmp:
                return -1
    return tmp

def recur(x1, y1, x2, y2):
    ck = check(x1, y1, x2, y2)
    if ck != -1:
        return str(ck)
    ans.append('(')
    ans.append(recur(x1, y1, (x1+x2)//2, (y1+y2)//2))
    ans.append(recur((x1+x2)//2+1, y1, x2, (y1+y2)//2))
    ans.append(recur(x1, (y1+y2)//2 + 1, (x1+x2)//2, y2))
    ans.append(recur((x1+x2)//2+1, (y1+y2)//2+1, x2, y2))
    ans.append(')')

n = int(input())
board = []
ans = []

for _ in range(n):
    line = list(map(int, input().strip()))
    board.append(line)

if check(0, 0, n-1, n-1) != -1:
    print(str(board[0][0]))
    exit()

recur(0,0,n-1, n-1)
ans = list(filter(None, ans))
print("".join(ans))


"""

8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
"""