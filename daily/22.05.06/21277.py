import sys
input = sys.stdin.readline

def rotate(arr):
    temp = []

    for x1 in range(len(arr[0])):
        temp.append([])
        for y1 in range(len(arr) - 1, -1, -1):
            temp[-1].append(arr[y1][x1])

    return temp

def compare(x, y, cb, p):
    for y1 in range(y, y + py):
        for x1 in range(x, x + px):
            if cb[y1][x1] == "1" and p[y1 - y][x1 - x] == "1":
                return 0
    left = min(px, x)
    right = max(px + m, x + px)
    top = min(py, y)
    bottom = max(py + n, y + py)

    return (bottom - top) * (right - left)

n, m = map(int, input().split())
board = []

for _ in range(n):
    line = list(input().strip())
    board.append(line)

n2, m2 = map(int, input().split())
puzzle = []

for _ in range(n2):
    line = list(input().strip())
    puzzle.append(line)

ans = sys.maxsize
for i in range(4):
    if i != 0:
        puzzle = rotate(puzzle)

    px = len(puzzle[0])
    py = len(puzzle)
    check_board = [[0 for _ in range(m + px * 2)] for _ in range(n + py * 2)]

    for y in range(py, py + n):
        for x in range(px, px + m):
            check_board[y][x] = board[y - py][x - px]
    for y in range(n + py + 1):
        for x in range(m + px + 1):
            area = compare(x, y, check_board, puzzle)
            if area != 0:
                ans = min(ans, area)
print(ans)


